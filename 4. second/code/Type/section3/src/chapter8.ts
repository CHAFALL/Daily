// 더 쉽고 정확하게 직관적으로 타입을 좁힐 수 있도록 객체 타입을 정의하는 특별한 방법

/**
 * 서로소 유니온 타입 (이것도 중요하다고 봄(ME))
 * 교집합이 없는 타입들로만 만든 유니온 타입을 말함
 */

// tag를 넣어서 직관적이도록 해줌
// tag를 통해서 객체가 겹칠 수 없도록도 해줌. (교집합이 없어짐.)

type Admin = {
  tag: "ADMIN";
  name: string;
  kickCount: number;
};

type Member = {
  tag: "MEMBER";
  name: string;
  point: number;
};

type Guest = {
  tag: "GUEST";
  name: string;
  visitCount: number;
};

type User = Admin | Member | Guest;

// Admin -> {name}님 현재까지 {kickCount}명 강퇴했습니다.
// Member -> {name}님 현재까지 {point}모았습니다.
// Guest -> {name}님 현재까지 {visitCount}번 오셨습니다.

function login(user: User) {
  switch (user.tag) {
    case "ADMIN": {
      console.log(`${user.name}님 현재까지 ${user.kickCount}명 강퇴했습니다.`);
      break;
    }
    case "MEMBER":
      {
        console.log(`${user.name}님 현재까지 ${user.point}모았습니다.`);
      }
      break;
    case "GUEST": {
      console.log(`${user.name}님 현재까지 ${user.visitCount}번 방문했습니다.`);
      break;
    }
  }

  // if (user.tag === "ADMIN") {
  //   console.log(`${user.name}님 현재까지 ${user.kickCount}명 강퇴했습니다.`);
  // } else if (user.tag === "MEMBER") {
  //   console.log(`${user.name}님 현재까지 ${user.point}모았습니다.`);
  // } else {
  //   console.log(`${user.name}님 현재까지 ${user.visitCount}번 방문했습니다.`);
  // }
}

/**
 * 복습겸 한가지 더 사례
 */

// 비동기 작업의 결과를 처리하는 객체

// 즉 동시에 여러개의 상태를 표현해야되는 이런 객체의 타입을 정의할 때는 선택적 프로퍼티를 사용하는 것보다는 상태에 따라서 이런식으로 타입들을 각각 잘게 쪼개어 이렇게 state나 tag같은 프로퍼티들을 추가해서 서로소 union 타입으로 만들어주는게 좋다.
// -> 그래야 더 직관적이고 안전하게 타입을 좁힐 수 있음.

type LoadingTask = {
  state: "LOADING";
};

type FailedTask = {
  state: "FAILED";
  error: {
    message: string;
  };
};

type SuccessTask = {
  state: "SUCCESS";
  response: {
    data: string;
  };
};

type AsyncTask = LoadingTask | FailedTask | SuccessTask;

// 별로 안 좋은 예
// type AsyncTask = {
//   state: "LOADING" | "FAILED" | "SUCCESS";
//   error?: {
//     message: string;
//   };
//   response?: {
//     data: string;
//   };
// };

// 로딩 중 -> 콘솔에 로딩중 출력
// 실패 -> 실패 : 에러메시지를 출력
// 성공 -> 성공 : 데이터를 출력
function processResult(task: AsyncTask) {
  switch (task.state) {
    case "LOADING": {
      console.log("로딩 중");
      break;
    }
    case "FAILED": {
      console.log(`에러 발생: ${task.error.message}`);
      break;
    }
    case "SUCCESS": {
      console.log(`에러 발생: ${task.response.data}`);
      break;
    }
  }
}

const loading: AsyncTask = {
  state: "LOADING",
};

const failed: AsyncTask = {
  state: "FAILED",
  error: {
    message: "오류 발생 원인은 ~~",
  },
};

const success: AsyncTask = {
  state: "SUCCESS",
  response: {
    data: "데이터 ~~",
  },
};
