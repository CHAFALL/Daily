import { computed, unref } from 'vue';

// 보면 반응형으로 만들다 보니 그 ref로 넘어가게 되어 unref를 넣어줘야 함을 알 수가 있다.(실수하기 쉬울 듯)
export const useNumber = number => {
	const isOdd = computed(() => unref(number) % 2 === 1);
	const isEven = computed(() => !isOdd.value);

	return {
		isOdd,
		isEven,
	};
};
