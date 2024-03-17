package com.d212.taiso.service;

import com.d212.taiso.domain.Member;
import com.d212.taiso.domain.MemberRole;
import com.d212.taiso.dto.MemberDTO;
import com.d212.taiso.dto.MemberModifyDTO;
import com.d212.taiso.repository.MemberRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.log4j.Log4j2;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.util.UriComponents;
import org.springframework.web.util.UriComponentsBuilder;

import java.util.LinkedHashMap;
import java.util.Optional;


@Service
// 우리가 이거를 API 서버에서 하는 진짜 이유 : 기존의 db 정보와 같이 활용을 하기 위해서이다.
// 그러므로 RequiredArgsConstructor를 이용해서 주입을 받아야 됨.
// 참고 : 카카오에서 닉네임은 unique 하다
@RequiredArgsConstructor
@Log4j2
public class MemberServiceImpl implements MemberService{

    private final MemberRepository memberRepository;

    private final PasswordEncoder passwordEncoder;

    @Override
    public MemberDTO getKakaoMember(String accessToken) {

        //accessToken을 이용해서 사용자의 정보 가져오기 (카카오 연동) 닉네임이 이메일 주소에 해당
        String nickname = getEmailFromKakaoAccessToken(accessToken);

        // 새로 데이터를 추가해주는데 pw가 문제가 됨.

        Optional<Member> result = memberRepository.findById(nickname);
        // 기존에 DB에 회원 정보가 있는 경우 - 현재 데이터 베이스와 처리
        if (result.isPresent()) {
            MemberDTO memberDTO = entityToDTO(result.get());


            log.info("existed....................." + memberDTO);

            return memberDTO;
            //return
        }
        //  없는 경우 - 현재 데이터 베이스와 처리
        Member socialMember = makeSocialMember(nickname);

        memberRepository.save(socialMember);

        MemberDTO memberDTO = entityToDTO(socialMember);

        return memberDTO;

    }

    @Override
    public void modifyMember(MemberModifyDTO memberModifyDTO) {
        Optional<Member> result = memberRepository.findById(memberModifyDTO.getEmail());

        Member member = result.orElseThrow();

        member.changeNickname(memberModifyDTO.getNickname());
        // 수정하면 False로 바꿔줘야 계속 수정 페이지로 가는 것을 막을 수 있음.
        member.changeSocial(false);
        member.changePw(passwordEncoder.encode(memberModifyDTO.getPw()));

        memberRepository.save(member);
    }

    private Member makeSocialMember(String email) {
        String tempPassword = makeTempPassword();

        log.info("tempPassword: " + tempPassword);

        Member member = Member.builder()
                .email(email)
                .pw(passwordEncoder.encode(tempPassword))
                .nickname("Social Member")
                .social(true) // 자기 닉네임 수정을 위해
                .build();

        member.addRole(MemberRole.USER);

        return member;
    }

    private String getEmailFromKakaoAccessToken(String accessToken) {
        String kakaoGetUserURL = "https://kapi.kakao.com/v2/user/me";

        RestTemplate restTemplate = new RestTemplate();

        HttpHeaders headers = new org.springframework.http.HttpHeaders();
        headers.add("Authorization", "Bearer " + accessToken);
        headers.add("Content-Type","application/x-www-form-urlencoded");


        HttpEntity<String> entity = new HttpEntity<>(headers);

        UriComponents uriBuilder = UriComponentsBuilder.fromHttpUrl(kakaoGetUserURL).build();

        ResponseEntity<LinkedHashMap> response =
                restTemplate.exchange(uriBuilder.toUri(), HttpMethod.GET, entity, LinkedHashMap.class);



        log.info("response-----------------");
        log.info(response);

        LinkedHashMap<String, LinkedHashMap> bodyMap = response.getBody();

        LinkedHashMap<String, String> kakaoAccount = bodyMap.get("properties");

        log.info("kakaoAccount: " + kakaoAccount);

        String nickname = kakaoAccount.get("nickname");

        log.info("nickname: " + nickname);

        return nickname;
    }

    private String makeTempPassword() {

        StringBuffer buffer = new StringBuffer();

        for(int i = 0;  i < 10; i++){
            buffer.append(  (char) ( (int)(Math.random()*55) + 65  ));
        }
        return buffer.toString();
    }

}
