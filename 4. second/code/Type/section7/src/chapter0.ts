/**
 * 제네릭
 * 일반적인 포괄적인.
 * 모든 타입에 두루두루 범용적으로 사용할 수 있는 함수 (함수계의 종합 병원)
 * 상황에 따라서 다른 타입을 담을 수 있다!
 */

// 제네릭 함수
// 여기서 T는 타입 변수이다.
function func<T>(value: T): T {
  return value;
}

let num = func(10);
// num.toUpperCase();

// 사용을 하려면 이렇게 type을 좁혀서 사용을 해야됨. -> (제네릭을 안 쓰고 unknown 타입으로 정의해서 이용할 때(불편)).
if (typeof num === "number") {
  num.toFixed();
}

let bool = func(true);

let str = func("string");

// 이렇게 하면 number[]타입으로 추론이 됨
let arr = func([1, 2, 3]);

// 근데 number[]타입으로 추론이 되도록 두지 말고 이 타입 변수 T에 튜플 타입으로 추론되게 하고 싶다면?
// 방식 1
let arr2 = func([1, 2, 3] as [number, number, number]);
// 방식 2
let arr3 = func<[number, number, number]>([1, 2, 3]);
