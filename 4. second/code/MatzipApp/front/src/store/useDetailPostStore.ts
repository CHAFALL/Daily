import {ResponsePost} from '@/api';
import {create} from 'zustand';

interface DetailPostState {
  detailPost: ResponsePost | null;
  setDetailPost: (detailPost: ResponsePost) => void;
}

const useDetailStore = create<DetailPostState>(set => ({
  detailPost: null,
  setDetailPost: (detailPost: ResponsePost) => {
    set({detailPost});
  },
}));

export default useDetailStore;

// 수정 기능을 위해서 정보를 상태에 담아뒀다가 수정 화면에서 사용하기 위함.
