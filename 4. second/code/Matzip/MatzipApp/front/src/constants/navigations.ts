// 여러곳에서 쓰이므로 이렇게 상수화 해줫음.
const authNavigations = {
  AUTH_HOME: 'AuthHome',
  LOGIN: 'Login',
  SIGNUP: 'Signup',
} as const; // 읽기 전용으로 만들려고

export {authNavigations};
