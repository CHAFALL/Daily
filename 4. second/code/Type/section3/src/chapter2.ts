// 업캐스팅은 모두 허용이 되지만 다운캐스팅은 아님
/**
 * Unknown 타입 (최상위)
 */

function unknownExam() {
  let a: unknown = 1;
  let b: unknown = "hello";
  let c: unknown = true;
  let d: unknown = null;
  let e: unknown = undefined;

  let unknownVar: unknown;

  // let num: number = unknownVar;
  // let str: string = unknownVar;
  // let bool: boolean = unknownVar;
}

/**
 * Never 타입 (최하위) -> 공집합 느낌
 */

function neverExam() {
  function neverFunc(): never {
    while (true) {}
  }

  let num: number = neverFunc();
  let str: string = neverFunc();
  let bool: boolean = neverFunc();

  // let never1: never = 10;
  // let never2: never = "string";
  // let never3: never = true;
}

/**
 * Void 타입 (void > undefined)
 */

function voidExam() {
  function voidFunc(): void {
    console.log("hi");
    return undefined;
  }

  let voidVar: void = undefined;
}

/**
 * any 타입 (치트키) -> 얘는 모든 타입의 슈퍼타입으로 위치하기도 하고 반대로 모든 타입의 서브타입으로도 위치하기도 함(never 제외)
 */

// 조금 위험한 타입이라서 웬만하면 이용하지 말 것.

function anyExam() {
  let unknownVar: unknown;
  let anyVar: any;
  let undefinedVar: undefined;
  let neverVar: never;

  anyVar = unknownVar; // 엉 다운이 되네?? (any 타입 한정으로 다운캐스팅이 됨.)

  undefinedVar = anyVar; // 엉 다운이 되네?? (any 타입 한정으로 다운캐스팅이 됨.)

  // 즉, any 타입은 자기한테 오는 다운캐스팅도 되고 자기가 다운캐스팅 하는것도 가능.

  // any가 유일하게 못하는 것!!
  // neverVar = anyVar;
}
