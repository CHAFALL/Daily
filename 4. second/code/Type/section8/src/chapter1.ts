/**
 * 인덱스드 엑세스 타입
 */

interface Post {
  title: string;
  content: string;
  author: {
    id: number;
    name: string;
    age: number;
  };
}

// [2]
// 인덱스드 엑세스 타입은 객체의 특정 프로퍼티 뿐만 아니라 배열 타입으로부터 특정 요소의 타입을 뽑아내는 것도 가능

type PostList = {
  title: string;
  content: string;
  author: {
    id: number;
    name: string;
    age: number;
  };
}[];

// 우리가 뽑아내고 싶은 속성의 타입을 이렇게 써줄 수 있다.
// 주의사항 : 인덱스드 엑세스에는 값이 올 수 없고 타입만 올 수 있다.
// 이렇게 안의 안의 안의 타입을 가져올 수 있다!!
// function printAuthorInfo3(author: Post["author"]["id"]){}

function printAuthorInfo(author: Post["author"]) {
  console.log(`${author.name}-${author.id}`);
}

const post: Post = {
  title: "게시글 제목",
  content: "게시글 본문",
  author: {
    id: 1,
    name: "chafa",
    age: 27,
  },
};

printAuthorInfo(post.author);

// [2]
function printAuthorInfo2(author: PostList[number]["author"]) {
  console.log(`${author.name}-${author.id}`);
}

const post2: PostList[number] = {
  title: "게시글 제목",
  content: "게시글 본문",
  author: {
    id: 1,
    name: "chafa",
    age: 27,
  },
};

printAuthorInfo(post2.author);

type Tup = [number, string, boolean];

type Tup0 = Tup[0];

type Tup1 = Tup[1];

type Tup2 = Tup[2];

// type Tup3 = Tup[3];


// 이렇게 넣으면 어떻게 뽑아오냐면 이 튜플 타입 안에 있는 모든 타입의 최적의 공통 타입을 불러옴
type TupNum = Tup[number];


// 인덱스트 엑세스 타입은 복잡하고 큰 타입으로부터 잘게 잘게 우리가 필요한 만큼만 타입을 추출할 수 있기 때문에 실무에서도 우리가 굉장히 요긴하게 자주 사용할 수 있음.