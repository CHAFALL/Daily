package jpabook.jpashop.service;

import jpabook.jpashop.domain.Member;
import jpabook.jpashop.repository.MemberRepository;
import lombok.AllArgsConstructor;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
// JPA의 어떤 모든 데이터, 로직 변경들은 가급적 Transaction 안에서 다 실행이 되어야 됨
@Transactional(readOnly = true)
//@AllArgsConstructor
// 위랑 비슷한 것인데 final이 붙어있는 필드로만 만들어줌
@RequiredArgsConstructor
// 기본은 readOnly = false
// readOnly = true 필요한 곳(읽기만 하는 곳)에 써주면 성능 up
public class MemberService {

    // Autowired 하면 스프링이 스프링 빈에 등록되어있는
    // memberRepository를 injection 해줌
//    @Autowired
    // 변경할 일이 없으면 final 넣는 것을 권장
    private final MemberRepository memberRepository;
    // 위와 같이 안하고 아래와 같이 해주는 이유??
    // 위와 같이 하면 변경이 불가하므로
//    @Autowired // 이거 생략가능한 이유 -> 생성자 하나면 알아서 넣어주므로
//    또 하나 좋은 거 @AllArgsConstructor하면 아래 것 해줌
//    public MemberService(MemberRepository memberRepository) {
//        this.memberRepository = memberRepository;
//    }

    /**
     * 회원 가입
     */
    // 얘만 읽기가 필요하므로 전체에 readOnly = true 해주고 얘만 이렇게
    @Transactional
    public Long join(Member member) {
        validateDuplicateMember(member); //중복 회원 검증
        memberRepository.save(member);
        return member.getId();
    }

    private void validateDuplicateMember(Member member) {
        List<Member> findMembers = memberRepository.findByname(member.getName());
        //EXCEPTION
        if (!findMembers.isEmpty()) {
            throw new IllegalStateException("이미 존재하는 회원입니다.");
        }
    }

    // 회원 전체 조회
    public List<Member> findMembers() {
        return memberRepository.findAll();
    }

    public Member findOne(Long memberId) {
        return memberRepository.findOne(memberId);
    }
}
