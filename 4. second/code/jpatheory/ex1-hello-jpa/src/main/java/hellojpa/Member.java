package hellojpa;

import jakarta.persistence.*;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.Date;

@Entity
// 근데 테이블 매핑 전략은 잘 이용 x
// 테이블마다 시퀀스를 따로 관리하고 싶을 때 이용
@SequenceGenerator(
        name = "MEMBER_SEQ_GENERATOR",
        sequenceName = "MEMBER_SEQ", //매핑할 데이터베이스 시퀀스 이름
        initialValue = 1, allocationSize = 50
)
//@Table(name = "MBR")
public class Member {

    @Id
    // 타입에 IDENTITY, SEQUENCE, TABLE, AUTO 이 있다
    // IDENTITY는 DB에 의존하므로 DB가 알아서 만들어주고 난 뒤에만 id값을 알 수 있는 문제점이 있다.
    // 그래서 JPA에서도 얘만 예외적으로 persist할 때 바로 DB에 insert 쿼리를 날려줌(기존은 commit 할 때 날림.)
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "MEMBER_SEQ_GENERATOR")
    private Long id; // 그냥 Long 쓰란다.

    // 객체에는 username이라고 쓰고 싶은데 DB에는 name이라고 써야될 때.
    @Column(name = "name", length = 10, nullable = false)
//    @Column(columnDefinition = "varchar(100) default ‘EMPTY'")
    private String username;


    public Member() {
    }



    //    private Integer age;
//
//    // enum 쓸때는 반드시 STRING으로!!!!!! default는 ORDINAL임
//    @Enumerated(EnumType.STRING)
//    private RoleType roleType;
//
//    // 타입으로 날짜(DATE), 시간(TIME), 날짜와 시간(TIMESTAMP)이 있다.
//    @Temporal(TemporalType.TIMESTAMP)
//    private Date createdDate;
//    @Temporal(TemporalType.TIMESTAMP)
//    private Date lastModifiedDate;
//
//    // 캘린더 시에 쓰임(년, 월만 있음)
//    private LocalDate testLocalDate;
//    // (년, 월, 일 모두 포함)
//    private LocalDateTime testLocalDateTime;
//
//    // DB에 varchar를 넘어서는 큰 뭔가를 넣고 싶으면 @Lob을 이용.
//    // 참고: 매핑하는 필드 타입이 문자면 CLOB 매핑, 나머지는 BLOB으로 매핑
//    @Lob
//    private String description;
//
//    // 얘는 DB에 매핑 안하고 싶어!
//    @Transient
//    private int temp;





}
