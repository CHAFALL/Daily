package com.d212.taiso.security;

import com.d212.taiso.domain.Member;
import com.d212.taiso.dto.MemberDTO;
import com.d212.taiso.repository.MemberRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.log4j.Log4j2;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import java.util.stream.Collectors;


// 잘된 자바 코드들은 항상 리턴 타입이랑 파라미터 타입은 가능하면 인터페이스로 뺌.(나중에 변경이 용이 하도록), 늘 김영한이 하던거네.
// 현제 리턴 타입이 유저 Details 타입인데, 근데 얘를 구현한 클래스 중에 하나가 유저(유저는 클래스이다보니 생성자를 가질 수 있음.)
// 그냥 어지럽네.

// 로그인을 처리할 때 동작하는 애임.
@RequiredArgsConstructor
@Service
@Log4j2
public class CustomUserDetailsService implements UserDetailsService {

    // 여기서 유저네임은 우리에게 ID에 해당하는 값이다.
    // 즉, 우리는 이메일..
    // 리턴 타입을 보면 UserDetails임을 알 수 있다. -> 즉 우리에게는 이게 멤버 DTO가 됨을 알 수 있다.
    // 얘는 인터페이스 이고 유저라는 애(Member DTO 쪽에 USER라는 애를 extends 했음)는 클래스 느낌....

    private final MemberRepository memberRepository;
    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {

        log.info("--------------loadUserByUsername-------------------" + username);


        Member member = memberRepository.getWithRoles(username);

        // 이렇게 뽑아낸 Member 엔티티를 가지고 멤버DTO를 반환해줘야 됨

        if (member == null) {
            throw new UsernameNotFoundException("Not Found");
        }

        MemberDTO memberDTO = new MemberDTO(
                member.getEmail(),
                member.getPw(),
                member.getNickname(),
                member.isSocial(),
                // MemberRole이 숫자라서 문자열로 바꿔주는 작업을 해줌.
                member.getMemberRoleList().stream()
                        .map(memberRole -> memberRole.name()).collect(Collectors.toList()));

        log.info(memberDTO);
        log.info("---------여기까지 하면 로그인 인증까지는 성공한 것임---------");
        // 이제부터는 이걸 가지고 json 또는 jwt 라는 문자열로 만들어주는 작업을 할 것임.

        return memberDTO;
    }
}
