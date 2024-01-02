import axios from 'axios';

function create(baseURL, option) {
	const instance = axios.create(Object.assign({ baseURL }, option));
	return instance;
}

export const posts = create(`${import.meta.env.VITE_APP_API_URL}posts/`);
// development : 'http://localhost:5000/posts/'
// production : 'http://localhost:5001/posts/'
