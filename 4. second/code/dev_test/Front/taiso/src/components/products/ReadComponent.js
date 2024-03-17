import { API_SERVER_HOST } from "../../api/todoApi";
import { getOne } from "../../api/productsApi";
import FetchingModal from "../common/FetchingModal";
import useCustomMove from "../../hooks/useCustomMove";
import useCustomCart from "../../hooks/useCustomCart";
import useCustomLogin from "../../hooks/useCustomLogin";
import { useQuery } from "@tanstack/react-query";

const initState = {
  pno: 0,
  pname: "",
  pdesc: "",
  price: 0,
  uploadFileNames: [],
};

const host = API_SERVER_HOST;

function ReadComponent({ pno }) {
  
  // 화면 이동용 함수
  const { moveToList, moveToModify, page, size } = useCustomMove();

  // 현재 사용자의 장바구니 아이템들
  const {cartItems, changeCart} = useCustomCart()

  const {loginState} = useCustomLogin()

  // v5에서는 파라미터가 객체여야 함, v4까지는 , 로 처리가 되었음

  // data를 넣어두면 비동기 처리를 하는데 마치 동기화된 코드처럼 쓸 수 있음.
  // useState(fetching, product 관련) 필요 x

  const {data, isFetching} = useQuery({
    queryKey: ['products', pno],
    queryFn: () => getOne(pno),
    staleTime: 1000 * 10
  })

  // staleTime을 쓰면 api 서버에 부하가 줄음

  // 빨리 갔다가 빨리 오면 호출을 안하지만, 10초가 지나서 스테일한 상태에서 딴데 갔다가 오면 다시 호출 -> 이게 리액트 쿼리를 쓰는 진짜 이유 중에 하나 (더 이상 신선하지 않은 상태가 되면 다시 리필하는 느낌)

  const handleClickAddCart = () => {
    let qty = 1

    // 타입 이렇게 다 맞춰줄 것이면 안전하게 parseInt, 또는 타입스크립트로 
    const addedItem = cartItems.filter(item => item.pno === parseInt(pno))[0]

    if (addedItem){
      if (window.confirm('이미 추가된 상품입니다. 추가하시겠습니까?') === false){
        return
      }
      qty = addedItem.qty + 1
    }
    changeCart({email: loginState.email, qty:qty, pno:pno})
  }

  
  const product = data || initState

  return (
    <div className="border-2 border-sky-200 mt-10 m-2 p-4">
      {isFetching ? <FetchingModal /> : <></>}
      <div className="flex justify-center mt-10">
        <div className="relative mb-4 flex w-full flex-wrap items-stretch">
          <div className="w-1/5 p-6 text-right font-bold">PNO</div>
          <div className="w-4/5 p-6 rounded-r border border-solid shadow-md">
            {product.pno}
          </div>
        </div>
      </div>
      <div className="flex justify-center">
        <div className="relative mb-4 flex w-full flex-wrap items-stretch">
          <div className="w-1/5 p-6 text-right font-bold">PNAME</div>
          <div className="w-4/5 p-6 rounded-r border border-solid shadow-md">
            {product.pname}
          </div>
        </div>
      </div>
      <div className="flex justify-center">
        <div className="relative mb-4 flex w-full flex-wrap items-stretch">
          <div className="w-1/5 p-6 text-right font-bold">PRICE</div>
          <div className="w-4/5 p-6 rounded-r border border-solid shadow-md">
            {product.price}
          </div>
        </div>
      </div>
      <div className="flex justify-center">
        <div className="relative mb-4 flex w-full flex-wrap items-stretch">
          <div className="w-1/5 p-6 text-right font-bold">PDESC</div>
          <div className="w-4/5 p-6 rounded-r border border-solid shadow-md">
            {product.pdesc}
          </div>
        </div>
      </div>
      <div className="w-full justify-center flex flex-col m-auto items-center">
        {product.uploadFileNames.map((imgFile, i) => (
          <img
            alt="product"
            key={i}
            className="p-4 w-1/2"
            src={`${host}/api/products/view/${imgFile}`}
          />
        ))}
      </div>
      <div className="flex justify-end p-4">
        <button
          type="button"
          className="inline-block rounded p-4 m-2 text-xl w-32 text-white bg-green-500"
          onClick={handleClickAddCart}
        >
          Add Cart
        </button>
        <button
          type="button"
          className="inline-block rounded p-4 m-2 text-xl w-32 text-white bg-red-500"
          onClick={() => moveToModify(pno)}
        >
          Modify
        </button>
        <button
          type="button"
          className="rounded p-4 m-2 text-xl w-32 text-white bg-blue-500"
          onClick={() => moveToList({ page, size })}
        >
          List
        </button>
      </div>
    </div>
  );
}

export default ReadComponent;
