package jpabook.jpashop.domain;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import static jakarta.persistence.FetchType.*;

@Entity
@Getter
@Setter
public class Delivery {
    @Id
    @GeneratedValue
    @Column(name = "delivery_id")
    private Long id;

    @OneToOne(mappedBy = "delivery", fetch = LAZY)
    private Order order;

    @Embedded
    private Address address;
    
    // ORDINAL(디폴트): 컬럼이 1, 2, 3, 4 숫자로 들어감
    // 그래서 중간에 다른 값이 들어간다고 사고!!!
    // 그래서 STRING으로!
    @Enumerated(EnumType.STRING)
    private DeliveryStatus status; //READY, COMP (배송 준비, 배송)
}
