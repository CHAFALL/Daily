package jpabook.jpashop.domain;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.util.ArrayList;
import java.util.List;

@Entity
@Getter @Setter
public class Member {
    @Id
    @GeneratedValue
    @Column(name = "member_id")
    private Long id;

    private String name;

    // 엔티티에 다른 값 객체를 포함할 때 사용됨
    // Member 엔티티에는 Address라는 값 객체가 포함됨
    @Embedded
    private Address address;

    // 멤버가 1, 주문이 다
    // 나는 매핑을 하는 애가 아니고,
    // member에 의해 mapping이 된 거일 뿐이야
    @OneToMany(mappedBy = "member")
    private List<Order> orders = new ArrayList<>();
}
