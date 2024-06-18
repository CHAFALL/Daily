import {LatLng, MapMarkerProps} from 'react-native-maps';

declare module 'react-native-maps' {
  export interface MyMapMarkerProps extends MapMarkerProps {
    coordinate?: LatLng;
  }
}

// 타입 재 정의
