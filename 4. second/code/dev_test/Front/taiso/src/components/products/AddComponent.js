import React, { useRef, useState } from "react";
import { postAdd } from "../../api/productsApi";
import FetchingModal from "../common/FetchingModal";
import ResultModal from "../common/ResultModal";
import useCustomMove from "../../hooks/useCustomMove";
import { useMutation, useQueryClient } from "@tanstack/react-query";

const initState = {
  pname: "",
  pdesc: "",
  price: 0,
  files: [],
};

// new FormData() -> POST, PUT

function AddComponent(props) {
  const [product, setProduct] = useState(initState);

  // 리액트에서 고유하게 번호(도메 엘리먼트)를 식별할 때 쓰는 것을 useRef라고 함
  const uploadRef = useRef();

  // useQuery 같은 경우는 보관을 해야 해서 key 값이 필요하지만 얘는 그냥 처리를 해주는 것이므로 key 값 같은 것 필요 없음.
  const addMutation = useMutation({mutationFn: (product) => postAdd(product)})


  // 근데 왜 추가했는데 바로 새로운 데이터가 보여지지 않지?? 기존에 stailTime으로 설정해둔 것이 있어서 그럼 -> closeModal쪽으로 ㄱㄱㄱ

  const {moveToList} = useCustomMove()

  // 이렇게 2가지를 설정해줘야 됨.
  // multipart/form-data   FormData()

  const handleChangeProduct = (e) => {
    product[e.target.name] = e.target.value;

    setProduct({ ...product });
  };

  const handleClickAdd = (e) => {
    console.log(product);

    const formData = new FormData();

    // 이렇게 하면 인풋 태그의 돔 객체, 엘리먼트 자체가 나오는데 그 속의 파일이 뭐니?
    const files = uploadRef.current.files;
    // console.log(files)
    // console.log(files.length)

    for (let i = 0; i < files.length; i++) {
      formData.append("files", files[i])
    }

    formData.append("pname", product.pname)
    formData.append("pdesc", product.pdesc)
    formData.append("price", product.price)

    console.log(formData)

    // 원래는 이렇게 직접 호출을 했는데 직접 호출하지 않고 addMutation.mutate()라는 함수를 이용
    // postAdd(formData).then(data => {
    //   setFetching(false)
    //   setResult(data.result)
    // })

    addMutation.mutate(formData)

  };

  const queryClient = useQueryClient()

  const closeModal = () => {
    queryClient.invalidateQueries("products/list")
    moveToList({page:1})
    
  }

  return (
    <div className="border-2 border-sky-200 mt-10 m-2 p-4">
      <div className="flex justify-center">
        <div className="relative mb-4 flex w-full flex-wrap items-stretch">
          <div className="w-1/5 p-6 text-right font-bold">Product Name</div>
          <input
            className="w-4/5 p-6 rounded-r border border-solid border-neutral-300 shadow-md"
            name="pname"
            type={"text"}
            value={product.pname}
            onChange={handleChangeProduct}
          ></input>
        </div>
      </div>
      <div className="flex justify-center">
        <div className="relative mb-4 flex w-full flex-wrap items-stretch">
          <div className="w-1/5 p-6 text-right font-bold">Desc</div>
          <textarea
            className="w-4/5 p-6 rounded-r border border-solid border-neutral-300 shadow-md resize-y"
            name="pdesc"
            rows="4"
            onChange={handleChangeProduct}
            value={product.pdesc}
          >
            {product.pdesc}
          </textarea>
        </div>
      </div>
      <div className="flex justify-center">
        <div className="relative mb-4 flex w-full flex-wrap items-stretch">
          <div className="w-1/5 p-6 text-right font-bold">Price</div>
          <input
            className="w-4/5 p-6 rounded-r border border-solid border-neutral-300 shadow-md"
            name="price"
            type={"number"}
            value={product.price}
            onChange={handleChangeProduct}
          ></input>
        </div>
      </div>
      <div className="flex justify-center">
        <div className="relative mb-4 flex w-full flex-wrap items-stretch">
          <div className="w-1/5 p-6 text-right font-bold">Files</div>
          <input
            ref={uploadRef}
            className="w-4/5 p-6 rounded-r border border-solid border-neutral-300 shadow-md"
            type={"file"}
            multiple={true}
          ></input>
        </div>
      </div>
      <div className="flex justify-end">
        <div className="relative mb-4 flex p-4 flex-wrap items-stretch">
          <button
            type="button"
            className="rounded p-4 w-36 bg-blue-500 text-xl text-white "
            onClick={handleClickAdd}
          >
            ADD
          </button>
        </div>
      </div>
      {addMutation.isPending ? <FetchingModal /> : <></>}
      {addMutation.isSuccess ? <ResultModal
        callbackFn={closeModal}
        title={'Product Add Result'}
        content = {`${addMutation.data.result} 번 상품 등록 완료`}
      ></ResultModal> : <></>}
    </div>
  );
}


// 상품 등록을 할 때는 useMutation을 이용
// useQuery는 select라고 생각하면 되고
// useMutation은 말 그대로 내가 데이터를 변경하고 싶을 때 이용

export default AddComponent;
