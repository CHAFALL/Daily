import Header, { IHeaderInfo } from '@/components/@common/Header';
import ProfileTabBar from '@/components/profile/ProfileTabBar';
import BuyHost from '@/components/profile/buy/BuyHost';
import BuyParticipant from '@/components/profile/buy/BuyParticipant';
import useTabStore from '@/stores/auctionTabStore';
import { IoIosArrowBack } from 'react-icons/io';

const ProfileBuyPage = () => {
  const info: IHeaderInfo = {
    left: <IoIosArrowBack />,
    center: '내 역경매 내역',
    right_1: null,
    right_2: null,
  };

  const { tab } = useTabStore();

  return (
    <>
      <div>
        <Header info={info} />
        <ProfileTabBar leftTab="내가 주최한 역경매" rightTab="내가 참여한 역경매" />
        {/* 탭에 따른 컴포넌트 보여주기 */}
        {tab === 'sale' ? <BuyHost></BuyHost> : <BuyParticipant></BuyParticipant>}
      </div>
    </>
  );
};
export default ProfileBuyPage;
