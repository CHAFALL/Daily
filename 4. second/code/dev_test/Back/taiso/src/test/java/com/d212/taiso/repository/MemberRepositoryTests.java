package com.d212.taiso.repository;

import com.d212.taiso.domain.Member;
import com.d212.taiso.domain.MemberRole;
import lombok.extern.log4j.Log4j2;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.security.crypto.password.PasswordEncoder;

@SpringBootTest
@Log4j2

// 주의할 점: password를 인코딩 해서 넣어줘야 됨(안 그러면 나중에 가져왔을 때 문제가 됨. 인코더를 이용할 때.)
public class MemberRepositoryTests {
    @Autowired
    private MemberRepository memberRepository;

    // 구글 쪽에서 만들어 준 것인데, id와 password 갑을 갖다가 비대칭 암호가 됨
    // 그래서 사용자가 똑같은 패스워드를 쓰지만 들어가는 생성되는 문자의 값이 다 다름
    // 그래서 서버 운영쪽에서도 모름. 사용자만 password를 암.
    @Autowired
    private PasswordEncoder passwordEncoder;

    @Test
    public void testInsertMember() {

        for (int i = 0; i < 10; i++) {
            Member member = Member.builder()
                    .email("user" + i + "@aaa.com")
                    .pw(passwordEncoder.encode("1111"))
                    .nickname("USER"+i)
                    .build();

            member.addRole(MemberRole.USER);

            if (i >= 5) {
                member.addRole(MemberRole.MANAGER);
            }

            if (i >= 8) {
                member.addRole(MemberRole.ADMIN);
            }

            memberRepository.save(member);
        }// end for
    }

    @Test
    public void testRead() {
        String email = "user9@aaa.com";
        Member member = memberRepository.getWithRoles(email);
        log.info("-----------------");
        log.info(member);
        log.info(member.getMemberRoleList());
    }


}
