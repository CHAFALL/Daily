/**
 * 기본 타입간의 호환성
 */

// 리터럴이 더 작은 개념임.

let num1: number = 10;
let num2: 10 = 10; // 리터럴

num1 = num2;

// 다운 캐스팅이라서 안됨.
// num2 = num1

// 슈퍼 (조건이 더 적은 타입이 슈퍼가 됨.)
type Animal = {
  name: string;
  color: string;
};

// 서브
type Dog = {
  name: string;
  color: string;
  breed: string;
};

let animal: Animal = {
  name: "기린",
  color: "yellow",
};

let dog: Dog = {
  name: "돌돌이",
  color: "brown",
  breed: "진돗개",
};

animal = dog;

// dog = animal

// 슈퍼
type Book = {
  name: string;
  price: number;
};

// 서브
type ProgrammingBook = {
  name: string;
  price: number;
  skill: string;
};

let book: Book;
let programmingBook: ProgrammingBook = {
  name: "한 입 크기로 잘라먹는 리액트",
  price: 30000,
  skill: "reactjs",
};

book = programmingBook;
// programmingBook = book;

/**
 * 초과 프로퍼티 검사 -> 초기화를 할 때 초기화하는 값으로 객체 리터럴 값을 사용하면 발생하는 문제
 */

type Book2 = {
  name: string;
  price: number;
};

let book2: Book2 = {
  name: "한 입 크기로 잘라먹는 리액트",
  price: 30000,
  // skill: "reactjs",
};

// 이 초과 프로퍼티 검사를 피하려면?
// 초기화 할 때 객체 리터럴 값을 사용한 것이 아니므로 오류 발생 x
let book3: Book2 = programmingBook;

function func(book: Book2) {}

func({
  name: "한 입 크기로 잘라먹는 리액트",
  price: 30000,
  // skill: "reactjs",
});

// 이렇게 하면 초과 프로퍼티 검사를 피할 수 O
func(programmingBook);
