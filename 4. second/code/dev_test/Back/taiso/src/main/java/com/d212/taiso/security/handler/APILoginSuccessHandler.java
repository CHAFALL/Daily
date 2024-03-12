package com.d212.taiso.security.handler;

import com.d212.taiso.dto.MemberDTO;
import com.d212.taiso.util.JWTUtil;
import com.google.gson.Gson;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import lombok.extern.log4j.Log4j2;
import org.springframework.security.core.Authentication;
import org.springframework.security.web.authentication.AuthenticationSuccessHandler;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Map;

// 인증에 성공했을 때 어떻게 할꺼야?

@Log4j2
public class APILoginSuccessHandler implements AuthenticationSuccessHandler {
    @Override
    public void onAuthenticationSuccess(HttpServletRequest request, HttpServletResponse response, Authentication authentication) throws IOException, ServletException {

        log.info("-------------------");
        log.info("authentication");
        log.info("-------------------");

        // 여기까지 왔다는 것은 인증 성공을 했다는 것
        // MemberDTO를 꺼내와가지고 JWT
        // MemberDTO는 인증한 것에서부터 getPrincipal로 부터 끄집어냄
        MemberDTO memberDTO = (MemberDTO) authentication.getPrincipal();

        // 우리가 만들어야 될 데이터
        // 이걸 왜 이렇게 따로 끄집어냈냐면 이따가 추가적인 정보(엑세스 토큰과 리프레스 토큰)를 넣을 것이므로
        Map<String, Object> claims = memberDTO.getClaims();

        // 엑세스 토큰 만들기
        String accessToken = JWTUtil.generateToken(claims, 10);
        String refreshToken = JWTUtil.generateToken(claims, 60 * 24);

        claims.put("accessToken", accessToken);
        claims.put("refreshToken", refreshToken);

        // 이렇게 claims에 정보를 넣고난 뒤에 json문자열로 만들 것이다.
        Gson gson = new Gson();

        String jsonStr = gson.toJson(claims);

        // 여기서부턴 기본적인 웹 프로그래밍이 튀어나옴(Java.io 문법)
        response.setContentType("application/json; charset=UTF-8");

        // PrintWriter는 Java에서 텍스트 데이터를 파일이나 다른 출력 대상에 쉽게 출력할 수 있도록 도와주는 클래스입니다.

        PrintWriter printWriter = response.getWriter();
        printWriter.println(jsonStr);
        printWriter.close();
    }

    // 어? 우리가 JWT 인증하면 나중에 어쨋든 토큰이라는 것만 있으면 되는 것이 아닌가?
    // 맞긴해. 문제는 로그인을 리액트 쪽에서 호출을 해서 가져가면 그러면 리액트 쪽에서도 무엇을 해야 되냐면,
    // 이 사용자에 대한 정보를 가져다가 화면에 출력하거나 이런 짓을 해야됨.
    // 그런데 암호화된 문자열만 있으면 그걸 알아보기가 힘들잖아. 그거 때문에 추가함.
    // 그래서 로그인을 하면 제이슨 문자를 주는데, 근데 여기에다가 추가적인 정보도 주려고 하는 것이다.
    // 그게 액세스 토튼과 리프레시 토큰이 되는 것이다.
}
