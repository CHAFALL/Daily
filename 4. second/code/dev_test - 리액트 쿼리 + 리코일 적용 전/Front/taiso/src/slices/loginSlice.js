import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import { loginPost } from "../api/memberApi";
import { getCookie, removeCookie, setCookie } from "../util/cookieUtil";

const initState = {
  email: "",
};

const loadMemberCookie = () => {
  const memberInfo = getCookie('member')

  return memberInfo
}

export const loginPostAsync = createAsyncThunk("loginPostAsync", (param) =>
  loginPost(param)
);

const loginSlice = createSlice({
  name: "loginSlice",
  initialState: loadMemberCookie() || initState,
  reducers: {
    // state : 기존 상태
    // action : 내가 처리하고 싶은 데이터
    login: (state, action) => {
      console.log("login.........", action);
      // return 데이터를 유지해줘
      console.log(action.payload);
      console.log("------------------");

      setCookie("member", JSON.stringify(action.payload), 1)

      return action.payload;
    },
    logout: () => {
      console.log("logout........");

      removeCookie('member')

      return { ...initState };
    },
  },
  extraReducers: (builder) => {
    // fulfilled : 완료가 되었다, pending: 처리 중, rejected: 문제 발생
    builder
      .addCase(loginPostAsync.fulfilled, (state, action) => {
        console.log("fulfilled");

        const payload = action.payload

        if (!payload.error){
          setCookie("member", JSON.stringify(payload), 1)
        }

        return payload
      })
      .addCase(loginPostAsync.pending, (state, action) => {
        console.log("pending");
      })
      .addCase(loginPostAsync.rejected, (state, action) => {
        console.log("rejected");
      });
  },
});

export const { login, logout } = loginSlice.actions;
export default loginSlice.reducer;
