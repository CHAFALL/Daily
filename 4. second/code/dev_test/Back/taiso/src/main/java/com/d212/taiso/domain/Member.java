package com.d212.taiso.domain;

import jakarta.persistence.ElementCollection;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.Id;
import lombok.*;

import java.util.ArrayList;
import java.util.List;

// 보통 db할 때 user라는 이름을 많이 써서, 데이터 베이스의 키워드로 사용될 가능성이 높아 member로 하겠다

@Entity
@Builder
@AllArgsConstructor
@NoArgsConstructor
@Getter
@ToString(exclude = "memberRoleList")
public class Member {

    @Id
    private String email;

    private String pw;

    private String nickname;

    private boolean social;

    @ElementCollection(fetch = FetchType.LAZY)
    // 처음부터 초기화를 시켜야 되니까 이걸 사용해서 빌더로 만들어 주더라도 처음부터 사용할 수 있도록.
    @Builder.Default
    private List<MemberRole> memberRoleList = new ArrayList<>();

    public void addRole(MemberRole memberRole){ memberRoleList.add(memberRole); }
    public void clearRole(){ memberRoleList.clear(); }

    public void changeNickname(String nickname) { this.nickname = nickname; }
    public void changePw(String pw){ this.pw = pw; }
    public void changeSocial(boolean social) { this.social = social; }


}
