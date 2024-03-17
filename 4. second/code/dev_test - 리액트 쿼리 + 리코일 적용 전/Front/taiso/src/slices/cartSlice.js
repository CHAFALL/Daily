import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import { getCartItems, postChangeCart } from "../api/cartApi";



// 왜 이렇게 createAsyncThunk로 싸냐면 extra reducer로 동작시키기 위함이다.
// 액션 생성자와 비동기 로직 통합, 상태 업데이트 자동 처리
export const getCartItemsAsync = createAsyncThunk('getCartItemsAsync', () => {
  return getCartItems()
})

export const postChangeCartAsync = createAsyncThunk('postChangeCartAsync', (param)=>{
  return postChangeCart(param)
})

const initState = []

const cartSlice = createSlice({
  name:'cartSlice',
  initialState:initState,
  extraReducers: (builder) => {
    builder.addCase(getCartItemsAsync.fulfilled, (state, action) => {
      // action: 가져온 데이터

      console.log("getCartItemsAsync.fulfilled")
      console.log(action.payload)

      return action.payload
    })
    .addCase(postChangeCartAsync.fulfilled, (state, action)=> {
      console.log("postChangeCartAsync.fulfilled")

      return action.payload
    })
  }
})

export default cartSlice.reducer