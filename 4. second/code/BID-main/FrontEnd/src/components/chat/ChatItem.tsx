import { IChatRoomListRes } from '@/types/chat';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Modal from '../@common/Modal';
import { useProfile } from '@/hooks/profile/useProfile';
import Toast from '../@common/Toast';
import { useChatRoom } from '@/hooks/chat/useChat';
import userImage from '@/assets/icon/defaultProfile.png';

const ChatItem = (props: { item: IChatRoomListRes }) => {
  const { chatRoomRes, unReadCount, audienceMemberRes } = props.item;
  const { dealId, lastMessage } = chatRoomRes;
  const { opponentNick } = audienceMemberRes;
  const navigate = useNavigate();
  const [showModal, setShowModal] = useState(false);

  const handleChatItemClick = () => {
    navigate(`/chat/rooms/${dealId}`);
  };
  const { useUserProfile } = useProfile();

  const { data: userInfo } = useUserProfile(opponentNick);

  const { useDeleteChatRoom } = useChatRoom();
  const { deleteChatRoom } = useDeleteChatRoom(dealId);

  // 채팅방 삭제
  const handleDeleteClick = async () => {
    try {
      await deleteChatRoom.mutate();
      Toast.success('구매 확정 후 채팅방을 나갑니다');
    } catch (error) {
      setShowModal(true);
      console.error('채팅방 나가기 에러 -> 모달 안내', error);
    }
  };

  return (
    <>
      <div className="w-full flex px-6 py-3 border-b border-[#D9D9D9]">
        <div
          className="flex justify-between overflow-hidden w-full"
          onClick={handleChatItemClick}
          onContextMenu={e => {
            e.preventDefault();
            handleDeleteClick();
          }}
        >
          <div className=" flex">
            <div className="w-14 h-14">
              {/* TODO: 프로필 사진으로 변경 */}
              {userInfo?.data.profileImage ? (
                <img
                  src={`${import.meta.env.VITE_BASE_URL}${userInfo?.data.profileImage}`}
                  className="w-full h-full rounded-2xl object-cover"
                />
              ) : (
                <img src={userImage} className="w-full h-full object-cover" />
              )}
            </div>
            <div className="flex flex-col justify-center gap-1 px-5">
              <p className="text-sm font-bold">{chatRoomRes.roomName}</p>
              <p className="text-sm">{lastMessage}</p>
            </div>
          </div>
          <div className="flex items-center mx-2">
            {unReadCount > 0 ? (
              <span className="bg-orange-500 text-sm rounded-full h-5 w-5 flex items-center justify-center text-white font-semibold">
                {unReadCount}
              </span>
            ) : null}
          </div>
        </div>
      </div>
      {/* Modal 추가 */}
      {showModal && (
        <Modal width="300px" height="auto" title="채팅방 나가기" onClose={() => setShowModal(false)}>
          <div className="flex flex-col justify-center items-center p-3">
            <p className="font-bold pb-3">구매확정 후에 가능합니다!!</p>
            <p>구매확정은 채팅방 상단에서</p>
          </div>
          <div className="flex justify-center py-4">
            <button className="bg-BID_MAIN text-white px-4 py-2 rounded-lg" onClick={() => setShowModal(false)}>
              확인
            </button>
          </div>
        </Modal>
      )}
    </>
  );
};

export default ChatItem;
