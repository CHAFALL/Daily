package jpabook.jpashop.domain;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

@Entity
@Table(name = "orders")
@Getter @Setter
public class Order {
    @Id @GeneratedValue
    @Column(name = "order_id")
    private Long id;

    // 주문이 다, 회원이 1
    // 연관 관계 주인을 정해줌(혼란 방지)
    @ManyToOne
    // 매핑을 member_id로 (fk키 = member_id)
    @JoinColumn(name = "member_id")
    private Member member;

    @OneToMany(mappedBy = "order")
    private List<OrderItem> orderItems = new ArrayList<>();

    @OneToOne
    @JoinColumn(name="delivery_id")
    // 1대1은 많이 접근하는 곳에다가 함(이번에는 order가 많음)
    private Delivery delivery;

    private LocalDateTime orderDate; // 주문시간
    @Enumerated(EnumType.STRING)
    private OrderStatus status; // 주문 상태 [ORDER, CANCEL]
}
