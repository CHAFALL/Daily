import React, { useState } from "react";
import useCustomLogin from "../../hooks/useCustomLogin";

const initState = {
  email: "",
  pw: "",
};

function LoginComponent(props) {
  const [loginParam, setLoginParam] = useState({ ...initState });

  const { doLogin, moveToPath } = useCustomLogin();

  const handleChange = (e) => {
    loginParam[e.target.name] = e.target.value;

    setLoginParam({ ...loginParam });
  };

  const handleClickLogin = (e) => {
    // dispatch(login(loginParam))

    doLogin(loginParam).then((data) => {
      if (data.error) {
        alert("이메일과 패스워드를 확인해 주세요.");
      } else {
        moveToPath("/");
      }
    });

    // dispatch(loginPostAsync(loginParam))
    // .unwrap()
    // .then(data => {
    //   console.log('after unwrap')
    //   console.log(data)

    //   if(data.error){
    //       alert("이메일과 패스워드를 확인해 주세요.")
    //   } else {
    //     alert("로그인 성공")

    //     // replace : 뒤로가기를 할 때 다시 로그인하는 정보가 나온다거나 하는 것이 없어짐.(replace는 옵션임.)
    //     navigate({pathname: '/'}, {replace:true})
    //   }

    // })
    // 개발자들에게 비동기가 어려운 이유 -> 언제 데이터가 올지 몰라서 거기에 맞춰서 코딩을 하는 것이 어려움
    // unWrap : 내가 비동기 호출을 했지만 동기화 된 것처럼 결과를 받아서 보는 상황에 유용
    // unWrap : 비동기 통신을 하고 크리에디트 어싱크 썬크로 뭔가를 처리하고 싶은데 결과 데이터를 직접 받아서 보고 싶을 때 unWrap 이용.
    // 자주 쓰는 것은 비추.(디버깅 하는 용도로 쓰는 건 낫 베드)
  };

  return (
    <div className="border-2 border-sky-200 mt-10 m-2 p-4">
      <div className="flex justify-center">
        <div className="text-4xl m-4 p-4 font-extrabold text-blue-500">
          Login Component
        </div>
      </div>
      <div className="flex justify-center">
        <div className="relative mb-4 flex w-full flex-wrap items-stretch">
          <div className="w-full p-3 text-left font-bold">Email</div>
          <input
            className="w-full p-3 rounded-r border border-solid border-neutral-500 shadow-md"
            name="email"
            type={"text"}
            value={loginParam.email}
            onChange={handleChange}
          ></input>
        </div>
      </div>
      <div className="flex justify-center">
        <div className="relative mb-4 flex w-full flex-wrap items-stretch">
          <div className="w-full p-3 text-left font-bold">Password</div>
          <input
            className="w-full p-3 rounded-r border border-solid border-neutral-500 shadow-md"
            name="pw"
            type={"password"}
            value={loginParam.pw}
            onChange={handleChange}
          ></input>
        </div>
      </div>
      <div className="flex justify-center">
        <div className="relative mb-4 flex w-full justify-center">
          <div className="w-2/5 p-6 flex justify-center font-bold">
            <button
              className="rounded p-4 w-36 bg-blue-500 text-xl  text-white"
              onClick={handleClickLogin}
            >
              LOGIN
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default LoginComponent;
