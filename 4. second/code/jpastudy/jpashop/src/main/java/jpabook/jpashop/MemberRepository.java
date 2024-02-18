package jpabook.jpashop;

import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;
import org.springframework.stereotype.Repository;

@Repository
public class MemberRepository {
    // 스프링 부트를 쓰기 때문에 스프링 컨테이너 위에서 다 동작을 하는데
    // @PersistenceContext를 써주면 엔티티 매니저를 주입해줌
    @PersistenceContext
    EntityManager em;

    public Long save(Member member) {
        // JPA는 전달된 엔티티를 영속성 컨텍스트에 저장하게 됩니다.
        em.persist(member);
        return member.getId();
    }
    public Member find(Long id) {
        return em.find(Member.class, id);
    }
}
