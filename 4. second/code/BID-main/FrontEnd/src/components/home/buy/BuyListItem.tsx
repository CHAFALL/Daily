import { IPurchaseSimpleRes } from '@/types/home';
import { changeEngToKr } from '@/utils/changeCategorie';
import { getDate } from '@/utils/getDate';
import { useNavigate } from 'react-router-dom';

const BuyListItem = (props: { item: IPurchaseSimpleRes }) => {
  const navigate = useNavigate();

  const { id, category, title, startTime, image } = props.item.dealSimpleRes;

  const { month, date, datOfWeek, time } = getDate(startTime);

  return (
    <div onClick={() => navigate(`/buy/detail/${id}`)} className="text-xs cursor-pointer">
      <div className="w-28 h-28 relative">
        <img src={`${import.meta.env.VITE_BASE_URL}${image}`} className="w-full h-full rounded-lg object-cover" />
        <div className="absolute flex flex-col justify-center items-center rounded-md top-0 left-0 right-0 bottom-0 text-center bg-black/15">
          <p className="text-white font-bold text-md whitespace-nowrap">
            {month}/{date} ({datOfWeek})
          </p>
          <p className="text-white font-bold text-xl">{time}</p>
        </div>
      </div>
      <div className="px-1 flex flex-col gap-1">
        <p className="text-[0.6rem] text-BID_SUB_GRAY pt-1">{changeEngToKr(category)}</p>
        <p className="w-28 truncate whitespace-normal line-clamp-2">{title}</p>
      </div>
    </div>
  );
};

export default BuyListItem;
