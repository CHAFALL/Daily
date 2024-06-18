import axios from 'axios';

import {Platform} from 'react-native';

const axiosInstance = axios.create({
  baseURL:
    Platform.OS === 'android'
      ? 'http://10.0.2.2:3030'
      : 'http://localhost:3030',

  withCredentials: true,
});

export default axiosInstance;

// withCredentials: true 옵션은 axios 요청 시에 쿠키나 인증 헤더와 같은 자격 증명을 현재 도메인과 다른 도메인으로의 요청에 포함시키는 설정입니다. 즉, CORS (Cross-Origin Resource Sharing) 상황에서 요청과 함께 쿠키나 인증 토큰을 전송할 수 있도록 해줍니다.
