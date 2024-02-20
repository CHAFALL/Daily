package jpabook.jpashop.repository;

import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;
import jpabook.jpashop.domain.Member;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
@RequiredArgsConstructor
public class MemberRepository {
    //    @PersistenceContext 얘를 죽이고 아래로 가능(생성자 해주고)
//    @Autowired 이거도 죽이고
    private final EntityManager em;
// @RequiredArgsConstructor 이거 쓰니깐 아래도 죽이고
//    public MemberRepository(EntityManager em) {
//        this.em = em;
//    }

    public void save(Member member) {
        em.persist(member); //이렇게 하면, 영속적 컨텍스트에
        // 멤버 객체를 올림.
        // 그때 영속적 컨텍스트는 키랑 value가 있는데
        // 키는 id값임(그래서 id값이 생성되어 있는 것이 보장이 됨)
        // DB에 들어가기 전에 해줌. 그래서 service에서 member.getId()로 리턴이 가능한 이유??
    }

    public Member findOne(Long id) {
        return em.find(Member.class, id);
    }

    public List<Member> findAll(){
        return em.createQuery("select m from Member m", Member.class)
                .getResultList();
    }

    public List<Member> findByname(String name){
        // 파라미터 바인딩(:xx)
        return em.createQuery("select m from Member m where m.name = :name", Member.class)
                .setParameter("name", name)
                .getResultList();
    }
}
