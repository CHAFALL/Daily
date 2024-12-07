import Modal from '@/components/@common/Modal';
import PointChargeModal from '@/components/@common/PointChargeModal';
import { useSale } from '@/hooks/home/useSale';
import { useProfile } from '@/hooks/profile/useProfile';
import useLiveStore from '@/stores/userLiveStore';
import userStore from '@/stores/userStore';
import { ISaleDetailRes } from '@/types/home';
import { getDate } from '@/utils/getDate';
import { useState } from 'react';
import { HiHeart, HiOutlineHeart } from 'react-icons/hi';
import { MdLiveTv } from 'react-icons/md';
import { useNavigate } from 'react-router-dom';

const DetailBottom = (props: { info: ISaleDetailRes; isSeller: boolean }) => {
  const { useUserProfile } = useProfile();
  const { nickname } = userStore();
  const { status, isWished, highestBid, startPrice, dealRes, immediatePrice } = props.info;
  const isSeller = props.isSeller;
  const [showBidModal, setShowBidModal] = useState<boolean>(false);
  const [showImmediateModal, setShowImmediateModal] = useState<boolean>(false);
  const [bidPrice, setBidPrice] = useState<string>('');
  const { usePostSaleBid, usePostSaleImmediate, usePostDealWishAdd, useDeleteDealWish } = useSale();
  const { mutate: bidMuate } = usePostSaleBid(dealRes.id, bidPrice, nickname);
  const { mutate: immediateMuate } = usePostSaleImmediate(dealRes.id);
  const { mutate: wishAddMuate } = usePostDealWishAdd(dealRes.id);
  const { mutate: wishDeleteMuate } = useDeleteDealWish(dealRes.id);

  const { data: userProfileInfo } = useUserProfile(nickname);
  const navigate = useNavigate();
  const { setTType, setPType } = useLiveStore();

  const handleBtnClick = () => {
    if (status === 'BEFORE') {
      setShowImmediateModal(true);
    } else if (status === 'END') {
      return;
    } else {
      setShowBidModal(true);
    }
  };

  // #TODO 라이브방 진입하는 함수
  const approachLive = () => {
    setTType('sale');
    setPType(isSeller ? 'seller' : 'buyer');

    // 판매자 로직
    if (isSeller) {
      if (status !== 'END') {
        navigate(`/live/sale/${dealRes.id}`, {
          state: {
            title: dealRes.title,
            startPrice: startPrice,
            startTime: getDate(dealRes.startTime).fullDate3,
          },
        });
      }
    }
  };
  const [showChargeModal, setShowChargeModal] = useState<boolean>(false);

  const goToChatRoom = () => {
    navigate(`/chat/rooms/${dealRes.id}`);
  };

  const checkBtn = () => {
    if (isSeller) {
      if (status === 'BEFORE' || status === 'LIVE' || status === 'AUCTION') {
        return (
          <button
            onClick={() => approachLive()}
            className="w-full py-3 text-red-500 rounded-xl text-center text-sm border-red-500 border flex justify-center items-center"
          >
            <MdLiveTv size={'16px'} color="red" />
            &nbsp;&nbsp;
            <p className=" text-red-500 ">라이브 시작하기</p>
          </button>
        );
      } else if (status === 'END') {
        return (
          <div className="w-full border rounded-xl text-md bg-BID_BLACK flex p-2 justify-center items-center gap-2">
            <p className=" text-white ">이미 종료된 경매입니다</p>
          </div>
        );
      }
    } else {
      if (status === 'BEFORE') {
        return (
          <button
            onClick={handleBtnClick}
            className={`w-full py-3 text-white rounded-xl text-center text-md bg-BID_MAIN`}
          >
            즉시 구매하기
          </button>
        );
      } else if (status === 'LIVE' || status === 'AUCTION') {
        return (
          <button
            onClick={handleBtnClick}
            className="w-full py-3  text-white rounded-xl text-center text-md bg-BID_MAIN"
          >
            입찰하기
          </button>
        );
      } else if (status === 'END') {
        return (
          <div className="w-full border rounded-xl text-md bg-BID_BLACK font-bold flex p-3 justify-center items-center gap-2-">
            <p className=" text-white ">이미 종료된 경매입니다</p>
          </div>
        );
      }
    }
  };

  return (
    <>
      {/* 입찰하기 모달 */}
      {showBidModal && (
        <Modal width="300px" height="auto" title="입찰하기" onClose={() => setShowBidModal(false)}>
          <div className="w-full flex flex-col justify-center items-center p-3 px-10">
            <div className="w-full flex gap-3">
              <p className="">현재 최고가</p>
              <p className="text-BID_MAIN">{highestBid === 0 ? startPrice : highestBid}원</p>
              <p className=""></p>
            </div>
            <div className="w-full flex gap-3 items-center">
              <p className="">내 포인트</p>
              <p className="text-BID_MAIN">{userProfileInfo?.data.point}원</p>
              <span onClick={() => setShowChargeModal(true)} className="text-BID_SUB_GRAY border-b text-xs">
                충전하기
              </span>
            </div>
            <div className="w-full pt-3">
              <input
                type="text"
                value={bidPrice}
                onChange={e => setBidPrice(e.target.value)}
                placeholder="입찰가를 입력해주세요"
                className="w-full outline-none border p-2 text-sm rounded-xl"
              />
            </div>
            <div className="w-full flex gap-5 py-4">
              <button
                className="w-full bg-BID_SUB_GRAY text-white px-4 py-2 rounded-2xl"
                onClick={() => setShowBidModal(false)}
              >
                취소
              </button>
              <button
                className="w-full bg-BID_MAIN text-white px-4 py-2 rounded-2xl"
                onClick={() => {
                  bidMuate();
                  setShowBidModal(false);
                }}
              >
                확인
              </button>
            </div>
          </div>
        </Modal>
      )}
      {/* 구매하기 모달 */}
      {showImmediateModal && (
        <Modal width="300px" height="auto" title="구매하기" onClose={() => setShowImmediateModal(false)}>
          <div className="w-full flex flex-col justify-center items-center p-3 px-10">
            <div className="w-full flex gap-3">
              <p className="">즉시 구매가</p>
              <p className="text-BID_MAIN">{highestBid === 0 ? immediatePrice : highestBid}원</p>
              <p className=""></p>
            </div>
            <div className="w-full flex gap-3 items-center">
              <p className="">내 포인트</p>
              {/* 내포인트 조회해야함 */}
              <p className="text-BID_MAIN">{userProfileInfo?.data.point}</p>
              <span onClick={() => setShowChargeModal(true)} className="text-BID_SUB_GRAY border-b text-xs">
                충전하기
              </span>
            </div>
            <div className="w-full flex gap-5 py-4">
              <button
                className="w-full bg-BID_SUB_GRAY text-white px-4 py-2 rounded-2xl"
                onClick={() => setShowImmediateModal(false)}
              >
                취소
              </button>
              <button
                className="w-full bg-BID_MAIN text-white px-4 py-2 rounded-2xl"
                onClick={() => {
                  immediateMuate();
                  setShowImmediateModal(false);
                  goToChatRoom();
                }}
              >
                확인
              </button>
            </div>
          </div>
        </Modal>
      )}
      {/* 포인트 충전 모달 */}
      {showChargeModal && (
        <PointChargeModal setShowChargeModal={setShowChargeModal} userProfileInfo={userProfileInfo?.data} />
      )}
      <div className="fixed px-4 bottom-0 w-full h-[4rem] bg-white z-10 text-[#A9A9A9] text-sm max-w-[500px]">
        <div className="w-full h-full py-2 flex items-center gap-3">
          {isWished ? (
            <HiHeart onClick={() => wishDeleteMuate()} size={'2rem'} color="#FF0000" />
          ) : (
            <HiOutlineHeart onClick={() => wishAddMuate()} size={'2rem'} color="#ababab" />
          )}
          {checkBtn()}
        </div>
      </div>
    </>
  );
};

export default DetailBottom;

/* BEFORE -> 즉시 구매하기
   END -> 이미 종료된 경매입니다
   나머지 -> 입찰하기
*/
