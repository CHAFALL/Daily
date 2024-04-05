/**
 * keyof 연산자
 */

// 이 typeof 연산자는 이런식으로 type을 정의할 때 사용하면 어떤 변수의 type을 이렇게 뽑아내는 용도로도 활용할 수 있음.
type Person = typeof person;

// keyof연산자은 뒤에 반드시 타입이 와야 됨

function getPropertyKey(person: Person, key: keyof Person) {
  return person[key];
}

// 이렇게도 가능.
function getPropertyKey2(person: Person, key: keyof typeof person) {
  return person[key];
}

const person = {
  name: "차파",
  age: 27,
};

getPropertyKey(person, "name");
