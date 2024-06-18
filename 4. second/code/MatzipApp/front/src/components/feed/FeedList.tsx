import React, {useState} from 'react';
import {FlatList, StyleSheet} from 'react-native';
import useGetInfinitePosts from '@/hooks/queries/useGetInfinitePosts';
import FeedItem from './FeedItem';

function FeedList() {
  const {
    data: posts,
    fetchNextPage,
    hasNextPage,
    isFetchingNextPage,
    refetch,
  } = useGetInfinitePosts();
  const [isRefreshing, setIsRefreshing] = useState(false);

  const handleRefresh = async () => {
    setIsRefreshing(true);
    await refetch();
    setIsRefreshing(false);
  };

  const handleEndReached = () => {
    if (hasNextPage && !isFetchingNextPage) {
      fetchNextPage();
    }
  };

  return (
    <FlatList
      data={posts?.pages.flat()}
      renderItem={({item}) => <FeedItem post={item} />}
      keyExtractor={item => String(item.id)}
      numColumns={2}
      contentContainerStyle={styles.contentContainer}
      onEndReached={handleEndReached}
      onEndReachedThreshold={0.5}
      refreshing={isRefreshing}
      onRefresh={handleRefresh}
      scrollIndicatorInsets={{right: 1}}
      indicatorStyle="black"
    />
  );
}

const styles = StyleSheet.create({
  contentContainer: {
    padding: 15,
  },
});

export default FeedList;

// flat() -> 1단계 배열로 만들어줌.
// keyExtractor -> 키 지정
// numColumns={2} -> 열 하나에 2개의 데이터 표시
//  refreshing, onRefresh : 새로고침 기능
// scrollIndicatorInsets={{right: 1}} : 스크롤바 버그 방지

//FlatList는 데이터의 길이가 정해져 있지 않고 많은 양의 데이터를 표시할 때 적합
// 그래서 데이터의 길이가 가변적이면서 이렇게 서버에서 가져오는 데이터를 많이 표시해 줄 때 이용.

// 스크롤 뷰로 표현이 가능은 하지만 스크롤 뷰 같은 경우는 데이터의 길이가 많지 않고 고정적인 길이를 표시할 때 사용해 주면 좋다.
