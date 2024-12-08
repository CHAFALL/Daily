import useOtherTabStore from '@/stores/profileOtherTab';
import React from 'react';

interface ProfileTabBarProps {
  leftTab: string;
  middleTab: string;
  rightTab: string;
}

const ProfileOtherTabBar: React.FC<ProfileTabBarProps> = ({ leftTab, middleTab, rightTab }) => {
  const { tab, setTab } = useOtherTabStore();

  return (
    <>
      <div className="w-full flex relative pb-2 text-center max-w-[500px]">
        <button
          onClick={() => setTab('review')}
          className={tab === 'review' ? ' font-bold flex-1 text-BID_MAIN' : 'text-gray-400 flex-1'}
        >
          <p>{leftTab}</p>
        </button>
        <button
          onClick={() => setTab('sale')}
          className={tab === 'sale' ? ' font-bold flex-1 text-BID_MAIN' : 'text-gray-400 flex-1'}
        >
          <p>{middleTab}</p>
        </button>
        <button
          onClick={() => setTab('buy')}
          className={tab === 'buy' ? ' font-bold flex-1 text-BID_MAIN' : 'text-gray-400 flex-1'}
        >
          <p>{rightTab}</p>
        </button>
        <button className="absolute bottom-0 left-0 w-full h-[1px] bg-gray-300">
          <div
            className={`${
              tab === 'review' ? 'left-0' : tab === 'sale' ? 'left-1/3' : 'left-2/3'
            } duration-500 ease-in-out relative bottom-[2px] z-10 w-1/3 h-[3px] bg-BID_MAIN`}
          ></div>
        </button>
      </div>
    </>
  );
};

export default ProfileOtherTabBar;
