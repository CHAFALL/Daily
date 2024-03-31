/**
 * 함수 타입 정의
 */

// 어떤 [타입의] 매개변수를 받고, 어떤 [타입의] 결과값을 반환하는지 이야기
// 반환값의 타입이 없다고 해도 return값의 반환값을 보고 자동으로 추론
function func(a: number, b: number): number {
  return a + b;
}

/**
 * 화살표 함수의 타입을 정의하는 방법
 */

const add = (a: number, b: number): number => a + b;

/**
 * 함수의 매개변수
 */

// 선택적 매개변수(?.) 보다 필수 매개변수가 뒤에 있으면 안된다.
function introduce(name = "chafa", age: number, tall?: number) {
  console.log(`name: ${name}`);
  // 여기부분 은근 중요할지도???
  if (typeof tall === "number") {
    console.log(`taill: ${tall + 10}`);
  }
}

introduce("chafa", 27, 177);

introduce("차파", 27);

// 갯수 제한을 두고 싶으면..
function getSum(...rest: [number, number, number]) {
  let sum = 0;
  rest.forEach((it) => (sum += it));
  return sum;
}

getSum(1, 2, 3);
// getSum(1, 2, 3, 4, 5);
