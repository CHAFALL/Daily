/**
 * Pick<T, K>
 * -> 뽑다, 고르다
 * -> 객체 타입으로부터 특정 프로퍼티만 딱 골라내는 그런 타입
 */

interface Post {
  title: string;
  tags: string[];
  content: string;
  thumbnailURL?: string;
}

// 직접 구현하기
type Pick<T, K extends keyof T> = {
  // K extends "title" | "tags" | "content"| "thumbnailURL"
  // "title" | content extends "title" | "tags" | "content"| "thumbnailURL"
  [key in K]: T[key];
};

const legacyPost: Pick<Post, "title" | "content"> = {
  title: "옛날 글",
  content: "옛날 컨텐츠",
};

/**
 * Omit<T, K>
 * -> 생략하다, 빼다
 * -> 객체 타입으로부터 특정 프로퍼티를 제거하는 타입
 */

// 직접 구현하기
type Omit<T, K extends keyof T> = Pick<T, Exclude<keyof T, K>>;
// T = Post, K = "title"
// Pick<Post, Exclude<keyof Post, "title">>
// Pick<Post, Exclude<"title" | "content" | "tags" | "thumbnailURL", "title">>
// Pick<Post, "content" | "tags" | "thumbnailURL">

const noTitlePost: Omit<Post, "title"> = {
  content: "",
  tags: [],
  thumbnailURL: "",
};

/**
 * Record<K, V>
 * 객체 타입을 만들어주는 유틸리티 타입
 */

// 이렇게 똑같은 것을 계속 작성???
// 비효율
type ThumbnailLegacy = {
  large: {
    url: string;
  };
  medium: {
    url: string;
  };
  small: {
    url: string;
  };
  watch: {
    url: string;
  };
};

// 직접 구현하기
// 이게 무슨 타입이 될지는 모르겠는데 적어도 이 타입변수 K에 들어오는 타입은 어떤 객체 타입의 키를 추출해 놓은 유니언 타입이야~
type Record<K extends keyof any, V> = {
  [key in K]: V;
};

type Thumbnail = Record<
  "large" | "medium" | "small" | "watch",
  { url: string; size: number }
>;
