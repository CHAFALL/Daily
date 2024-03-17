package com.d212.taiso.service;

import com.d212.taiso.dto.PageRequestDTO;
import com.d212.taiso.dto.PageResponseDTO;
import com.d212.taiso.dto.ProductDTO;
import org.springframework.transaction.annotation.Transactional;

@Transactional
public interface ProductService {

    PageResponseDTO<ProductDTO> getList(PageRequestDTO pageRequestDTO);

    Long register(ProductDTO productDTO);

    ProductDTO get(Long pno);

    void modify(ProductDTO productDTO);

    // 엘리먼트 컬렉션의 장점은 종속적인 애이므로 엔티티가 지워지면 같이 지워짐.
    void remove(Long pno);
}
