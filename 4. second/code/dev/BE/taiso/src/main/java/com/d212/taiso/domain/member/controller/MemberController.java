package com.d212.taiso.domain.member.controller;
/**
 * Created by 전근렬 on 2024-03-21
 */

import com.d212.taiso.domain.member.dto.MemberJoinReq;
import com.d212.taiso.domain.member.service.MemberService;
import com.d212.taiso.global.result.ResultCode;
import com.d212.taiso.global.result.ResultResponse;
import lombok.RequiredArgsConstructor;
import lombok.extern.log4j.Log4j2;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@Log4j2
@RestController
@RequestMapping("/members")
@RequiredArgsConstructor
public class MemberController {

    private final MemberService memberService;

    @GetMapping("/ck/{email}")
    public ResponseEntity<ResultResponse> checkEmail(@PathVariable("email") String email) {
        try {
            boolean check = memberService.checkEmail(email);

            if (check == true) { //중복된 이메일이 존재하는 경우
                return ResponseEntity.ok(ResultResponse.of(ResultCode.EMAIL_DO_EXIST, false));
            }
            return ResponseEntity.ok(ResultResponse.of(ResultCode.EMAIL_DO_NOT_EXIST, true));

        } catch (Exception e) {
            log.debug("이메일 중복체크 에러 발생: {}", e);
            throw new RuntimeException(e);
        }
    }

    @PostMapping("/join")
    public ResponseEntity<ResultResponse> memberJoin(@RequestBody MemberJoinReq memberJoinReq) {
        memberService.memberJoin(memberJoinReq);
        return ResponseEntity.ok(ResultResponse.of(ResultCode.JOIN_SUCCESS, true));
    }


    @DeleteMapping("/")
    public ResponseEntity<ResultResponse> memberDelete() {
        memberService.memberDelete();
        return ResponseEntity.ok(ResultResponse.of(ResultCode.MEMBER_DELETE_SUCCESS, true));
    }
}