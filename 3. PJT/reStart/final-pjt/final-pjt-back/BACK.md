# Back

## accounts

- accounts/login/
  
  - POST : 로그인

- accounts/logout/
  
  - POST : 로그아웃

- accounts/signup/
  
  - POST : 회원가입

- accounts/profile/\<str:username>/
  
  - GET : 특정 사용자의 팔로워 정보 제공

- accounts/profile/\<str:username>/
  
  - 인증된 사용자만 접근 가능
  
  - POST : 특정 사용자를 팔로우 하거나 팔로우를 취소

## community

- community/
  
  - 인증된 사용자만 접근 가능
  
  - GET : 게시글 목록 제공
  
  - POST : 신규 게시글 작성

- community/\<int:article_pk>/
  
  - 인증된 사용자만 접근 가능
  
  - GET : 상세 게시글 정보 제공
  
  - PUT : 상세 게시글 수정
  
  - DELETE : 상세 게시글 삭제

- community/\<int:article_pk>/like/
  
  - 인증된 사용자만 접근 가능
  
  - GET : 특정 게시글의 좋아요 수와 사용자의 해당 게시글 좋아요 여부 제공
  
  - POST : 해당 게시글에 좋아요 또는 좋아요 취소

- community/\<int:article_pk>/comments/
  
  - 인증된 사용자만 접근 가능
  
  - GET : 특정 게시글에 작성된 댓글 목록 제공
  
  - POST : 특정 게시글에 댓글 작성

- community/\<int:article_pk>/comments/\<int:comment_pk>/
  
  - 인증된 사용자만 접근 가능
  
  - DELETE : 특정 댓글 삭제
  
  - PUT : 특정 댓글 수정

- community/\<int:article_pk>/comments/\<int:comment_pk>/like/
  
  - 인증된 사용자만 접근 가능
  
  - GET : 특정 댓글의 좋아요 수와 사용자의 해당 게시글 좋아요 여부 제공
  
  - POST : 해당 댓글에 좋아요 또는 좋아요 취소

- community/\<int:article_pk>/comments/\<int:comment_pk>/recomment/
  
  - 인증된 사용자만 접근 가능
  
  - GET : 특정 댓글에 작성된 대댓글 목록 제공
  
  - POST : 특정 댓글에 대댓글 작성

- community/\<str:username>/articles/
  
  - GET : 특정 사용자가 작성한 게시글 목록 제공

- community/\<str:username>/comments/
  
  - GET : 특정 사용자가 작성한 댓글 목록 제공

- community/\<str:username>/like/articles/
  
  - GET : 특정 사용자가 좋아요 한 게시글 목록 제공

## movies

- movies/
  
  - GET : 전체 영화 목록 제공

- movies/genres/
  
  - GET : 장르 목록 제공

- movies/recommend/
  
  - 인증된 사용자만 접근 가능
  
  - GET : 추천하는 영화 목록 제공

- movies/genres/\<int:genre_pk>/
  
  - GET : 특정 장르를 포함하는 영화 목록 제공 

- movies/actor/\<int:actor_pk>
  
  - GET : 특정 배우가 출연하는 영화 목록 제공

- movies/search/\<str:word>/
  
  - GET : 특정 문자열이 제목에 포함된 영화 목록 제공

- movies/\<int:movie_pk>/
  
  - GET : 특정 영화의 상세 정보를 제공

- movies/\<int:movie_pk>/actors/
  
  - GET : 특정 영화에 출연하는 배우 목록 제공

- movies/\<int:movie_pk>/like/
  
  - 인증된 사용자만 접근 가능
  
  - POST : 특정 영화에 좋아요 또는 좋아요 취소

- movies/\<int:movie_pk>/scores/
  
  - 인증된 사용자만 접근 가능
  
  - PUT : 영화의 평점 수정

- movies/\<int:movie_pk>/comments/
  
  - 인증된 사용자만 접근 가능
  
  - GET : 특정 영화에 작성된 리뷰 목록 제공
  
  - POST : 특정 영화에 리뷰 작성

- movies/\<int:movie_pk>/comments/\<int:comment_pk>/
  
  - 인증된 사용자만 접근 가능
  
  - PUT : 특정 영화 리뷰 수정
  
  - DELETE : 특정 영화 리뷰 삭제

- movies/\<str:username>/like/movies/
  
  - GET : 특정 사용자가 좋아요 한 영화 목록 제공
