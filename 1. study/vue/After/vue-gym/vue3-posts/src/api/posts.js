import { posts } from '.';

// 밖에서도 목록을 조회 가능하도록 하기 위해
export function getPosts(params) {
	return posts.get('/', { params });
}

export function getPostById(id) {
	// String으로 인식이 되어서 undefined가 떳다??? -> 그럴수 있겠네.
	// const numberId = parseInt(id); // 다른 곳에서 해결함..
	// console.log(typeof id);
	return posts.get(`/${id}`);
}

export function createPost(data) {
	return posts.post('', data);
}

// 전체 수정(안 집어넣은 요소는 빈값으로 판단하고 데이터가 날아가게 설계??)
// export function updatePost(id, data) {
// 	return posts.put(`/${id}`, data);
// }

// 일부수정
export function updatePost(id, data) {
	return posts.patch(`/${id}`, data);
}

export function deletePost(id) {
	return posts.delete(`/${id}`);
}
