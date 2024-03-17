package com.d212.taiso.repository;

import com.d212.taiso.domain.Member;
import org.springframework.data.jpa.repository.EntityGraph;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

// 이메일 이니깐 String 으로
public interface MemberRepository extends JpaRepository<Member, String> {

    // 우리 같은 경우 조회를 할 때 사용자의 이메일을 가지고 조회를 하니까 findByEmail 같은 것으로 만들어 써도 되지만,
    // 조인을 해서 데이터를 한번에 가져오고 싶다. -> 엘리먼트 컬렉션을 쓸 때 엔티티 그래프로 해결.

    // Role도 가져오려고 하므로 @EntityGraph를 이용
    @EntityGraph(attributePaths = {"memberRoleList"})
    @Query("select m from Member m where m.email = :email")
    Member getWithRoles(@Param("email") String email);
}
