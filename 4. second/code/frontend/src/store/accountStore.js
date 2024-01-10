// store/accountStore.js

import authStore from '@/store/authStore'; // authStore 모듈을 가져옴
import { requestLogin } from '../common/api/accountAPI';

const state = {
  token: null,
};

const getters = {
  getToken: (state) => {
    return state.token;
  },
};

const mutations = {
  setToken: (state, token) => {
    state.token = token;
    localStorage.setItem('accessToken', token); // 토큰을 localStorage에 저장

    // authStore 모듈의 checkUserToken 액션을 호출
    authStore.actions.checkUserToken({ commit: authStore.commit, state: authStore.state, rootState: authStore.rootState });
  },
};

const actions = {
  loginAction: async ({ commit }, loginData) => {
    const response = await requestLogin(loginData);
    commit('setToken', response.data.accessToken);
  },
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
