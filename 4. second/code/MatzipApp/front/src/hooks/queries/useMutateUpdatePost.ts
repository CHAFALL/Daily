import {useMutation} from '@tanstack/react-query';

import {updatePost} from '@/api/post';
import {UseMutationCustomOptions} from '@/types';
import queryClient from '@/api/queryClient';
import {queryKeys} from '@/constants';

function useMutateUpdatePost(mutationOptions?: UseMutationCustomOptions) {
  return useMutation({
    mutationFn: updatePost,
    onSuccess: newPost => {
      queryClient.invalidateQueries({
        queryKey: [queryKeys.POST, queryKeys.GET_POSTS],
      });
      queryClient.invalidateQueries({
        queryKey: [queryKeys.MARKER, queryKeys.GET_MARKERS],
      });

      // 새로운 정보의 post가 그대로 오기 때문에 무효화를 하지 않아도 그냥 캐시 정보를 업데이트 해주면 된다.

      queryClient.setQueryData(
        [queryKeys.POST, queryKeys.GET_POST, newPost.id],
        newPost,
      );
      queryClient.invalidateQueries({
        queryKey: [
          queryKeys.POST,
          queryKeys.GET_CALENDAR_POSTS,
          new Date(newPost.date).getFullYear(),
          new Date(newPost.date).getMonth() + 1,
        ],
      });
    },
    ...mutationOptions,
  });
}

export default useMutateUpdatePost;
