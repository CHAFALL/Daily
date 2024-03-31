/**
 * 선언 합침
 * -> 간단한 프로그래밍을 할 때는 잘 사용되지 않고
 * -> TS의 모듈 그러니까 라이브러리의 타입 정의가 좀 부실한 경우에 우리가 직접 이 타입을 좀 더 추가해주고 정확하게 만들어주는 일종의 모듈 보강이라는 작업을 할 때 사용을 함
 */

// 동일한 이름의 인터페이스들은 다 합쳐짐.

interface Person {
  name: string;
}

interface Person {
  // 동일한 property를 중복 정의하는데 타입을 다르게 하면 충돌이 발생해서 허용 x -> 서브 타입도 불가
  // name: "hello"
  // name: number;
  age: number;
}

const person: Person = {
  name: "",
  age: 27,
};

/**
 * 모듈 보강
 * -> 이번 예시가 완벽하진 x
 * -> 보통 라이브러리의 코드들은 node_modules 안에 있기 때문에 여기 안에 있는 것을 불러와서 모듈을 보강하고 이런 작업이 필요
 */

// 라이브러리
interface Lib {
  a: number;
  b: number;
}

// c가 추가로 필요할 시
interface Lib {
  c: string;
}

const lib: Lib = {
  a: 1,
  b: 2,
  c: "hello",
};
