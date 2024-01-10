// services/api.js

import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8080/api/v1', // API 엔드포인트의 기본 URL
  // 다른 Axios 설정들...
});

export { api };
