import {useMutation, useQuery} from '@tanstack/react-query';
import {getAccessToken, postLogin, postSignup} from '../../api/auth';
import {UseMutationCustomOptions} from '../../types/common';
import {removeEncryptedStorage, setEncryptStorage} from '../../utils';
import axiosInstance from '../../api/axios';
import {removeHeader, setHeader} from '../../utils/header';
import {useEffect} from 'react';

// Axios를 이용하므로 Error를 ResponseError로 커스텀해줘야 함 (타입이 다르므로)

function useSignup(mutationOptions?: UseMutationCustomOptions) {
  return useMutation({
    mutationFn: postSignup,
    ...mutationOptions,
  });
}

function useLogin(mutationOptions?: UseMutationCustomOptions) {
  return useMutation({
    mutationFn: postLogin,
    onSuccess: ({accessToken, refreshToken}) => {
      setEncryptStorage('refreshToken', refreshToken);
      setHeader('Authorization', `Bearer ${accessToken}`);
    },
    onSettled: () => {},
    ...mutationOptions,
  });
}

function useGetRefreshToken() {
  const {isSuccess, data, isError} = useQuery({
    queryKey: ['auth', 'getAccessToken'],
    queryFn: getAccessToken,
    staleTime: 1000 * 60 * 30 - 1000 * 60 * 3,
    refetchInterval: 1000 * 60 * 30 - 1000 * 60 * 3,
    refetchOnReconnect: true,
    refetchIntervalInBackground: true,
  });

  useEffect(() => {
    if (isSuccess) {
      setHeader('Authorization', `Bearer ${data.accessToken}`);
      setEncryptStorage('refreshToken', data.refreshToken);
    }
  }, [isSuccess]);

  useEffect(() => {
    if (isError) {
      removeHeader('Authorization');
      removeEncryptedStorage('refreshToken');
    }
  }, [isError]);

  return {isSuccess, isError};
}

// onSettled => 성공여부를 신경쓰지 않고 실행.

// 리액트 쿼리는 데이터 fetching을 위한 useQuery와 데이터 update를 위한 useMutation을 제공하는데 이것들을 한번 랩핑하는 커스텀 훅을 만들어주자!

// 이미 첫번째 인자로 mutationFn를 사용하고 있으므로 Omit를 통해 제외해주자
