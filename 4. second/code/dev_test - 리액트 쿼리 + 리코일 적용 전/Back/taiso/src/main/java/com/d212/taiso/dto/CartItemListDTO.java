package com.d212.taiso.dto;

// DTO는 상황에 따라서 여러 개를 만드는 것이 잘못이 아님

import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@Builder
@NoArgsConstructor
public class CartItemListDTO {
    private Long cino;

    private int qty;

    private String pname;

    private int price;

    private Long pno;

    private String imageFile;

    // 이번엔 생성자를 이렇게 넣은 이유
    // JPA 기능 중에서 프로젝션스라고 해서 그냥 바로 dto를 뽑는 기능이 있다.
    // 그걸 쓰려고
    // 왜 롬복이로 안 만듬??? -> 헷갈리므로(몇 번째 파라미터가 들어갔는지 모르므로)
    public CartItemListDTO(Long cino, int qty, String pname, int price, Long pno, String imageFile) {
        this.cino = cino;
        this.qty = qty;
        this.pname = pname;
        this.price = price;
        this.pno = pno;
        this.imageFile = imageFile;
    }
}
