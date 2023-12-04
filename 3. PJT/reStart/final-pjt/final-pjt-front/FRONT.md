# App.vue

## SignUpView

- 인증된 사용자는 접근 불가

- 경로 : /signup

- 회원 가입

## LoginView

- 인증된 사용자는 접근 불가

- 경로 : /login

- 로그인

## MovieListView

- 경로 : /
- 기본 페이지
- 전체 영화 목록, 검색 기능 제공

#### MovieGenreList

- 라우터 기능을 포함한 장르별 버튼 구현

## MovieGenreView

- 경로 : /genres/:id
- 장르별 영화 목록 제공

## ActorView

- 경로 : /actor/:id
- 각 배우 별 프로필 사진 및 해당 배우가 출현한 영화 목록 제공

#### MovieList

- MovueListView, MovieGenreView, ActorView 모두가 사용하는 컴포넌트

- 영화 목록 컴포넌트

###### MovieListItem

- 영화 목록의 개별 항목 컴포넌트

## MovieDetailView

- 경로 : /movies/:id
- 특정 영화의 상세 정보 제공

#### MovieDetail

- 영화 상세 정보 컴포넌트

###### MovieDetailComment

- 영화에 작성된 리뷰 작성 및 목록 컴포넌트

- **MovieDetailCommentItem**
  
  - 리뷰 목록 개별 항목 컴포넌트

###### MovieDetailActors

- 영화에 출연한 배우 목록 컴포넌트

- **MovieDetailActorsItem**
  
  - 출연 배우 목록 개별 항목 컴포넌트

###### MovieDetailModal

- 영화 예고편 모달 컴포넌트

## RecommendedView

- 인증된 사용자만 접근 가능

- 경로 : /recommended

- 추천하는 영화 (평점순, 리뷰가 많은 순, 선호하는 장르) 목록 제공

#### MovieRecommendList

- 추천하는 영화 목록 컴포넌트

## CommunityListView

- 인증된 사용자만 접근 가능

- 경로 : /articles

- 게시글 목록 제공

#### ArticleList

- 게시글 목록 컴포넌트

###### ArticleListItem

- 게시글 목록 개별 항목 컴포넌트

## ArticleDetailView

- 인증된 사용자만 접근 가능

- 경로 : /articles/:id

- 상세 게시글 제공

#### ArticleDetail

- 상세 게시글 정보 제공 컴포넌트

###### ArticleDetailComment

- 특정 게시글의 댓글 작성 및 목록을 제공하는 컴포넌트

- **ArticleDetailCommentItem**
  
  - 댓글 목록의 개별 항목 컴포넌트
  
  - 댓글 수정 및 삭제 기능 포함
  
  - **ArticleDetailCommentRecomment**
    
    - 개별 댓글의 대댓글 작성 및 목록을 제공하는 컴포넌트
    
    - **ArticleDetailCommentRecommentItem**
      
      - 대댓글 목록의 개별 항목 컴포넌트
      
      - 댓글 수정 및 삭제 기능 포함

## ArticleCreateView

- 인증된 사용자만 접근 가능

- 경로 : /articles/create

- 게시글 작성

## ArticleUpdateView

- 인증된 사용자만 접근 가능

- 경로 : /articles/:id/update

- 게시글 수정

## UserDetailView

- 인증된 사용자만 접근 가능

- 경로 : /profile/:username

- 특정 사용자의 상세 정보 제공

#### UserFollowing

- 사용자가 팔로우하는 사용자들을 제공하는 컴포넌트

#### UserFollower

- 사용자를 팔로우하는 사람들을 제공하는 컴포넌트

#### UserArticles

- 사용자가 작성한 게시글 목록을 제공하는 컴포넌트

#### UserComments

- 사용자가 작성한 댓글 목록을 제공하는 컴포넌트

#### UserLikeArticles

- 사용자가 좋아요 한 게시글 목록을 제공하는 컴포넌트

###### UserLikeArticleItem

- 좋아요 한 게시글 목록 개별 항목 컴포넌트

#### UserLikeMovies

- 사용자가 좋아요 한 영화 목록을 제공하는 컴포넌트

###### UserLikeMovieItem

- 좋아요 한 영화 목록 개별 항목 컴포넌트

## EasterEggView

- 경로 : /meow
- 이스터에그
