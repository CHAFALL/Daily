import React from 'react';
import { useNavigate } from 'react-router-dom';

interface ModalProps {
  closeModal: () => void;
}

const SelectWriteModal: React.FC<ModalProps> = ({ closeModal }) => {
  const navigate = useNavigate();

  const goToSaleWrite = () => {
    navigate(`/write/sale`);
    closeModal();
  };

  const goToBuyWrite = () => {
    navigate(`/write/buy`);
    closeModal();
  };

  return (
    <>
      <div
        className="fixed w-full top-0 bottom-[65px] left-0 right-0 transition ease-in-out delay-200 z-[11] bg-black bg-opacity-50 max-w-[500px] mx-auto"
        onClick={closeModal}
      >
        <div className=" fixed w-full h-full flex items-center justify-center max-w-[500px] mx-auto">
          <div className="p-2 rounded-2xl absolute bottom-[70px] z-[12]">
            <div className="flex flex-col bg-base-200 w-32 text-white">
              <button
                className="animate-sheetOn bg-BID_BLACK rounded-2xl text-center p-3"
                onClick={() => goToSaleWrite()}
              >
                경매글 등록
              </button>
              <button
                className="animate-sheetOn bg-BID_BLACK  rounded-2xl text-center p-3 mt-2"
                onClick={() => goToBuyWrite()}
              >
                역경매글 등록
              </button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default SelectWriteModal;
