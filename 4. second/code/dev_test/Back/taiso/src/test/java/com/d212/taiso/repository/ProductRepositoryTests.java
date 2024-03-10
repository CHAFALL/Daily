package com.d212.taiso.repository;

import com.d212.taiso.domain.Product;
import com.d212.taiso.dto.PageRequestDTO;
import jakarta.transaction.Transactional;
import lombok.extern.log4j.Log4j2;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.test.annotation.Commit;

import java.util.Arrays;
import java.util.Optional;
import java.util.UUID;

@SpringBootTest
@Log4j2
public class ProductRepositoryTests {

    @Autowired
    private ProductRepository productRepository;

    @Test
    public void testInsert() {

        for (int i = 0; i < 10; i++) {
            Product product = Product.builder()
                    .pname("Test" + i)
                    .pdesc("Test Desc" + i)
                    .price(1000)
                    .build();

            product.addImageString(UUID.randomUUID()+"_"+"IMAGE1.jpg");
            product.addImageString(UUID.randomUUID()+"_"+"IMAGE2.jpg");

            productRepository.save(product);
        }

    }

    @Test
    public void testRead2() {
        Long pno = 1L;
        Optional<Product> result = productRepository.selectOne(pno);
        Product product = result.orElseThrow();
        log.info(product);
        log.info(product.getImageList());
    }

    @Commit
    @Transactional
    @Test
    public void testDelete() {
        Long pno = 2L;

        productRepository.updateToDelete(2L, true);
    }

    @Test
    public void testUpdate() {

        Product product = productRepository.selectOne(1L).get();

        product.changePrice(3000);

        // 이렇게 clearList()를 안하고 그냥 다른 어레이리스트로 바꿔치면 안되냐?
        //jpa가 어레이리스트를 관리하고 있어서 이 어레이리스트가 아닌 다른 어레이리스트로 바꾸면
        // 문제가 생김
        // 컬렉션 같은 것을 처리할 때는 얘가 물고있는 컬렉션을 계속 써야 됨
        // 2개를 지우고 3개를 추가함
        product.clearList();

        product.addImageString(UUID.randomUUID()+"_"+"PIMAGE1.jpg");
        product.addImageString(UUID.randomUUID()+"_"+"PIMAGE2.jpg");
        product.addImageString(UUID.randomUUID()+"_"+"PIMAGE3.jpg");

        productRepository.save(product);
    }

    @Test
    public void testList() {
        Pageable pageable = PageRequest.of(0, 10, Sort.by("pno").descending());
        Page<Object[]> result = productRepository.selectList(pageable);

        result.getContent().forEach(arr -> log.info(Arrays.toString(arr)));
    }

    @Test
    public void testSearch() {
        PageRequestDTO pageRequestDTO = PageRequestDTO.builder().build();

        productRepository.searchList(pageRequestDTO);
    }

}
