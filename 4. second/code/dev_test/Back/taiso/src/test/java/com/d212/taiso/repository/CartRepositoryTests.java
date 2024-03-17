package com.d212.taiso.repository;

import com.d212.taiso.domain.Cart;
import com.d212.taiso.domain.CartItem;
import com.d212.taiso.domain.Member;
import com.d212.taiso.domain.Product;
import com.d212.taiso.dto.CartItemListDTO;
import lombok.extern.log4j.Log4j2;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.annotation.Commit;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;

@SpringBootTest
@Log4j2
public class CartRepositoryTests {

    @Autowired
    private CartRepository cartRepository;

    @Autowired
    private CartItemRepository cartItemRepository;


    // @Commit은 테스트 메소드가 완료된 후에 트랜잭션을 커밋하도록 지시합니다.
    // 테스트가 완료된 후에 트랜잭션을 커밋하면 테스트 중에 수행된 변경 사항이 데이터베이스에 영구적으로 유지되므로,
    // 테스트 완료 후에도 데이터베이스가 알려진 상태로 유지되는데 도움이 됩니다.
    // 하지만 일반적으로 유닛 테스트에서는 각 테스트 메소드 전후에
    // 데이터베이스를 알려진 상태로 유지하기 위해 롤백하는 것이 일반적입니다.

    // 실제로 테스트 결과가 DB에 반영을 했으면 좋겠으면 @Transactional과 @Commit
    @Transactional
    @Commit
    @Test
    public void testInsertByProduct() {
        String email = "user1@aaa.com";
        Long pno = 6L;
        int qty = 2;

        // 이메일 상품번호로 장바구니에 아이템이 기존에 있었는지 여부를 판단, 없으면 추가하고 있으면 수량 변경해서 저장

        CartItem cartItem = cartItemRepository.getItemOfPno(email, pno);

        // 이미 사용자의 장바구니에 담겨있는 경우
        if (cartItem != null) {
            cartItem.changeQty(qty);
            cartItemRepository.save(cartItem);
            return;
        }

        // 사용자의 장바구니에 장바구니 아이템을 만들어서 저장
        // 장바구니 자체가 없을 수도 있음

        Optional<Cart> result = cartRepository.getCartOfMember(email);

        // 있는 경우도 있을 수 있어서 변수로 빼둠.
        Cart cart = null;

        if (result.isEmpty()) {
            log.info("MemberCart is not exist!!");
            // 음.. 생각 빡인데...
            Member member = Member.builder().email(email).build();
            Cart tempCart = Cart.builder().owner(member).build();

            cart = cartRepository.save(tempCart);
        } else { // 장바구니는 있으나 해당 상품의 장바구니 아이템은 없는 경우
            cart = result.get();
        }

        log.info(cart);

        //if (cartItem == null) {
        Product product = Product.builder().pno(pno).build(); // 카트 아이템에다가 담을 상품 생성
        cartItem = CartItem.builder().cart(cart).product(product).qty(qty).build();
        //}

        cartItemRepository.save(cartItem);

    }

    @Test
    public void testListOfMember() {
        String email = "user1@aaa.com";

        List<CartItemListDTO> cartItemListDTOList = cartItemRepository.getItemsOfCartDTOByEmail(email);

        for (CartItemListDTO dto : cartItemListDTOList) {
            log.info(dto);
        }

    }

    @Transactional
    @Commit
    @Test
    public void testUpdateByCino() {
        Long cino = 1L;
        int qty = 4;

        Optional<CartItem> result = cartItemRepository.findById(cino);

        CartItem cartItem = result.orElseThrow();

        cartItem.changeQty(qty);

        cartItemRepository.save(cartItem);
    }

    @Test
    public void testDeleteThenList() {
        Long cino = 1L;

        Long cno = cartItemRepository.getCartFromItem(cino);

        cartItemRepository.deleteById(cino);

        // 삭제한 다음에 다시 조회
        List<CartItemListDTO> cartItemList = cartItemRepository.getItemsOfCartDTOByCart(cno);

        for (CartItemListDTO dto : cartItemList) {
            log.info(dto);
        }
    }
}
