package jpabook.jpashop;

import jakarta.transaction.Transactional;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.annotation.Rollback;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
class MemberRepositoryTest {
    @Autowired
    MemberRepository memberRepository;

    @Test
    // 이거 없으면 에러남...
    // 엔티티 매니저를 통한 모든 데이터 변경은 항상 트랜잭션 안에서 이루어져야 한다.
    @Transactional
    // 트랜잭션이 테스트 케이스 안에 있으면 테스트가 끝난 다음에 바로 롤백 해버림..(DB에 없는 이유.)
    // 이를 막고 싶다면 아래를 넣어주면 됨
    @Rollback(value = false)
    public void testMember() throws Exception {
        //given
        Member member = new Member();
        member.setUsername("memberA");

        //when
        Long savedId = memberRepository.save(member);
        Member findMember = memberRepository.find(savedId);

        //then
        Assertions.assertThat(findMember.getId()).isEqualTo(member.getId());
        Assertions.assertThat(findMember.getUsername()).isEqualTo(member.getUsername());
        // 같은 영속성 컨텍스트 안에서는 id 값이 같으면 같은 엔티티로 식별
        Assertions.assertThat(findMember).isEqualTo(member);
        System.out.println("findMember == member " + (findMember == member));
    }



}