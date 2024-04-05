/**
 * 조건부 타입
 */
type A = number extends string ? string : number;

type ObjA = {
  a: number;
};

type ObjB = {
  a: number;
  b: number;
};

type B = ObjB extends ObjA ? number : string;

/**
 * 제네릭과 조건부 타입
 */

type StringNumberSwitch<T> = T extends number ? string : number;

let varA: StringNumberSwitch<number>;

let varB: StringNumberSwitch<string>;

// 기존 방식 (이러면 해줘야 될 것이 너무 많아!!)
// function removeSpaces(text: string | undefined | null) {
//   if (typeof text === "string") {
//     return text.replaceAll(" ", "");
//   } else {
//     return undefined;
//   }
// }

// let result = removeSpaces("hi im winterload") as string;
// result.toUpperCase();

// New
function removeSpaces<T>(text: T): T extends string ? string : undefined

function removeSpaces(text: any) {
  if (typeof text === "string") {
    return text.replaceAll(" ", "");
  } else {
    return undefined;
  }
}

let result = removeSpaces("hi im winterload");
result.toUpperCase();

let result2 = removeSpaces(undefined);

