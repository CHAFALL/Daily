// enum 타입
// 여러가지 값들에 각각 이름을 부여해 열거해두고 사용하는 타입 (JS에는 없고 TS만 제공)

// 이렇게 enum을 이용하면 내가 0을 관리자로 했었는지 유저로 했었는지 헷갈릴 일이 없음.

// 숫자를 이렇게 일일이 기입 안해줘도 알아서 0부터 넣어줌
// 아래와 같이 하면?? 0, 10, 11 이렇게 자동으로 넣어줌.
// 이런 것을 숫자형 enum이라고 함

enum Role {
  ADMIN,
  USER = 10,
  GUEST,
}

enum Language {
  korean = "ko",
  english = "en",
}

const user1 = {
  name: "user1",
  role: Role.ADMIN,
  language: Language.korean,
};

const user2 = {
  name: "user2",
  role: Role.USER,
};

const user3 = {
  name: "user3",
  role: Role.GUEST,
};

console.log(user1, user2, user3);
// {name: user1, role: 0} {name: user2, role: 1} {name: user3, role: 2}
