package com.d212.taiso.dto;

// DTO를 만드는 이유
// 여러 개의 정보를 한 번에 묶어서 전달을 하는 것
// 2가지 케이스의 합집합을 해서 DTO를 짬. -> 첨 알았네(유사한 것만 이렇게 하는 듯)

import lombok.Data;

@Data
public class CartItemDTO {

    private String email;

    private Long pno;

    private int qty;

    private Long cino;
}
