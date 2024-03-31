// any (치트키 같지만 오류를 못 잡아냄, 이러면 TS가 가진 이점을 다 포기하는 느낌)
// 특정 변수의 타입을 우리가 확실히 모를때

let anyVar: any = 10;

anyVar = "hello";
anyVar = true;
anyVar = {};
anyVar = () => {};

// 가능은 하지만 type에 따라 오류가 뜰 수 있음.
// anyVar.toUpperCase();
// anyVar.toFixed();

// 이렇게도 됨.
// any 타입은 변수에 지정할 경우 모든 타입의 값을 다 할당받을 수 있고 반대로 모든 타입의 변수에 다 any 타입의 값을 집어넣을 수 있다.
let num: number = 10;
num = anyVar;

// unknown
// 그래서 any보단 조금 더 안전한 방식
// unknown은 이런식으로 모든 값을 다 저장가능하지만 반대로는 안됨.
let unknownVar: unknown;
unknownVar = "";
unknownVar = 1;
unknownVar = () => {};

// 아래와 같은 것 안됨. (연산도 못함)
// num = unknownVar;
// unknownVar.toUpperCase();

// 이렇게는 가능 (이런 것을 타입 정제 또는 타입 좁히기라고 함.)
if (typeof unknownVar === "number") {
  num = unknownVar;
}
