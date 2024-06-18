import {ResponseCalendarPost, getCalendarPosts} from '@/api';
import {queryKeys} from '@/constants';
import {UseQueryCustomOptions} from '@/types';
import {keepPreviousData, useQuery} from '@tanstack/react-query';

function useGetCalendarPosts(
  year: number,
  month: number,
  queryOptions?: UseQueryCustomOptions<ResponseCalendarPost>,
) {
  return useQuery({
    queryFn: () => getCalendarPosts(year, month),
    queryKey: [queryKeys.POST, queryKeys.GET_CALENDAR_POSTS, year, month],
    // (다음 달이나 이전달로 이동을 할 때) 이렇게 캐시되지 않은 날짜를 가져올 때 화면에서 목록이 잠깐 사라지는 깜빡임 현상이 발생하는 것을 해결하는 법! -> 아래와 같이 하면 데이터를 가져오는 동안 이전 데이터를 유지해줌. (페이지 네이션을 구현할 때 특히 유용.)
    placeholderData: keepPreviousData,
    ...queryOptions,
  });
}

export default useGetCalendarPosts;
