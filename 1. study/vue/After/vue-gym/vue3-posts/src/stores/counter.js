import { defineStore } from 'pinia';

export const useCounterStore = defineStore('counter', {
	state: () => ({
		counter: 1,
	}),
	getters: {
		doubleCount: state => state.counter * 2,
		doubleCountPlusOne() {
			return this.doubleCount + 1;
		},
	},
	actions: {
		increment() {
			this.counter++;
		},
	},
});

// 여기서 increment는 화살표 함수를 정의하지 않은 이유가 화살표 함수를 정의하게 되면 store 인스턴스에 접근 불가, (this를 사용할 때는 상위 스코프의 this 영향을 받기 때문에)
