// axios는 2가지 형태의 axios가 있다
// 1. 엑세스 토큰을 가지고 전달해주는 엑시오스(interceptors 이용)
// 2. 아무것도 없이 로그인 할 때처럼 그냥 전달하는 엑시오스

import axios from "axios";
import { getCookie, setCookie } from "./cookieUtil";
import { API_SERVER_HOST } from "../api/todoApi";

const jwtAxios = axios.create();

const refreshJWT = async (accessToken, refreshToken) => {
  const host = API_SERVER_HOST;

  const header = { headers: { Authorization: `Bearer ${accessToken}` } };

  const res = await axios.get(
    `${host}/api/member/refresh?refreshToken=${refreshToken}`,
    header
  );

  console.log(res.data);

  return res.data;
};

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

  const data = res.data;

  if (data && data.error === "ERROR_ACCESS_TOKEN") {
    const memberCookieValue = getCookie("member");

    const result = await refreshJWT(
      memberCookieValue.accessToken,
      memberCookieValue.refreshToken
    );

    // 새로운 accessToken, refreshToken

    // 가져왔으면 갱신해줘야지
    memberCookieValue.accessToken = result.accessToken;
    memberCookieValue.refreshToken = result.refreshToken;

    setCookie("member", JSON.stringify(memberCookieValue), 1);

    // 토큰 때문에 화면에서 에러가 뜨는 부분을 다시 한번 호출을 해줘야 됨.
    // res.config가 어떤거지???
    const originalRequest = res.config

    originalRequest.headers.Authorization = `Bearer ${result.accessToken}`
    // 바뀐 리프레시 토큰으로 다시 호출
    return await axios(originalRequest)
  }

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
