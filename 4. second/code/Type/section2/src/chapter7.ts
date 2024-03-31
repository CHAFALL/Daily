// void
// void -> 공허 -> 아무것도 없다.
// void -> 아무것도 없는 타입
// 왜 undefined랑 null이 있는데 void가 생겼을까? -> return를 꼭 넣어줘야 됨..

function func1(): string {
  return "hello";
}

function func2(): void {
  console.log("hello");
}

let a: void;

// 불가
// a = 1;
// a = "hello";
// a = {};

// 얘만 담을 수 있음
a = undefined;
// 예외적으로 엄격한 null 검사를 false로 하면 null도 담을 수 있음
// a = null;

// never
// never -> 존재하지 않는
// 불가능한 타입
// 반환값이 있는 것 자체가 모순일 때

function func3(): never {
  // 무한 루프
  while (true) {}
}

// 실행되면 바로 프로그램이 중지될 것이므로 반환값 타입으로 never가 적합
function func4(): never {
  throw new Error();
}

let anyVar: any;

let b: never;

// 얘는 정말 아무값도 담을 수 없음
// b = 1;
// b = {};
// b = "";
// b = undefined;
// b = null;
// b = anyVar;
