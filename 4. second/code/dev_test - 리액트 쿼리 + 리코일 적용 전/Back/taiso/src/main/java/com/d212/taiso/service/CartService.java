package com.d212.taiso.service;

import com.d212.taiso.dto.CartItemDTO;
import com.d212.taiso.dto.CartItemListDTO;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;


// 반환값을 보면 전부 DTO로 되어있는 것을 알 수 있다. -> axios를 덜 쓰게 하기 위해서 조회까지 같이 해주는 느낌.
@Transactional
public interface CartService {
    List<CartItemListDTO> addOrModify(CartItemDTO cartItemDTO);

    List<CartItemListDTO> getCartItems(String email);

    List<CartItemListDTO> remove(Long cino);
}
