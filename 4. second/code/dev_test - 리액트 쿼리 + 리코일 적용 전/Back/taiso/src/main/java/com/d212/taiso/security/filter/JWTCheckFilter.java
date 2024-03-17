package com.d212.taiso.security.filter;

// 필터 처리 3가지
// 1. 필터 생성
// 2. 이 필터를 어떤 경로에 들어왔을 때 동작하게 할 것인지 설정
// 3. 잘못 되면 어떻게 할 건지 (잘 되었을 때는 그냥 원래 하던거를 하면 됨.)


import com.d212.taiso.dto.MemberDTO;
import com.d212.taiso.util.JWTUtil;
import com.google.gson.Gson;
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import lombok.extern.log4j.Log4j2;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.filter.OncePerRequestFilter;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;
import java.util.Map;

// 스프링 웹 시큐리티는 굉장히 많은 여러 종류의 필터를 지원한다.
// 근데 모든 경우에 체크하겠끔 동작하는 필터가 있음(원스펄 리퀘스터 필터)

@Log4j2
public class JWTCheckFilter extends OncePerRequestFilter {

    // 어떤 경로로 들어오면 필터링을 해야된다. 그런데 어떤 경로는 안해도 된다.
    // (ex. 로그인 경로는 지금 로그인을 하는 것이기 때문에 JWT 토큰이 없다)
    // 이런 것들을 빼주는 역할을 하는 것이 shouldNotFilter
    @Override
    protected boolean shouldNotFilter(HttpServletRequest request) throws ServletException {

        // true == not checking

        String path = request.getRequestURI();

        log.info("check uri----------" + path);


        // 회원 쪽은 체크하지 마!
        if (path.startsWith("/api/member/")) {
            return true;
        }

        //이미지 조회 경로는 체크하지 않음
        if(path.startsWith("/api/products/view/")) {
            return true;
        }

        // 부정의 부정은 긍정, 즉 false == check
        return false;
    }


    @Override
    protected void doFilterInternal(HttpServletRequest request,
                                    HttpServletResponse response,
                                    FilterChain filterChain) throws ServletException, IOException {

        log.info("-------------------");
        log.info("-----------------JWTCheckFilter.................");
        log.info("-------------------");

        String authHeaderStr = request.getHeader("Authorization");

        //Bearer //7 JWT 문자열 , Bearer과 공백 포함해서 총 7자 뒤에 JWT 문자열이 오므로 잘라내는 작업 필요.

        try {
            //Bearer accestoken...
            String accessToken = authHeaderStr.substring(7);
            Map<String, Object> claims = JWTUtil.validateToken(accessToken);
            log.info("JWT claims: " + claims);



//            filterChain.doFilter(request, response);


            // 권한 관련-------------------------(참고)
            // 사용자의 토큰이 성공을 했다면 사용자에 대한 정보를 끄집어낼 수 o
            // 이 사용자의 정보를 가지고 멤버 DTO를 구성
            String email = (String) claims.get("email");
            String pw = (String) claims.get("pw");
            String nickname = (String) claims.get("nickname");
            Boolean social = (Boolean) claims.get("social");
            List<String> roleNames = (List<String>) claims.get("roleNames");

            MemberDTO memberDTO = new MemberDTO( email, pw, nickname, social.booleanValue(),
                    roleNames);
            log.info("-----------------------------------");
            log.info(memberDTO);
            log.info(memberDTO.getAuthorities());
            UsernamePasswordAuthenticationToken authenticationToken
                    = new UsernamePasswordAuthenticationToken(memberDTO,pw,memberDTO.getAuthorities());
            SecurityContextHolder.getContext().setAuthentication(authenticationToken);

            filterChain.doFilter(request, response);

            // 권한 관련 끝---------------


        }catch(Exception e){
            log.error("JWT Check Error..............");
            log.error(e.getMessage());

            // 문제가 생겼으면 이야기 해주는 부분.
            Gson gson = new Gson();
            String msg = gson.toJson(Map.of("error", "ERROR_ACCESS_TOKEN"));
            response.setContentType("application/json");
            PrintWriter printWriter = response.getWriter();
            printWriter.println(msg);
            printWriter.close();
        }


        // 성공하면 목적지로 (그냥 다음 것 타요.) (이거 뭔데???)
//        filterChain.doFilter(request, response);
    }
}
