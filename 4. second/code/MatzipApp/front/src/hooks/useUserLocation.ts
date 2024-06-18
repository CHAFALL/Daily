import {useEffect, useState} from 'react';
import {LatLng} from 'react-native-maps';
import GeoLocation from '@react-native-community/geolocation';
import useAppState from './useAppState';

function useUserLocation() {
  // 만약에 사용자가 현재 위치의 권한을 허용하지 않았을 시를 대비하여 초기값 설정
  const [userLocation, setUserLocation] = useState<LatLng>({
    latitude: 37.5516032365118,
    longitude: 126.98989626020192,
  });
  const [isUserLocationError, setIsUserLocationError] = useState(false);
  const {isComeback} = useAppState();

  // console.log('isComeback', isComeback);

  useEffect(() => {
    GeoLocation.getCurrentPosition(
      info => {
        const {latitude, longitude} = info.coords;
        setUserLocation({latitude, longitude});
        setIsUserLocationError(false);
      },
      () => {
        setIsUserLocationError(true);
      },
      {
        enableHighAccuracy: true,
      },
    );
  }, [isComeback]);

  return {userLocation, isUserLocationError};
}

// 사용자가 권한을 허용하고 돌아왔는데 그걸 판단해주는 것이 없다.
// 그 상태를 체크할 수 있는 기능을 추가 필요.
// React Native엣는 앱에 백그라운드 상태에 갔다가 다시 앱으로 돌아올 때 상태를 체크할 수 있는 기능 제공 -> AppState

export default useUserLocation;
