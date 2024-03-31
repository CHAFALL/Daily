/**
 * 타입 좁히기
 * 조건문 등을 이용해 넓은타입에서 좁은타입으로
 * 타입을 상황에 따라 좁히는 방법
 */

type Person = {
  name: string;
  age: number;
};

// value => number : toFixed
// value => string : toUpperCase
// value => Date : getTime
// value => Person : name은 age살 입니다.
function func(value: number | string | Date | null | Person) {
  // 원래는 아래와 같은 함수는 동작 x
  // value;
  // value.toFixed();
  // value.toUpperCase();

  // 이렇게 타입을 좁혀주는 방식들을 타입가드라고 함.
  if (typeof value === "number") {
    console.log(value.toFixed());
  } else if (typeof value === "string") {
    console.log(value.toUpperCase());
    // 왼쪽에 있는 값이 오른쪽에 있는 인스턴스냐를 의미
  } else if (value instanceof Date) {
    console.log(value.getTime);
    // value가 null이 아니고 value에 age가 있다면?
  } else if (value && "age" in value) {
    console.log(`${value.name}은 ${value.age}살 입니다.`);
  }
  // Date를 쓰려고 object 이용했음 (단, 이 방식은 null이나 다른 객체 있으면 불가) -> (null도 object에 속하므로)
  // else if (typeof value === "object") {
  //   console.log(value.getTime);
  // }

  // 인스턴스 연산자는 우측에 타입이 들어가선 안됨. ( 인스턴스 연산자는 클래스를 판단하는 거임)
  // else if (value instanceof Person) {
  // }
}
