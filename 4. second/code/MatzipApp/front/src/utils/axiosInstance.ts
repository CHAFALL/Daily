import axiosInstance from '@/api/axios';

function setHeader(key: string, value: string) {
  axiosInstance.defaults.headers.common[key] = value;
}

function removeHeader(key: string) {
  if (!axiosInstance.defaults.headers.common[key]) {
    return;
  }

  delete axiosInstance.defaults.headers.common[key];
}

export {setHeader, removeHeader};

// axiosInstance.defaults.headers.common['Authorization'] = accessToken; => 이렇게 해주면 앞으로의 요청에 일일이 헤더를 설정해주지 않고 디폴트로 헤더가 들어감.
