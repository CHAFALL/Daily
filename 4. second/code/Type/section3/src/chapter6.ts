/**
 * 타입 단언 (이거 중요!!!(me))
 * 타입 단언은 실제로 값을 그 타입으로 바꾸는 것은 아님.
 * TS의 눈을 잠시 가리는 느낌
 * 조금 위험한 문법임... (맨 밑의 !만 봐도 알 수 있음.)
 * 그래서 조심해서 확실할 때만 사용하기를 권장!!
 */

type Person = {
  name: string;
  age: number;
};

// 안되는 예시

// let person2: Person = {};
// person2.name = "chafa";
// person2.age = 27;

// let person3 = {};
// person3.name = "chafa";
// person3.age = 27;

// 나중에 값을 넣고 싶을 때 이용!!
let person = {} as Person;
person.name = "chafa";
person.age = 27;

type Dog = {
  name: string;
  color: string;
};

// 이렇게도 가능.

let dog = {
  name: "돌돌이",
  color: "brown",
  breed: "진도",
} as Dog;

/**
 * 타입 단언의 규칙
 * 값 as 단언 <- 단언식
 * A as B
 * A 가 B의 슈퍼타입이거나
 * A 가 B의 서브타입이어야 한다.
 */

let num1 = 10 as never;
let num2 = 10 as unknown;

// 두 형식끼리 겹치는 것이 없다.
// let num3 = 10 as string;

// 이렇게 다중 단언을 할 수 있긴 하지만 이렇게 쓰는 것 비추!!!
// 정말 필요할 시에만 이렇게 할 것!!
let num3 = 10 as unknown as string;

/**
 * const 단언
 */

let num4 = 10 as const; // 이러면 리터럴 타입으로 추론함.

// 이럴때 쓰임 (커서 올려보면 readonly로 추정되는 것을 알 수 있다.) -> 이렇게 하면 앞에마다 readonly를 일일이 붙여줄 필요가 없음
let cat = {
  name: "야옹이",
  color: "yellow",
} as const;

// 이게 막히게 됨.
// cat.name = ''

/**
 * Non Null 단언 -> 어떤 값이 null이거나 undefined 값이 아니라고 알려주는 역할. (!) <- 무조건 값이 있어!!
 */

type Post = {
  title: string;
  author?: string;
};

let post: Post = {
  title: "게시글1",
  author: "chafa",
};

const len: number = post.author!.length;
