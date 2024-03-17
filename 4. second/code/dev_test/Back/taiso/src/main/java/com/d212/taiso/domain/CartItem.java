package com.d212.taiso.domain;

import jakarta.persistence.*;
import lombok.*;

// 이걸 엘리먼트 컬렉션으로 만들 수 있다.
// 하지만 앞에서 이미 다뤄봤어서 따로 한번 분리 해보자는 것임
// 그리고 ManyToMany(이런건 안 씀)가 아닌 ManyToOne OneToMany로 하는 것을 보여주려고
@Entity
@Builder
@AllArgsConstructor
@NoArgsConstructor
@Getter
@ToString(exclude = {"cart", "product"})
// 테이블에 인덱스를 잡아둘 생각
// 여기가 중요하다는데 이게 뭐고

// 조회할 때 cino(pk)로 할 수도 있겠지만 조회를 할 때 어느 카트에 들어있는
// 장바구니 아이템들을 조회할 것이므로 카트 번호를 더 많이 쓸거라 판단해서
// 이걸로 조회하는 인덱스가 하나 있으면 좋겠다고 판단

// 내가 어떤 카트(장바구니) 안에 있는 상품의 수량을 변경해야 되잖아
// 그래서 cino로 조회를 하는 것이 아니라 카트의 번호랑 상품 번호로 찾을 일이 많다.
// 그래서 걔도 인덱스로 빼둠.
@Table(name = "tbl_cart_item", indexes = {
        @Index(columnList = "cart_cno", name = "idx_cartitem_cart"),
        @Index(columnList = "product_pno, cart_cno", name="idx_cartitem_pno_cart")
})

public class CartItem {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long cino;

    @ManyToOne
    @JoinColumn(name = "product_pno")
    private Product product;

    // Cascade는??
    @ManyToOne
    @JoinColumn(name = "cart_cno")
    private Cart cart;

    private int qty;

    public void changeQty(int qty) {
        this.qty = qty;
    }
}

