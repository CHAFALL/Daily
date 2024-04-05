/**
 * 제네릭 클래스
 */

class List<T> {
  constructor(private list: T[]) {
    // 이것도 private 접근 제어자가 달려있으면 자동으로 해줌.
    // this.list = list;
  }
  push(data: T) {
    this.list.push(data);
  }
  pop() {
    return this.list.pop();
  }
  print() {
    console.log(this.list);
  }
}

const numberList = new List([1, 2, 3]);
numberList.pop();
numberList.push(4);
numberList.print();

const stringList = new List(["1", "2"]);
stringList.push("hello");

// 제네릭 클래스는 제네릭 interface나 제네릭 타입변수와는 다르게 클래스의 생성자를 호출할 때 이 생성자의 인수로 전달하는 이 값을 기준으로 type변수에 type을 추론

//-> 그렇기 때문에 제네릭 interface나 제네릭 타입변수와는 다르게 우리가 앞에다가 반드시 타입을 명시 안해줘도 됨.