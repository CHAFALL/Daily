import Toast from '@/components/@common/Toast';
import { checkTimeStamp, endPurchaseLive, endRecording, matchLive, startRecording } from '@/service/live/api';
import { useMutation } from '@tanstack/react-query';
import { IMatchReq, IRecordReq, ITimeStampReq } from './../../types/live';

export const useLive = () => {
  // 역경매 라이브 매칭
  const usePostLiveMatch = () => {
    return useMutation({
      mutationKey: ['match'],
      mutationFn: ({ dealId, formId, offerPrice }: IMatchReq) => matchLive({ dealId, formId, offerPrice }),
    });
  };

  // 녹화 시작
  const useStartLiveRecord = (dealId: string) => {
    return useMutation({
      mutationKey: ['recording', 'start', dealId],
      mutationFn: ({ userId, dealId }: IRecordReq) => startRecording({ userId, dealId }),
      onSuccess: () => {
        Toast.success('녹화를 시작합니다.');
      },
      onError: () => {
        Toast.error('녹화를 실패했습니다.');
      },
    });
  };

  // 녹화 종료
  const useEndLiveRecord = (dealId: string) => {
    return useMutation({
      mutationKey: ['recording', 'end', dealId],
      mutationFn: ({ userId, dealId }: IRecordReq) => endRecording({ userId, dealId }),
      onSuccess: () => {
        Toast.success('녹화를 종료합니다.');
      },
      onError: () => {
        Toast.error('녹화를 실패했습니다.');
      },
    });
  };

  // 타임라인
  const useTimeStamp = () => {
    return useMutation({
      mutationKey: ['timeStamp'],
      mutationFn: ({ step, dealId }: ITimeStampReq) => checkTimeStamp({ step, dealId }),
    });
  };

  // 역경매 종료
  const useEndPurchaseLive = () => {
    return useMutation({
      mutationKey: ['purchase'],
      mutationFn: (dealId: string) => endPurchaseLive(dealId),
    });
  };

  return { usePostLiveMatch, useStartLiveRecord, useEndLiveRecord, useTimeStamp, useEndPurchaseLive };
};
