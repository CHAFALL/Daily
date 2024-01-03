const objPlugins = {
	// 객체로 작성시 install 메소드 필수
	// 플러그인은 두 가지의 매개변수를 받는다.(함수도 동일)
	// 첫번째: 애플리케이션의 인스턴스
	// 두번째: 옵션
	install(app, option) {
		console.log('objPlugins app: ', app);
		console.log('objPlugins option: ', option);
		// app 객체를 찍어서 확인 가능.
		// app.component() : 전역 컴포넌트 추가 가능
		// app.config.globalProperties 전역 애플리케이션 인스턴스에 속성 추가
		// app.directive 커스텀 디렉티브 추가 가능
		// app.provide 다양한 리소스를 자식 컴포넌트에서 사용할 수 있도록 해줌
	},
};
export default objPlugins;
