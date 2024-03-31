/**
 * 함수 타입 호환성
 * 특정 함수 타입을 다른 함수 타입으로 취급해도 괜찮은가를 판단하는
 * 1. 반환값의 타입이 호환되는가
 * 2. 매개변수의 타입이 호환되는가
 */

// 기준1. 반환값이 호환되는가
type A = () => number;
type B = () => 10;

let a: A = () => 10;
let b: B = () => 10;

a = b;

// 불가 (다운캐스팅)
// b = a;

// 기준2. 매개변수가 호환되는가
// 2-1. 매개변수의 개수가 같을 때

type C = (value: number) => void;
type D = (value: 10) => void;

let c: C = (value) => {};
let d: D = (value) => {};

// 반환값 타입을 기준으로 호환성을 판단할 때와는 다르게 매개변수의 타입을 기준으로 호환성을 판단할 때는 반대로 업캐스팅이면 호환이 안된다고 함.
// 불가
// c = d;

d = c;

type Animal = {
  name: string;
};

type Dog = {
  name: string;
  color: string;
};

let animalFunc = (animal: Animal) => {
  console.log(animal.name);
};

let dogFunc = (dog: Dog) => {
  console.log(dog.name);
  console.log(dog.color);
};

// 불가 (업캐스팅이어서 안됨)
// animalFunc = dogFunc;

// 아래와 같이 되므로 업캐스팅을 막아둠!!! (함수는...)
// let testFunc = (animal: Animal) => {
//   console.log(animal.name);
//   console.log(animal.color);
// };

dogFunc = animalFunc;

let testFunc2 = (dog: Dog) => {
  console.log(dog.name);
};

// 2-2. 매개변수의 개수가 다를 때
// 매개변수의 갯수가 다를때는 할당하려고 하는 쪽의 함수의 타입의 매개변수의 갯수가 더 적을 때에만 호환이 됨.

type Func1 = (a: number, b: number) => void;
type Func2 = (a: number) => void;

let func1: Func1 = (a, b) => {};
let func2: Func2 = (a) => {};

func1 = func2;

// 불가
// func2 = func1;
