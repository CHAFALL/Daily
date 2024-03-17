package com.d212.taiso.service;

import com.d212.taiso.domain.Cart;
import com.d212.taiso.domain.CartItem;
import com.d212.taiso.domain.Member;
import com.d212.taiso.domain.Product;
import com.d212.taiso.dto.CartItemDTO;
import com.d212.taiso.dto.CartItemListDTO;
import com.d212.taiso.repository.CartItemRepository;
import com.d212.taiso.repository.CartRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.log4j.Log4j2;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
@Log4j2
@RequiredArgsConstructor
public class CartServiceImpl implements CartService{

    private final CartRepository cartRepository;

    private final CartItemRepository cartItemRepository;

    @Override
    public List<CartItemListDTO> addOrModify(CartItemDTO cartItemDTO) {

        String email = cartItemDTO.getEmail();
        Long pno = cartItemDTO.getPno();
        int qty = cartItemDTO.getQty();
        Long cino = cartItemDTO.getCino();

        // 장바구니 번호가 있는 경우 // 기존에 담겨있는 상품에 대한 처리
        if (cino != null) {
            Optional<CartItem> cartItemResult = cartItemRepository.findById(cino);

            CartItem cartItem = cartItemResult.orElseThrow();

            cartItem.changeQty(qty);

            cartItemRepository.save(cartItem);

            return getCartItems(email);
        }

        Cart cart = getCart(email);

        CartItem cartItem = null;

        cartItem = cartItemRepository.getItemOfPno(email, pno);

        //  이 상품은 장바구니에 장바구니 아이템으로 추가된 적이 없는 경우
        if (cartItem == null) {
            // 장바구니 아이템을 새로 만들기
            Product product = Product.builder().pno(pno).build();
            cartItem = CartItem.builder().product(product).cart(cart).qty(qty).build();
        } else {
            cartItem.changeQty(qty);
        }

        cartItemRepository.save(cartItem);

        return getCartItems(email);
    }

    private Cart getCart(String email) {

        // 해당 email의 장바구니(Cart)아 있는지 확인, 있으면 반환

        // 없으면 Cart 객체 생성하고 추가 반환

        Cart cart = null;
        Optional<Cart> result = cartRepository.getCartOfMember(email);
        if(result.isEmpty()) {
            log.info("Cart of the member is not exist!!");
            Member member = Member.builder().email(email).build();
            Cart tempCart = Cart.builder().owner(member).build();
            cart = cartRepository.save(tempCart);
        }else {
            cart = result.get();
        }
        return cart;
    }

    @Override
    public List<CartItemListDTO> getCartItems(String email) {
        return cartItemRepository.getItemsOfCartDTOByEmail(email);
    }

    @Override
    public List<CartItemListDTO> remove(Long cino) {
        // 삭제를 하려면 장바구니 아이템이 있는 카트 아이템의 상위인 카트의 번호를 알아야 한다.
        Long cno = cartItemRepository.getCartFromItem(cino);

        cartItemRepository.deleteById(cino);

        return cartItemRepository.getItemsOfCartDTOByCart(cno);
    }
}
