/**
 * 맵드 타입
 * 주의사항 -> 맵드 타입은 인터페이스에서는 쓸 수가 없음. (무조건 타입 별칭으로만)
 */

interface User {
  id: number;
  name: string;
  age: number;
}

type PartialUser = {
  [key in "id" | "name" | "age"]?: User[key];
};

type BooleanUser = {
  [key in keyof User]: boolean;
};

type ReadOnlyUser = {
  readonly [key in keyof User]: User[key];
};

// 한명의 유저 정보를 불러오는 기능
function fetchUser(): User {
  // ...기능
  return {
    id: 1,
    name: "chafa",
    age: 27,
  };
}

const user = fetchUser();
user.id = 1;

// 한명의 유저 정보를 수정하는 기능
function updateUser(user: PartialUser) {
  // ... 수정하는 기능
}

updateUser({
  // id: 1,
  // name: "chafa",
  age: 25,
});


// 이건 활용도가 굉장히 높고 실무에서도 굉장히 자주 쓰이는 타입이다!!!!!