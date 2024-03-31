/**
 * 사용자 정의 타입가드
 */

// 이럴때 서로소 union을 이용하면 좋지만 이번에는 남이 만들어둔 타입이라던가 라이브러리가 그냥 제공하는 타입이라서 우리가 직접 손을 댈수 없는 상황이라고 가정

type Dog = {
  name: string;
  isBark: boolean;
};

type Cat = {
  name: string;
  isScratch: boolean;
};

type Animal = Dog | Cat;

// animal is Dog 이거까지 달아줘야지 타입이 좁혀짐을 알 수 있음
function isDog(animal: Animal): animal is Dog {
  return (animal as Dog).isBark !== undefined;
}

function isCat(animal: Animal): animal is Cat {
  return (animal as Cat).isScratch !== undefined;
}

function warning(animal: Animal) {
  if (isDog(animal)) {
    // 강아지
    animal;
  } else if ("isScratch" in animal) {
    // 고양이
    animal;
  }
}
