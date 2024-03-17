import React from "react";
import { API_SERVER_HOST } from "../../api/todoApi";

const host = API_SERVER_HOST;

function CartItemComponent({
  cino,
  pname,
  price,
  pno,
  qty,
  imageFile,
  changeCart,
  email,
}) {
  const handleClickQty = (amount) => {
    changeCart({ email: email, cino: cino, pno: pno, qty: qty + amount });
  };

  return (
    <li key={cino} className="border-2">
      <div className="w-full border-2">
        <div className=" m-1 p-1 ">
          <img src={`${host}/api/products/view/s_${imageFile}`} alt="" />
        </div>
        <div className="justify-center p-2 text-xl ">
          <div className="justify-end w-full"> </div>
          <div>Cart Item No: {cino}</div>
          <div>Pno: {pno}</div>
          <div>Name: {pname}</div>
          <div>Price: {price}</div>
          <div className="flex ">
            <div className="w-2/3"> Qty: {qty} </div>
            <div>
              <button
                className="m-1 p-1 text-2xl bg-orange-500 w-8 rounded-lg"
                onClick={() => handleClickQty(1)}
              >
                {" "}
                +{" "}
              </button>
              <button
                className="m-1 p-1 text-2xl bg-orange-500 w-8 rounded-lg"
                onClick={() => handleClickQty(-1)}
              >
                {" "}
                -{" "}
              </button>
            </div>
          </div>
          <div className="flex text-white font-bold p-2 justify-center">
            <button
              className="m-1 p-1 text-xl text-white bg-red-500 w-8 rounded-lg"
              onClick={() => handleClickQty(-1 * qty)}
            >
              X
            </button>
          </div>
          <div className="font-extrabold border-t-2 text-right m-2 pr-4">
            {qty * price} 원
          </div>
        </div>
      </div>
    </li>
  );
}

// 이렇게 짯을 때 문제가 되는 점 : 장바구니에 넣었을 때의 가격과 실제로 구매할 때의 가격이 달라지면 우얌??? -> 그 상품이 삭제되지 않는 한 가격은 못 바꾼다. 이런식으로 막을 수 있음.

export default CartItemComponent;
