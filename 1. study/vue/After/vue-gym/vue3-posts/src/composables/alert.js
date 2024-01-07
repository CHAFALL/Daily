import { useAlertStore } from '@/stores/alert';
import { storeToRefs } from 'pinia';

export const useAlert = () => {
	const { alerts } = storeToRefs(useAlertStore());
	const { vAlert, vSuccess } = useAlertStore();
	return {
		alerts,
		vAlert,
		vSuccess,
	};
};

// alert store에 적용 전

// 함수 범위가 아닌 모듈 범위로 빼줌.(공유을 위해...)
// const alerts = ref([]);
// export function useAlert() {
// 	// alert
// 	const vAlert = (message, type = 'error') => {
// 		alerts.value.push({ message, type });
// 		setTimeout(() => {
// 			alerts.value.shift();
// 		}, 2000);
// 	};
// 	const vSuccess = message => vAlert(message, 'success');
// 	return {
// 		alerts,
// 		vAlert,
// 		vSuccess,
// 	};
// }
