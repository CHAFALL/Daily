package com.d212.taiso.service;

import com.d212.taiso.domain.Product;
import com.d212.taiso.domain.ProductImage;
import com.d212.taiso.dto.PageRequestDTO;
import com.d212.taiso.dto.PageResponseDTO;
import com.d212.taiso.dto.ProductDTO;
import com.d212.taiso.repository.ProductRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.log4j.Log4j2;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;


@Service
@Log4j2
@RequiredArgsConstructor
public class ProductServiceImpl implements ProductService {

    private final ProductRepository productRepository;

    @Override
    public PageResponseDTO<ProductDTO> getList(PageRequestDTO pageRequestDTO) {

        Pageable pageable = PageRequest.of(pageRequestDTO.getPage() - 1,
                pageRequestDTO.getSize(),
                Sort.by("pno").descending());

        Page<Object[]> result = productRepository.selectList(pageable);

        // Object[] => 0: product 1: productImage

        List<ProductDTO> dtoList = result.get().map(arr -> {

            ProductDTO productDTO = null;

            Product product = (Product) arr[0];
            ProductImage productImage = (ProductImage) arr[1];

            productDTO =  ProductDTO.builder()
                    .pno(product.getPno())
                    .pname(product.getPname())
                    .pdesc(product.getPdesc())
                    .price(product.getPrice())
                    .build();

            String imageStr = productImage.getFileName();
            productDTO.setUploadFileNames(List.of(imageStr));


        return productDTO;
        }).collect(Collectors.toList());

        long totalCount = result.getTotalElements();

        return PageResponseDTO.<ProductDTO>withAll()
                .dtoList(dtoList)
                .total(totalCount)
                .pageRequestDTO(pageRequestDTO)
                .build();
    }

    @Override
    public Long register(ProductDTO productDTO) {

        Product product = dtoToEntity(productDTO);

        log.info("----------------------");
        log.info(product);
        log.info(product.getImageList());

        Long pno = productRepository.save(product).getPno();

        return pno;
    }

    @Override
    public ProductDTO get(Long pno) {

        Optional<Product> result = productRepository.findById(pno);

        Product product = result.orElseThrow();

        ProductDTO productDTO = entityToDTO(product);

        return productDTO;

    }

    @Override
    public void modify(ProductDTO productDTO) {
        // 조회
        Optional<Product> result = productRepository.findById(productDTO.getPno());

        Product product = result.orElseThrow();
        // 변경 내용 반영,
        product.changePrice(productDTO.getPrice());
        product.changeName(productDTO.getPname());
        product.changeDesc(product.getPdesc());
        product.changeDel(productDTO.isDelFlag());

        // 이미지 처리
        List<String> uploadFileNames = productDTO.getUploadFileNames();

        // (근데 파일 변경 여부를 알 수가 없음)
        product.clearList();

        if (uploadFileNames != null && !uploadFileNames.isEmpty()) {
            uploadFileNames.forEach(uploadName -> {
                product.addImageString(uploadName);
            });
        }

        // 저장
        productRepository.save(product);
    }


    // 원래대로라면 삭제 기능은 없고 Delete Flag 값을 변경하는 것 뿐이다.
    // 삭제를 실제로 하는 것을 한번 연습해보기 위해서 작성했을 뿐 실제로는 삭제 x해야 된다.
    @Override
    public void remove(Long pno) {
        productRepository.deleteById(pno);
    }

    public ProductDTO entityToDTO(Product product) {

        ProductDTO productDTO = ProductDTO.builder()
                .pno(product.getPno())
                .pname(product.getPname())
                .pdesc(product.getPdesc())
                .price(product.getPrice())
                .delFlag(product.isDelFlag())
                .build();

        List<ProductImage> imageList = product.getImageList();

        if(imageList == null || imageList.isEmpty()){
            return productDTO;
        }

        List<String> fileNameList = imageList.stream().map(productImage ->
                productImage.getFileName()).toList();

        productDTO.setUploadFileNames(fileNameList);
        return productDTO;

    }

    private Product dtoToEntity(ProductDTO productDTO) {
        Product product = Product.builder()
                .pno(productDTO.getPno())
                .pname(productDTO.getPname())
                .pdesc(productDTO.getPdesc())
                .price(productDTO.getPrice())
                .build();

        // 엔티티 안의 컬렉션은 새로 만들면 문제가 커짐.
        List<String> uploadFileNames = productDTO.getUploadFileNames();

        if (uploadFileNames == null || uploadFileNames.size() == 0) {

            return product;
        }

        uploadFileNames.forEach(fileName -> {
            product.addImageString(fileName);
        });

        return product;
    }
}
