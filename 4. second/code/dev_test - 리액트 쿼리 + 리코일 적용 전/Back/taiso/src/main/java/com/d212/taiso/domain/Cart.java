package com.d212.taiso.domain;

import jakarta.persistence.*;
import lombok.*;

// 왜 굳이 장바구니를 따로 만들었는가??
// 한국인들은 항상 사람이 주어 -> 그래서 항상 DB 같은 설계를 봐도
// 항상 회원이 중심으로 뭐든지 설계가 된다.
// 그러다보면 시스템 분리를 할 때 회원이 떨어질 수 없는 문제가 발생할 수도 있다.
// 그래서 아예 장바구니는 장바구니대로 따로 설계를 하는게 좋겠다고 판단함.
@Entity
@Builder
@AllArgsConstructor
@NoArgsConstructor
@Getter
@ToString(exclude = "owner")
@Table(
        name = "tbl_cart",
        // 이메일(사용자의 id)를 기준으로 해서 장바구니를 읽어 와야 되므로
        // 이렇게 구성
        indexes = {@Index(name = "idx_cart_email", columnList = "member_owner")}
)
public class Cart {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long cno;

    @OneToOne
    // OneToOne은 JoinColumn 안 써도 되는 느낌인가???
    // 이렇게 컬럼명을 지정한 이유는 인덱스를 쓰고 싶어서 란다.
    @JoinColumn(name = "member_owner")
    private Member owner;
}
