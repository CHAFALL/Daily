import {createPost} from '@/api';
import queryClient from '@/api/queryClient';
import {queryKeys} from '@/constants';
import {UseMutationCustomOptions} from '@/types/common';
import {Marker} from '@/types/domain';
import {useMutation} from '@tanstack/react-query';

function useMutateCreatePost(mutationOptions?: UseMutationCustomOptions) {
  return useMutation({
    mutationFn: createPost,
    onSuccess: newPost => {
      queryClient.invalidateQueries({
        queryKey: [queryKeys.POST, queryKeys.GET_POSTS],
      });
      queryClient.invalidateQueries({
        queryKey: [
          queryKeys.POST,
          queryKeys.GET_CALENDAR_POSTS,
          new Date(newPost.date).getFullYear(),
          new Date(newPost.date).getMonth() + 1,
        ],
      });
      queryClient.setQueryData<Marker[]>(
        [queryKeys.MARKER, queryKeys.GET_MARKERS],
        existingMarkers => {
          const newMarker = {
            id: newPost.id,
            latitude: newPost.latitude,
            longitude: newPost.longitude,
            color: newPost.color,
            score: newPost.score,
          };
          return existingMarkers
            ? [...existingMarkers, newMarker]
            : [newMarker];
        },
      );
    },
    ...mutationOptions,
  });
}

// 이렇게 상태를 업데이트해주는 방법은 쿼리를 무효화하는 방법 말고도 캐시를 직접 업데이트 하는 방법도 있다.

// 이렇게 서버에서 리스폰스로 데이터를 보내주고 있다면 그걸 이용해서 캐시를 직접 업데이트 함으로써 네트워크 요청을 줄이는 장점이 있다. 그런데 상황에 따라 쿼리를 무효화해서 다시 상태를 업데이트 시켜주는 방법이 나을 때도 있다.

// 이렇게 해주면 어떤 장소를 추가했을 때 이 마커를 가져오는 쿼리가 무효화되면서 마커가 바로 표시됨.
// 무효화된 쿼리는 다음번에 활성화되거나 refetch를 호출할 때 자동으로 다시 데이터 패칭을 시도하게 됩니다.
// 무효화된 쿼리는 React Query가 다음번에 데이터를 사용할 때(즉, 쿼리가 활성화될 때) 데이터를 다시 가져오도록 트리거합니다.
// 쿼리를 무효화하면 React Query가 자동으로 데이터를 다시 가져오도록 관리하므로, 개발자는 복잡한 데이터 갱신 로직을 직접 구현할 필요가 없습니다. 이는 코드의 간결성을 높이고 유지보수를 쉽게 만듭니다.

export default useMutateCreatePost;
