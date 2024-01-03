export default {
	install(app, options) {
		const person = {
			name: 'chafa',
			say() {
				alert(this.name);
			},
			...options,
		};
		app.config.globalProperties.$person = person;
		// setup 함수 내에서 접근하고플때(아래)
		app.provide('person', person);
	},
};
