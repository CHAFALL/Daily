import userStore from "@/stores/userStore";
import { IChatResList } from "@/types/chat";
import { formatDateTime } from "@/utils/formatDateTime";
import { useEffect, useRef } from "react";

const ChatLogs = (props: { chatResList: IChatResList } ) => {

  const { message, senderId, createTime  } = props.chatResList
  const { userId } = userStore()

  // 마지막 내용 바로 보여주기
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (messagesEndRef.current) {
      messagesEndRef.current.scrollIntoView();
    }
  });

  return (
    <div className="w-full flex flex-col space-y-2 flex-nowrap overflow-x-auto">
        <div
          
          className={`flex ${senderId !== userId ? "justify-start" : "justify-end"}`}
        >
          <div className="flex items-end">
            {senderId !== userId ? (
              <>
                <p className="bg-gray-200 text-sm rounded-lg px-3 py-2">{`${message}`}</p>
                <p className="text-xs text-gray-400 ml-2">{`${formatDateTime(createTime.toString())}`}</p>
              </>
            ) : (
              <>
                <p className="text-xs text-gray-400 mr-2">{`${formatDateTime(createTime.toString())}`}</p>
                <p className="bg-BID_MAIN text-white text-sm rounded-lg px-3 py-2">{message}</p>
              </>
            )}
          </div>
        </div>
      <div ref={messagesEndRef} />
    </div>
  );
};

export default ChatLogs;
