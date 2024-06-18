import { createParamDecorator, ExecutionContext } from '@nestjs/common';

// 1: 커스텀 데코레이터가 받는 데이터, 2: ExecutionContext (현재 실행 중인 컨텍스트에 대한 정보를 제공합니다.)
// switchToHttp().getRequest()를 사용하여 HTTP 요청 객체를 가져옵니다.
export const GetUser = createParamDecorator((_, ctx: ExecutionContext) => {
  const request = ctx.switchToHttp().getRequest();

  return request.user;
});

// 클라이언트에서 헤더에 토큰을 넣어주면 유저 정보 처리 가능하게 하기 위해 HTTP 요청 객체를 가져옵니다.
