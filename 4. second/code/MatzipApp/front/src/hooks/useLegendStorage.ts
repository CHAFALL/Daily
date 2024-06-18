// 상태를 스토리지에 저장해서 앱을 껐다 켜도 상태가 유지되도록 하자!!!!!

import {storageKeys} from '@/constants';
import useLegendStore from '@/store/useLegendStore';
import {getEncryptStorage, setEncryptStorage} from '@/utils';
import {useEffect} from 'react';

function useLegendStorage() {
  const {isVisible, setIsVisible} = useLegendStore();

  const set = async (flag: boolean) => {
    await setEncryptStorage(storageKeys.SHOW_LEGEND, flag);
    setIsVisible(flag);
  };

  useEffect(() => {
    (async () => {
      const storedData =
        (await getEncryptStorage(storageKeys.SHOW_LEGEND)) ?? false;
      setIsVisible(storedData);
    })();
  }, [setIsVisible]);

  return {set, isVisible};
}

export default useLegendStorage;
