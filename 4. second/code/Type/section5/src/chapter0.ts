// interface는 객체 타입을 정의하는 데 특화된 문법
// 그렇기 때문에 인터페이스는 타입 별칭에서는 제공하지 않는 상속이나 합침 등의 객체 타입을 다루는 여러가지 특수한 기능들을 제공

/**
 * 인터페이스
 */

interface Person {
  readonly name: string;
  age?: number;

  // 이렇게도 가능
  sayHi(): void; // 호출 시그니처
  sayHi(a: number, b: number): void;
  // sayHi: () => void; // 함수 타입 표현식
}

// 메서드 오버로딩을 구현할 시에는 함수 타입 표현식으론 불가능하고 호출 시그니처로만 가능

// 인터페이스에서는 타입별칭처럼 유니온이나 인터섹션 타입은 만들 수 없음.... -> 그래서 이용하고 싶다면 타입별칭에다가 활용을 해서 달아주거나 type 주석에다가 활용하는 수 밖에 없음

type Type1 = number | string | Person;
type Type2 = number & string & Person;

const person: Person | number = {
  name: "chafa",
  sayHi: function () {
    console.log("Hi");
  },
};

// person.name = "홍길동";
person.sayHi();
person.sayHi(1, 2);
