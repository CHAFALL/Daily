// axios는 2가지 형태의 axios가 있다
// 1. 엑세스 토큰을 가지고 전달해주는 엑시오스(interceptors 이용)
// 2. 아무것도 없이 로그인 할 때처럼 그냥 전달하는 엑시오스

import axios from "axios";
import { getCookie } from "./cookieUtil";

const jwtAxios = axios.create();

//처리하기 전에 해야 되는 것과 뭔가 잘못 되었을 때 해야되는 것을 작성

//before request
const beforeReq = (config) => {
  console.log("before request.............");
  const memberInfo = getCookie("member");

  if (!memberInfo) {
    console.log("Member NOT FOUND");
    // axios의 결과는 Promise여서 Promise로 리턴을 하게끔
    return Promise.reject({ response: { data: { error: "REQUIRE_LOGIN" } } });
  }

  const { accessToken } = memberInfo;

  // Authorization 헤더 처리
  config.headers.Authorization = `Bearer ${accessToken}`;

  return config;
};
//fail request
const requestFail = (err) => {
  console.log("request error............");
  return Promise.reject(err);
};
//before return response
const beforeRes = async (res) => {
  console.log("before return response...........");
  return res;
};
//fail response
const responseFail = (err) => {
  console.log("response fail error.............");
  return Promise.reject(err);
};
jwtAxios.interceptors.request.use(beforeReq, requestFail);
jwtAxios.interceptors.response.use(beforeRes, responseFail);

export default jwtAxios;
