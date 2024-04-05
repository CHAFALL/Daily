/**
 * infer
 * inference -> 추론하다
 * 조건부 타입 내에서 특정 타입만 딱 추론해 올 수 있는...
 */

type FuncA = () => string;

type FuncB = () => number;

// infer R => 이 조건식을 참으로 만드는 타입을 추론
type ReturnType<T> = T extends () => infer R ? R : never;

type A = ReturnType<FuncA>;

type B = ReturnType<FuncB>;

// 얘는 never가 나옴
// T에 number가 들어가는데 () => infer R이 true가 되도록 하는 것이 없으므로
type C = ReturnType<number>;

/**
 * 예제
 */
type PromiseUnpack<T> = T extends Promise<infer R> ?  R : never;
// 1. T는 프로미스 타입이어야 한다.
// 2. 프로미스 타입의 결과값 타입을 반환해야 한다.


type PromiseA = PromiseUnpack<Promise<number>>;
// number

type PromiseB = PromiseUnpack<Promise<string>>;
// string
