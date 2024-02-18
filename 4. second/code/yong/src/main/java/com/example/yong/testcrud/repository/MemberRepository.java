package com.example.yong.testcrud.repository;

import com.example.yong.testcrud.entity.Member;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.Optional;


public interface MemberRepository extends JpaRepository<Member, Long> {

   List<Member> findAllByNameOrderByBirthDesc(String name);

   Optional<Member> findByName(String name);
}
