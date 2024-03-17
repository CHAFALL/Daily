import {getCartItemsAsync, postChangeCartAsync} from "../slices/cartSlice"

import { useDispatch, useSelector } from "react-redux"

const useCustomCart = () => {
  // 지금 현재 카트에 있는 상품을 바로 볼 때 이게 필요
  const cartItems = useSelector(state => state.cartSlice)

  const dispatch = useDispatch()

  // 카트 아이템을 가져오거나 이럴 때 필요
  const refreshCart = () => {
    dispatch(getCartItemsAsync())
  }

  // 내가 무언가를 변경할 때 이용
  const changeCart = (param) => {
    dispatch(postChangeCartAsync(param))
  }

  return {cartItems, refreshCart, changeCart}

}

export default useCustomCart