import { ReactElement, useState } from "react";
import { TodoDispatchContext, useTodoDispatch } from "../App";

interface Props {
  // 리턴값 void
  // onClickAdd: (text: string) => void;
  children: ReactElement;
}

export default function Editor(props: Props) {
  const dispatch = useTodoDispatch();

  // 제네릭 괄호 보고 자동 적용
  // 초기값을 딱히 넣을 것이 없어서 ()안 값이 빈 값일때는 따로 설정가능 <- 이렇게 하면 undefined도 가능. ( 주로 ""를 넣어주는 것이 맞음)
  // const [text, setText] = useState<string>();
  const [text, setText] = useState("");

  // 이벤트 핸들러를 사용할 시 타입 설정법
  // 이런 e 방식 어떻게 알죠?? -> html 쪽에 만들면 뜨드라 -> 이렇게 하면 훨씬 안정적
  const onChangeInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    setText(e.target.value);
  };

  const onClickButton = () => {
    dispatch.onClickAdd(text);
    setText("");
  };

  return (
    <div>
      <input value={text} onChange={onChangeInput} />
      <button onClick={onClickButton}>추가</button>
    </div>
  );
}
