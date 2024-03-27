// 타입 별칭
// 공통적으로 사용되는 것
// 스코프 내에서 중복되는 것 주의!!!!
type User = {
  id: number;
  name: string;
  nickname: string;
  birth: string;
  bio: string;
  location: string;
};

let user: User = {
  id: 1,
  name: "user1",
  nickname: "chafa",
  birth: "1997.08.23",
  bio: "안녕",
  location: "대구",
};

let user2: User = {
  id: 1,
  name: "user2",
  nickname: "chafa2",
  birth: "1997.08.24",
  bio: "안녕2",
  location: "대구2",
};

// 인덱스 시그니처
// 주의할 점 -> 조건을 위배하지만 않으면 모든 객체를 허용하는 타입이다.
// 예 ) 아무런 속성이 없어도 조건을 위배할 것이 없어서 오류 발생 x
type CountryCodes = {
  [key: string]: string;
};

let countryCodes: CountryCodes = {
  Korea: "ko",
  UnitedState: "us",
  UnitedKingdom: "uk",
};

// 있어야 될 놈은 써놓을 수 있다.
type CountryNumberCodes = {
  [key: string]: number;
  Korea: number;
};

let countryNumberCodes: CountryNumberCodes = {
  Korea: 410,
  UnitedState: 840,
  UnitedKingdom: 826,
};
