import {QueryClient} from '@tanstack/react-query';

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      retry: false,
    },
    mutations: {
      retry: false,
    },
  },
});

export default queryClient;

//리액트 쿼리는 요청이 실패하면 기본적으로 3번 재요청을 하게 되는데 이걸 모두 하지 않는 방식으로 변환

// export default를 사용하면, 모듈을 임포트할 때 특정한 이름을 사용하지 않고도 해당 항목을 불러올 수 있습니다.

//export default의 특징:
// 1. 단 하나의 기본 내보내기만 허용: 각 모듈은 하나의 default 내보내기만 가질 수 있습니다. 이는 그 모듈의 '주' 내보내기로 간주될 수 있습니다.
// 2. 임의의 이름으로 임포트 가능: default로 내보낸 항목은 임포트할 때 어떤 이름을 사용하여도 괜찮습니다. 즉, 내보내는 측에서 정한 이름을 따를 필요가 없습니다.
