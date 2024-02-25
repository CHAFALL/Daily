package hellojpa;

import jakarta.persistence.*;

import java.util.List;

public class JpaMain {

    public static void main(String[] args) {

        EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello");

        EntityManager em = emf.createEntityManager();

        EntityTransaction tx = em.getTransaction();
        tx.begin();

        //code
        try{



//            jpa에서 지원하지 않는 좀 더 deep한 것을 조회해야 한다면? JPQL 이용 (페이징도 이걸로 함)
//            List<Member> result = em.createQuery("select m from Member as m", Member.class)
//                    .setFirstResult(5)
//                    .setMaxResults(8) // 5번부터 8개 가져와!!
//                    .getResultList();
//
//            for (Member member : result) {
//                System.out.println("member.name = " + member.getName());
//            }

            // 비영속(객체를 생성한 상태)
//            Member member = new Member(100L, "A");
//            member.setId(120L);
//            member.setName("HelloJPA");

            // 영속(객체를 저장한 상태)
//            em.persist(member); // 이때 DB에 저장 되지는 않음.

            // 조회 후 수정
//            Member findMember = em.find(Member.class, 100L);
//            findMember.setName("HelloJPA");

//            수정 시에 em.persist(findMember)로 저장할 필요 x
//            왜냐하면 jpa를 통해서 엔티티를 가져오면(em.find) jpa에서 관리를 해주게 됨
//            그리고 jpa가 변경 여부를 transaction commit하는 순간에 체크를 함

            tx.commit();

        } catch (Exception e){
            tx.rollback();
        } finally {
            em.close();
        }

        emf.close();
    }
}
