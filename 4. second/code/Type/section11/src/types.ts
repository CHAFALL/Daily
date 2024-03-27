// 공통으로 여러 컴포넌트에서 사용되는 타입을 유지해야 될 때는 별도의 타입스크립트 파일을 만들어서 이 타입들을 분리하는 게 좋음.

// 객체 타입 설정
export interface Todo {
  id: number;
  content: string;
}