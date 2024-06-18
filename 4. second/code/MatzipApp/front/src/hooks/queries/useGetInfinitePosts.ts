import {ResponsePost, getPosts} from '@/api';
import {queryKeys} from '@/constants';
import {ResponseError} from '@/types';
import {
  InfiniteData,
  QueryKey,
  UseInfiniteQueryOptions,
  useSuspenseInfiniteQuery,
} from '@tanstack/react-query';

function useGetInfinitePosts(
  queryOptions?: UseInfiniteQueryOptions<
    ResponsePost[],
    ResponseError,
    InfiniteData<ResponsePost[], number>,
    ResponsePost[],
    QueryKey,
    number
  >,
) {
  return useSuspenseInfiniteQuery({
    queryFn: ({pageParam}) => getPosts(pageParam),
    queryKey: [queryKeys.POST, queryKeys.GET_POSTS],
    initialPageParam: 1,
    getNextPageParam: (lastPage, allPages) => {
      const lastPost = lastPage[lastPage.length - 1];
      return lastPost ? allPages.length + 1 : undefined;
    },
    ...queryOptions,
  });
}

export default useGetInfinitePosts;

// Suspense -> 로딩 처리가 필욯ㄴ 컴포넌트에 선언적으로 코드를 작성 가능, 부모 컴포넌트에서 비동기 데이터를 fetching하는 자식 컴포넌트를 suspense로 감싸주면 된다.
// FeedHomeScreen으로 고고고

// 참고 ) select는 반환값을 변환해 줄 수 있는 기능.

//ErrorBoundary -> 에러경계는 하위 컴포넌트 어디에서든 에러를 기록하며 깨진 컴포넌트 트리 대신 폴백 UI를 보여주는 React 컴포넌트

// useInfiniteQuery는 useQuery와 비슷하지만 페이징 기능이 추가된 쿼리느낌

// queryKey
// 이 키는 react-query가 캐시를 관리하는 데 사용됩니다. queryKey는 데이터를 식별하는 고유한 키로 사용됩니다. 여기서는 [queryKeys.POST, queryKeys.GET_POSTS]라는 배열이 키로 사용됩니다.
// queryKey는 동일한 데이터를 여러 곳에서 요청할 때 중복 요청을 방지하고, 캐시된 데이터를 재사용할 수 있게 해줍니다. 즉, queryKey가 같으면 동일한 데이터로 인식하여 효율적으로 데이터를 관리합니다.
