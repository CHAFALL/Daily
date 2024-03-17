import { Cookies } from "react-cookie";

const cookies = new Cookies();

export const setCookie = (name, value, days = 1) => {
  const expires = new Date();
  expires.setUTCDate(expires.getUTCDate() + days); //보관기한

  return cookies.set(name, value, { expires, path: "/" });
  // 하위 경로에서 다 써야 되므로
};

export const getCookie = (name) => {
  return cookies.get(name);
};

export const removeCookie = (name, path = '/') => {
  cookies.remove(name, {path:path})
}
