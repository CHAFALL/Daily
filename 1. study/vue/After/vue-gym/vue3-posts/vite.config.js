import { fileURLToPath, URL } from 'node:url';

import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

// https://vitejs.dev/config/
export default defineConfig({
	plugins: [vue()],
	// envPrefix (참고)
	// mode의 디폴트 값 development
	resolve: {
		alias: {
			'@': fileURLToPath(new URL('./src', import.meta.url)),
		},
	},
});

// 참고
// 비트에서는 기본적으로 npm run dev로 실행을 할 때 기본적으로 development가 되고 빌드 할 때는 production 모드가 된다.
