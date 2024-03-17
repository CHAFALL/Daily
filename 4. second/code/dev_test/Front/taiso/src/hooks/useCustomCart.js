import { useRecoilState } from "recoil";
import { cartState } from "../atoms/cartState";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { getCartItems, postChangeCart } from "../api/cartApi";
import { useEffect } from "react";

const useCustomCart = () => {
  const [cartItems, setCartItems] = useRecoilState(cartState);

  const queryClient = useQueryClient();

  const changeMutation = useMutation({
    mutationFn: (param) => postChangeCart(param),
    onSuccess: (result) => {
      setCartItems(result);
    },
  });

  const query = useQuery({
    queryKey: ["cart"],
    queryFn: getCartItems,
    staleTime: 1000 * 60 * 60,
  });
  // 이렇게 변경시키는 것은 isSuccess를 안으로 하면 안되고 useEffect로 빼줌??
  useEffect(() => {
    if (query.isSuccess) {
      queryClient.invalidateQueries("cart");
      setCartItems(query.data);
    }
  }, [query.isSuccess]);

  const changeCart = (param) => {
    changeMutation.mutate(param)
  }
  return {cartItems, changeCart}
};

export default useCustomCart;
