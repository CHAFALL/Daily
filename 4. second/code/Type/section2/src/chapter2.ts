// 배열
// 방식 1 (이걸 추천)
let numArr: number[] = [1, 2, 3];
let strArr: string[] = ["hello", "im", "winterload"];
// 방식 2 (Array<제네릭>)
let boolArr: Array<boolean> = [true, false, true];

// 배열에 들어가는 요소들의 타입이 다양한 경우
let multiArr: (number | string)[] = [1, "hello"];

// 다차원 배열의 타입을 정의하는 방법
let doubleArr: number[][] = [
  [1, 2, 3],
  [4, 5],
];

// 튜플 (JS는 없고, TS에서만 특별히 제공)
// 길이와 타입이 고정된 배열
let tup1: [number, number] = [1, 2];
let tup2: [number, string, boolean] = [1, "2", true];

const users: [string, number][] = [
  ["user1", 1],
  ["user2", 2],
  ["user3", 3],
  ["user4", 4],
  // [5, "user5"]
];
