/**
 * 타입 추론 -> 추론할 정보가 있으면 해주고 없으면 안해주는 느낌
 */

let a = 10; // let은 const와는 달리 좀더 범용적인 타입으로 추론을 해주는 것을 알 수 있다. (조금 더 넓은 타입으로 추론을 해주는 것을 "타입넓히기"라고 함)
let b = "hello";
let c = {
  id: 1,
  name: "chafa",
  profile: {
    nickname: "ccc",
  },
  urls: ["https://ccc.com"],
};

let { id, name, profile } = c;

let [one, two, three] = [1, "hello", true];

function func(message = "hello") {
  return "hello";
}

// any 진화 (암묵적 any타입일 때 적용이 됨.)
// 이런 방식 비추!!!

// 커서 올려보면서 타입이 어떻게 추론되어가는지 보기
// 초기값을 토대로 판단하네??

// 암묵적 any 타입 (let d:any; <- 이건 암묵적 아님.., 이렇게 하면 함수 어디서든 다 쓸 수 있게됨.)

let d;
d = 10;
d.toFixed();
// d.toUpperCase();

d = "hello";
d.toUpperCase();
// d.toFixed();

const num = 10; // 리터럴 타입으로 됨을 알 수 있다.
const str = "hello";

let arr = [1, "string"]; // union 타입으로 됨을 알 수 있다.
