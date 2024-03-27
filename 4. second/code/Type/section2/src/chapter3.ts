// object
// 이걸 객체 리터럴타입이라고 함
// :object로만 하면 속성 접근이 불가능해서 구조기준으로 해줘야 한다. (구조적 타입 시스템)
let user: {
  id?: number; // ?를 달면 있어도 되고 없어도 되는 값 (이런것을 optional property라고 함)
  name: string;
} = {
  id: 1,
  name: "user1",
};

user = {
  name: "홍길동",
};

let config: {
  readonly apiKey: string; // 이러면 바꿀 수 없음
} = {
  apiKey: "MY API KEY",
};

// config.apiKey = "hacked";
