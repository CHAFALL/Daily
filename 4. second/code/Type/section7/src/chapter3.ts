/**
 * 제네릭 인터페이스
 */

interface KeyPair<K, V> {
  key: K;
  value: V;
}

// 제네릭 인터페이스는 제네릭 함수와는 달리 타입으로 정의할 때 반드시 타입 변수에 타입을 직접 할당해줘야 된다.
let keyPair: KeyPair<string, number> = {
  key: "key",
  value: 0,
};

let keyPair2: KeyPair<boolean, string[]> = {
  key: true,
  value: ["1"],
};

/**
 * 인덱스 시그니처
 */

interface NumberMap {
  [key: string]: number;
}

let numberMap1: NumberMap = {
  key: -1231,
  key2: 123123,
};

interface Map<V> {
  [key: string]: V;
}

let stringMap: Map<string> = {
  key: "value",
};

let booleanMap: Map<boolean> = {
  key: true,
};

/**
 * 제네릭 타입 별칭
 */

type Map2<V> = {
  [key: string]: V;
};

let stringMap2: Map2<string> = {
  key: "hello",
};

/**
 * 제네릭 인터페이스의 활용 예시
 * -> 유저 관리 프로그램
 * -> 유저 구분: 학생 유저 / 개발자 유저
 */

interface Student {
  type: "student";
  school: string;
}

interface Developer {
  type: "developer";
  skill: string;
}


interface User<T> {
  name: string;
  profile: T;
}

function goToSchool(user: User<Student>) {
  
  const school = user.profile.school;
  console.log(`${school}로 등교 완료`);
}

const developerUser: User<Developer> = {
  name: "chafa",
  profile: {
    type: "developer",
    skill: "TypeScript",
  },
};

const studentUser: User<Student> = {
  name: "홍길동",
  profile: {
    type: "student",
    school: "서울대",
  },
};




// interface User {
//   name: string;
//   profile: Student|Developer;
// }

// 매번 이렇게 타입 좁히기를 하던 것을 제네릭을 이용하면 훨씩 간편하게 만들 수 있다!!
// function goToSchool(user: User) {
  //   if (user.profile.type !== "student") {
    //     console.log("잘 못 오셨습니다.");
    //     return;
    //   }
    
    //   const school = user.profile.school;
    //   console.log(`${school}로 등교 완료`);
    // }
    
    
    // function goToSchool(user: User) {
      //   if (user.profile.type !== "student") {
        //     console.log("잘 못 오셨습니다.");
//     return;
//   }

//   const school = user.profile.school;
//   console.log(`${school}로 등교 완료`);
// }

// const developerUser: User = {
//   name: "chafa",
//   profile: {
//     type: "developer",
//     skill: "TypeScript",
//   },
// };

// const studentUser: User = {
//   name: "홍길동",
//   profile: {
//     type: "student",
//     school: "서울대",
//   },
// };


