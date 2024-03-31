/**
 * 인터페이스의 확장
 */

interface Animal {
  name: string;
  age: number;
}

interface Dog extends Animal {
  name: "hello"; // 이렇게 다시 정의 가능.(오버라이딩 느낌.), 단, 원본 타입의 서브 타입이어야지만 가능!!
  isBark: boolean;
}

const dog: Dog = {
  name: "hello",
  age: 7,
  isBark: true,
};

interface Cat extends Animal {
  name: "hello";
  isScratch: boolean;
}

type Animal2 = {
  name: string;
  age: number;
};
// 보면 interface는 객체 타입이면 다 확장이 가능함을 알 수 있음

interface Chicken extends Animal2 {
  isFly: boolean;
}

// 다중확장도 가능! 
interface DogCat extends Dog, Cat {}

const dogCat: DogCat = {
  name: "hello",
  age: 18,
  isBark: true,
  isScratch: true,
};
