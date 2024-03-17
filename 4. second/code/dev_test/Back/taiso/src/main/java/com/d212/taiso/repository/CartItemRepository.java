package com.d212.taiso.repository;

import com.d212.taiso.domain.CartItem;
import com.d212.taiso.dto.CartItemListDTO;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;

public interface CartItemRepository extends JpaRepository<CartItem, Long> {

    // input -> email, output -> CartItemListDTO
    // 엔티티를 DTO로 DTO를 엔티티로 바꾸는 작업은 서비스 쪽에서 했었다.
    // 근데 이번에 프로젝션스라는 것을 이용할 것이므로 한번에 처리가 가능하다.
    // 특정한 사용자의 모든 장바구니 아이템들을 가져올 경우
    // 엘리먼트 컬렉션은 엔티티가 아니어서 당당하게 Product p 이런식으로 못 쓰고 p.imageList이런식으로만 가능


    // INNER JOIN : 교집합
    // LEFT JOIN : 왼쪽 테이블의 모든 행과 오른쪽 테이블의 일치하는 행을 반환
    // 여기서 INNER JOIN을 LEFT로 해도 되었지만 1대1 관계라 그냥 INNER JOIN으로 함
    // mc : 멤버의 카트
    // 조금 조금씩 추가하면서 test 돌리면서 select문을 보고 파악하는구나
//    @Query("select ci, mc, p " +
//            "from " +
//            "CartItem ci inner join Cart mc on ci.cart = mc " +
//            "left join Product p on ci.product = p " +
//            "left join p.imageList pi " +
//            "where " +
//            "pi.ord = 0 " +
//            "and mc.owner.email = :email order by ci.cino desc ")

    // Long cino, int qty, String pname, int price, String imageFile

    // 이렇게 하면 한번에 바로 DTO까지 뽑아낼 수 있다.
    @Query("select " +
            "new com.d212.taiso.dto.CartItemListDTO(ci.cino, ci.qty, p.pname, p.price, p.pno, pi.fileName ) " +
            "from " +
            "CartItem ci inner join Cart mc on ci.cart = mc " +
            "left join Product p on ci.product = p " +
            "left join p.imageList pi " +
            "where " +
            "pi.ord = 0 " +
            "and mc.owner.email = :email order by ci.cino desc ")
    List<CartItemListDTO> getItemsOfCartDTOByEmail(@Param("email") String email);

    // 이메일, 상품 번호로 해당 상품이 이미 장바구니 아이템으로 존재하는지 확인 필요
    @Query("select ci from CartItem ci left join Cart c on ci.cart = c " +
            "where c.owner.email = :email and ci.product.pno = :pno")
    CartItem getItemOfPno(@Param("email") String email, @Param("pno") Long pno);

    // 장바구니 아이템 번호로 장바구니 번호를 얻어오려고 하는 경우
    // 어떤 장바구니 아이템(장바구니에 들어가 있는 번호)이 있는데 그 번호 가지고 삭제 같은 것을 할 때 문제가 됨
    // 끄집어 낼 수 있는지 한번 확인해보는 용도로 쓰려고
    @Query("select c.cno from Cart c left join CartItem ci on ci.cart = c where ci.cino = :cino")
    Long getCartFromItem(@Param("cino") Long cino);

    // 장바구니 번호로 모든 장바구니 아이템을 조회
    @Query("select " +
            "new com.d212.taiso.dto.CartItemListDTO(ci.cino, ci.qty, p.pname, p.price, p.pno, pi.fileName ) " +
            "from " +
            "CartItem ci inner join Cart mc on ci.cart = mc " +
            "left join Product p on ci.product = p " +
            "left join p.imageList pi " +
            "where " +
            "pi.ord = 0 and mc.cno = :cno " +
            "order by ci.cino desc ")
    List<CartItemListDTO> getItemsOfCartDTOByCart(@Param("cno") Long cno);
}
