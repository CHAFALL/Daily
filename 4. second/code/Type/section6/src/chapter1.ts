/**
 * 타입스크립트의 클래스
 */

const employee = {
  name: "chafa",
  age: 27,
  position: "developer",
  Worker() {
    console.log("일함");
  },
};

// 타입스크립트의 클래스는 실제 타입으로도 활용이 된다.
class Employee {
  // 필드
  name: string;
  age: number;
  position: string;


  // 생성자
  // 아래까지 써줘야지만 초기값 설정 안했다고 오류가 뜨지 않음. (위에다가 초기값 설정을 해주는 방식도 있긴함..)
  constructor(name: string, age: number, position: string) {
    this.name = name;
    this.age = age;
    this.position = position;
  }

  // 메서드
  work() {
    console.log("일함");
  }
}

class ExecutiveOfficer extends Employee {
  // 필드
  officeNumber: number;

  // 생성자
  constructor(
    name: string,
    age: number,
    position: string,
    officeNumber: number
  ) {
    super(name, age, position);
    this.officeNumber = officeNumber;
  }
}

const employeeB = new Employee("chafa", 27, "개발자");
console.log(employeeB);

// 타입스크립트의 클래스는 실제 타입으로도 활용이 된다.
const employeeC: Employee = {
  name: "",
  age: 0,
  position: "",
  work() {},
};
