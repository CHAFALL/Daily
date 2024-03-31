/**
 * 함수 타입 표현식
 */

type Operation = (a: number, b: number) => number;

const add: (a: number, b: number) => number = (a, b) => a + b;
const sub: Operation = (a, b) => a - b;
const multiply: Operation = (a, b) => a * b;
const divide: Operation = (a, b) => a / b;

/**
 * 호출 시그니처
 * (콜 시그니처)
 */

// 이렇게 호출 시그니처를 이용할 때는 이런 식으로 객체에 property를 추가할 수 있다. (참고.)
type Operation2 = {
  (a: number, b: number): number;
  name: string; // 이 부분
};

const add2: Operation2 = (a, b) => a + b;
const sub2: Operation2 = (a, b) => a - b;
const multiply2: Operation2 = (a, b) => a * b;
const divide2: Operation2 = (a, b) => a / b;
