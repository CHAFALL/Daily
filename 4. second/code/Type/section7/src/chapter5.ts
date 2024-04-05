/**
 * 프로미스
 */

// resolve: 비동기 성공 했을 시 호출하는 함수이고 이때 이 함수의 인수로 전달하는 이 ㄱ밧은 비동기 작업의 결과값이 됨.
// reject: 비동기 작업이 실패했을 때 호출하는 함수이고 여기다가 실패의 이유를 넣는다.
const promise = new Promise<number>((resolve, reject) => {
  setTimeout(() => {
    resolve(20);
    reject("~~때문에 실패");
  }, 3000);
});

promise.then((response) => {
  console.log(response * 10); // 20
});

promise.catch((err) => {
  if (typeof err === "string") {
    console.log(err);
  }
});

/**
 * 프로미스를 반환하는 함수의 타입을 정의
 */

interface Post {
  id: number;
  title: string;
  content: string;
}

function fetchPost(): Promise<Post> {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve({
        id: 1,
        title: "게시글 제목",
        content: "게시글 컨텐츠",
      });
    }, 3000);
  });
}

const postRequest = fetchPost();

postRequest.then((post)=> {
  post.id
})
