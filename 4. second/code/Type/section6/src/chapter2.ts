/**
 * 접근 제어자
 * access modifier
 * => public private proteced
 */

class Employee {
  // 필드
  // private name: string;
  // protected age: number;
  // position: string;

  // 생성자 -> 이렇게 생성자에서 접근제어자를 할당할꺼면 필드는 지워줘야됨.(중복으로 했다고..)
  // 이렇게 접근 제어자가 붙어있는 매개변수들은 자동으로 필드도 정의하고 심지어 필드의 값 초기화도 자동으로 해줌.
  constructor(
    private name: string,
    protected age: number,
    public position: string
  ) {
    this.name = name;
    this.age = age;
    this.position = position;
  }

  // 메서드
  work() {
    console.log(`${this.name} 일함`);
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
  // 메서드
  func() {
    // this.name;
    this.age;
  }
}

const employee = new Employee("chafa", 27, "developer");

// 이렇게 수정하는 것도 가능
// why? 일단은 객체이기도 하고 또 클래스의 각각의 필드에 대해 접근제어자가 기본값으로 public으로 되어있으므로
// employee.name = "홍길동";
// employee.age = 30;
employee.position = "디자이너";

console.log(employee);
