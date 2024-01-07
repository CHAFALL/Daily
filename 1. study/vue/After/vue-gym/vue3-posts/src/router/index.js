import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import AboutView from '@/views/AboutView.vue';
import PostCreateView from '@/views/posts/PostCreateView.vue';
import PostDetailView from '@/views/posts/PostDetailView.vue';
import PostListView from '@/views/posts/PostListView.vue';
import PostEditView from '@/views/posts/PostEditView.vue';
import NotFoundView from '@/views/NotFoundView.vue';
import NestedView from '@/views/nested/NestedView.vue';
import NestedOneView from '@/views/nested/NestedOneView.vue';
import NestedTwoView from '@/views/nested/NestedTwoView.vue';
import NestedHomeView from '@/views/nested/NestedHomeView.vue';
import Mypage from '@/views/Mypage.vue';

const routes = [
	{
		path: '/',
		name: 'Home',
		component: HomeView,
	},
	{
		path: '/about',
		name: 'About',
		component: AboutView,
	},
	{
		path: '/posts',
		name: 'PostList',
		component: PostListView,
	},
	{
		path: '/posts/create',
		name: 'PostCreate',
		component: PostCreateView,
	},
	{
		path: '/posts/:id',
		name: 'PostDetail',
		component: PostDetailView,
		// 위의 파라미터 값(:id)이 해당 컴퍼넌트에 props로 전달됨
		// 여기 연구 더 필요(내가 직접 오류 잡아내서..)
		props: true,
		// 객체나 함수로도 넘겨줄 수 있음.
		// props: route => {
		// 	return {
		// 		id: parseInt(route.param.id),
		// 	};
		// },
	},
	{
		path: '/posts/:id/edit',
		name: 'PostEdit',
		component: PostEditView,
	},

	{
		path: '/:pathMatch(.*)*',
		name: 'NotFound',
		component: NotFoundView,
	},

	{
		path: '/nested',
		name: 'Nested',
		component: NestedView,
		children: [
			{
				path: '',
				name: 'NestedHome',
				component: NestedHomeView,
			},
			{
				// /nested/one 이렇게 자동으로 붙음
				// 주의사항 앞에 저절로 /nested가 붙기때문에 /one이라고 하면 안됨
				path: 'one',
				name: 'NestedOne',
				component: NestedOneView,
			},
			{
				path: 'two',
				name: 'NestedTwo',
				component: NestedTwoView,
			},
		],
	},
	{
		path: '/my',
		name: 'Mypage',
		component: Mypage,
		// 이렇게 배열로 정의한다면 해쉬를 없애거나 이러한 기능을 계속 추가 가능!!
		beforeEnter: [removeQueryString],
	},
];

function removeQueryString(to) {
	if (Object.keys(to.query).length > 0) {
		return { path: to.path, query: {} };
	}
}

const router = createRouter({
	history: createWebHistory('/'),
	// history: createWebHashHistory(), // SEO 검색엔진에 치명적 단점이 있어서 안 씀.. 장점은 뭐였드라...어라라?
	routes,
});

// router.beforeEach((to, from) => {
// 	console.log('to: ', to);
// 	console.log('from: ', from);
// 	if (to.name === 'Mypage') {
// 		// return false;
// 		// return { name: 'Home' };
// 		return '/posts';
// 	}
// });

export default router;
