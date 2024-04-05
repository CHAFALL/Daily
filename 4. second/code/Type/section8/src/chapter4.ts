/**
 * 템플릿 리터럴 타입 (참고)
 */

type Color = "red" | "black" | "green";

type Animal = "dog" | "cat" | "chicken";

type ColorAnimal = `${Color}-${Animal}`;

const colorAnimal: ColorAnimal = "black-cat";
