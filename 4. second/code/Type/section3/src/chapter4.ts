/**
 * 대수 타입
 * -> 여러개의 타입을 합성해서 새롭게 만들어낸 타입
 * -> 합집합 타입과 교집합 타입이 존재합니다.
 */

/**
 * 1. 합집합 - Union 타입
 */

let a: string | number | boolean;

a = 1;
a = "hello";
a = true;

let arr: (number | string | boolean)[] = [1, "hello", true];

type Dog = {
  name: string;
  color: string;
};

type Person = {
  name: string;
  language: string;
};

type Union1 = Dog | Person;

let union1: Union1 = {
  name: "",
  color: "",
};

let union2: Union1 = {
  name: "",
  language: "",
};

// 합집합이다!! -> 두 객체 모두에 포함이 됨.
let union3: Union1 = {
  name: "",
  color: "",
  language: "",
};

// 합집합이다!! (최소 조건 중 하나는 반드시 충족해야 됨.)
// 포함될 수 있는 객체가 없네.....

// let union4: Union1 = {
//   name: "",
// };

/**
 * 2. 교집합 타입 - Intersection 타입
 */

// number과 string의 교집합은 없으므로 never 타입으로 인지
let variable: number & string;

type Dog2 = {
  name: string;
  color: string;
};

type Person2 = {
  name: string;
  language: string;
};

type Intersection = Dog2 & Person2;

// 모든 것이 다 들어가 있어야 된다. (dog2 객체이면서 person2 객체이기도 해야 된다.)
let intersection1: Intersection = {
  name: "",
  color: "",
  language: "",
};
