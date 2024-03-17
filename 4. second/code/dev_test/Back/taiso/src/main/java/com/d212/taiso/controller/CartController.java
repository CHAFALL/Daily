package com.d212.taiso.controller;

import com.d212.taiso.dto.CartItemDTO;
import com.d212.taiso.dto.CartItemListDTO;
import com.d212.taiso.service.CartService;
import lombok.RequiredArgsConstructor;
import lombok.extern.log4j.Log4j2;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;

import java.security.Principal;
import java.util.List;

@RestController
@RequiredArgsConstructor
@Log4j2
@RequestMapping("api/cart")
public class CartController {
    private final CartService cartService;

    // 시큐리티 영역 안에 있으므로
    @PreAuthorize("#itemDTO.email == authentication.name")
    @PostMapping("/change")
    public List<CartItemListDTO> changeCart(@RequestBody CartItemDTO itemDTO) {
        log.info(itemDTO);

        if (itemDTO.getQty() <= 0) {
            return cartService.remove(itemDTO.getCino());
        }

        return cartService.addOrModify(itemDTO);
    }

    // 로그인한 사용자는 굳이 파라미터 값으로 자기 이메일을 안 던져도 되잖아!!
    @PreAuthorize("hasRole('ROLE_USER')")
    @GetMapping("/items")
    public List<CartItemListDTO> getCartItems(Principal principal) {
        String email = principal.getName();

        log.info("email: " + email);

        return cartService.getCartItems(email);
    }

    @PreAuthorize("hasAnyRole('ROLE_USER')")
    @DeleteMapping("/{cino}")
    public List<CartItemListDTO> removeFromCart(
            @PathVariable("cino") Long cino
    ){
        log.info("cart item no: " + cino);
        return cartService.remove(cino);
    }

}
