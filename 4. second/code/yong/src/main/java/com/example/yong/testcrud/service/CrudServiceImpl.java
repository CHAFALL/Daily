package com.example.yong.testcrud.service;

import com.example.yong.testcrud.entity.Member;

import com.example.yong.testcrud.repository.MemberRepository;
import jakarta.transaction.Status;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.apache.catalina.connector.Response;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import javax.swing.text.html.Option;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;


@Service
@Transactional(readOnly = true)
@Slf4j
@RequiredArgsConstructor
public class CrudServiceImpl implements CrudService{

    private final MemberRepository memberRepository;

    @Override
    @Transactional(readOnly = false)
    public void SaveMember(String name) {
        Member member = Member.builder()
                .name(name)
                .birth(LocalDateTime.now())
                .build();
        memberRepository.save(member);
        member = memberRepository.findByName(name).orElseThrow(() -> new RuntimeException("이름을 찾을 수 없다."));

    }

    @Override
    @Transactional(readOnly = false)
    public Member GetMember(String name) {
        Member member = memberRepository.findByName(name).orElseThrow(() -> new RuntimeException("이름을 찾을 수 없다."));
        return member;
    }

    @Override
    @Transactional
    public void DeleteMemeber(String name) {
        memberRepository.delete(
                memberRepository.findByName(name)
                        .orElseThrow(() -> new RuntimeException("멤버가 없어...")));
    }

    @Override
    @Transactional
    public void UpdateMemeber(String name, String newName) {
        Member member = memberRepository.findByName(name).orElseThrow(() -> new RuntimeException("이름을 찾을 수 없다."));
        member.setName(newName);
    }
}
