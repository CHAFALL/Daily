import { useTodoDispatch } from "../App";
import { Todo } from "../types";

interface Props extends Todo {
  
}

export default function TodoItem(props: Props) {

  const dispatch = useTodoDispatch();

  const onClickButton = () => {
    dispatch.onClickDelete(props.id);
  };

  return (
    <div>
      {props.id}번 : {props.content}
      <button onClick={onClickButton}>삭제</button>
    </div>
  );
}

// 타입스크립트는 라이브러리들의 코드도 타입 검사를 수행함. -> 그렇게 때문에 라이브러리 코드들에 대한 타입 정보가 제공되지 않은 상황에서는 타입 검사가 제대로 이루어지지 않기 때문에 오류가 발생하고 바로 사용할 수가 없다.

// -> 오른쪽에 Ts 마크가 붙어있는 라이브러리는 그냥 명령어만 입력해서 설치해서 바로 쓸 수 있음.

// 그럼 없는 것은 어떻게 해야될까??
// -> Ts마크 대신에 Dt 마크가 있는지 파악
// 이 dt 마크를 클릭하면 새로운 페이지로 이동됨.
// 그러면 해당 라이브러리의 type 정보를 갖고 있는 패키지로 가짐. -> 이걸 추가 설치해줘야 됨.

// 즉, 자바 스크립트로 만들어진 라이브러리를 사용할 때는 그 라이브러리에 타입 정보만 제공하는 패키지가 별도로 있는지 확인 필요.1