import axios from 'axios';
import { ref, unref, watchEffect, isRef } from 'vue';

axios.defaults.baseURL = import.meta.env.VITE_APP_API_URL;

const defaultConfig = {
	method: 'get',
};

const defaultOptions = {
	immediate: true,
};

// config 객체는 이따가 구조분해 할당을 할 것, default로는 빈 객체로 두자
// 그래야 undefined로 와도 에러가 안남...
export const useAxios = (url, config = {}, options = {}) => {
	const response = ref(null);
	const data = ref(null);
	const error = ref(null);
	const loading = ref(false);

	const { onSuccess, onError, immediate } = {
		...defaultOptions, // 위에서 아래로 내려가면서 덮어써짐
		...options, // 그러면 default로 immediate가 true였다가 options에서 false로 오면 false가 최종적으로 값이 된다.
	};

	// 중요!!
	// ref로 선언된 객체(RefImpl) 풀어주는 방법!!(params 객체를 wrapping으로 풀어줘 보자!!) -> unref 필요
	// console.log('config.params: ', config.params);
	const { params } = config;
	const execute = body => {
		data.value = null;
		error.value = null;
		loading.value = true;
		axios(unref(url), {
			...defaultConfig,
			...config,
			params: unref(params),
			// 여긴 이해못함
			// watchEffect는 callback 함수로 함수가 넘어오므로
			// body의 타입이 객체일 때만 body를 넘기고 아니면 빈 값을 넣어주자!
			data: typeof body === 'object' ? body : {},
		})
			.then(res => {
				response.value = res;
				data.value = res.data;
				if (onSuccess) {
					onSuccess(res);
				}
			})
			.catch(err => {
				error.value = err;
				if (onError) {
					onError(err);
				}
			})
			.finally(() => {
				loading.value = false;
			});
	};
	// params를 반응형데이터로 넘기는 사람도 있을 것이고 그냥 일반 오브젝트로 넘기는 분들도 있을 것이다.
	//-> 그래서 둘 다 가능하게 하기 위해서 아래와 같이 해봄
	if (isRef(params) || isRef(url)) {
		watchEffect(execute);
	} else {
		if (immediate) {
			execute(); // 한번만 호출해도 되므로.(일반은)
		}
	}

	// 이렇게 execute라는 함수로 그냥 감싼 후에 감시하는 것임 그냥
	return {
		response,
		data,
		error,
		loading,
		execute,
	};
};

// 참고로 여기서 async await로 안 기다려도 되는 이유??
// 리턴 값으로 UI에 뿌릴 것이라 이러한 데이터는 반응형으로 연결이 되어 있기 때문에 나중에 이렇게 데이터를 삽입을 해도 해당 UI에서 감지해서 변경이 될 것이기 때문에 async await를 안 써도 됨.
