// store/authStore.js

import { api } from '@/services/api';
import router from '@/common/lib/vue-router'; // Vue Router 인스턴스 가져오기

const state = {
  token: null,
  user: null,
  isLoggedIn: false,
};

const mutations = {
  setToken(state, token) {
    state.token = token;
  },
  setUser(state, user) {
    state.user = user;
  },
  setLoggedIn(state, isLoggedIn) {
    state.isLoggedIn = isLoggedIn;
  },
  resetAuthState(state) {
    state.token = null;
    state.user = null;
    state.isLoggedIn = false;
  },
};

const actions = {
  async checkUserToken({ commit, dispatch }) {
    try {
      console.log("야호")
      const token = localStorage.getItem('accessToken');
      if (!token) {
        commit('setToken', null);
        commit('setUser', null);
        commit('setLoggedIn', false);

        return;
      }

      const response = await api.get('/users/me', {
        headers: { 'Authorization': `Bearer ${token}` },
      });

      const userData = response.data;
      commit('setToken', token);
      commit('setUser', userData);
      commit('setLoggedIn', true);


    } catch (error) {
      dispatch('handleAxiosError', error);
    }
  },

  handleAxiosError({ commit, dispatch }, error) {
    if (error.response) {
      const statusCode = error.response.status;

      switch (statusCode) {
        case 401:
          dispatch('handleUnauthorizedError', error.response.data.message);
          break;
        case 403:
          dispatch('handleForbiddenError');
          break;
        // 다른 상태코드에 대한 처리
        // ...
        default:
          console.error(`Unexpected error: ${statusCode}`);
      }
    } else {
      console.error('Network error');
    }
  },

  handleUnauthorizedError({ commit, dispatch }, errorMessage) {
    if (errorMessage.includes('SignatureVerificationException') || errorMessage.includes('JWTDecodeException')) {
      showPopupMessage(commit, '세션이 유효하지 않습니다.');
      dispatch('handleLogout');
    } else if (errorMessage.includes('TokenExpiredException')) {
      showPopupMessage(commit, '세션이 만료되었습니다.');
      dispatch('handleLogout');
    } else {
      // 다른 401 에러에 대한 처리
      // ...
    }
  },

  handleForbiddenError({ commit }) {
    showPopupMessage(commit, '접근 권한이 없습니다.');
  },

  showPopupMessage({ commit }, message) {
    alert(message);
  },

  handleLogout({ commit }) {

    // 로컬 스토리지에서 토큰 제거
    localStorage.removeItem('accessToken');
    commit('resetAuthState');


    // 리다이렉트를 홈 화면으로 수행
    router.push({ name: 'home' });
  },

  // 다른 기능 추가 가능
};

const getters = {
  getToken: (state) => state.token,
  getUser: (state) => state.user,
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
};
