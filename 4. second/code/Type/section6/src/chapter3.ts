/**
 * 인터페이스와 클래스
 */

interface CharacterInterface {
  name: string;
  moveSpeed: number;
  move(): void;
}

// 방식 1
// class Character implements CharacterInterface {
//   name: string;
//   moveSpeed: number;

//   constructor(name: string, moveSpeed: number) {
//     this.name = name;
//     this.moveSpeed = moveSpeed;
//   }

//   move(): void {
//     console.log(`${this.moveSpeed} 속도로 이동!`);
//   }
// }

// 방식 2 (접근제어자를 써서 필드 생략)
// 여기서 주의할 점: 인터페이스로 정의한는 필드들은 무조건 public이라서 접근제어자에 다른 것을 달면 안됨!!! -> 그래서 private 같은 것이 있다면 인터페이스에 정의하지 말고 그냥 아래와 같이 따로 정의를 해줘야 됩니다.
class Character implements CharacterInterface {
  constructor(
    public name: string,
    public moveSpeed: number,
    private extra: string
  ) {
    this.name = name;
    this.moveSpeed = moveSpeed;
  }

  move(): void {
    console.log(`${this.moveSpeed} 속도로 이동!`);
  }
}

// 보통 클래스를 만들 때 이렇게 인터페이스로 설계도를 먼저 만들고 구현하는 일은 보통은 없다.
// 근데 어떤 라이브러리의 구현이나 아니면 굉장히 복잡하고 정교한 프로그래밍을 해야 된다거나 할 때는 인터페이스를 이용해서 이렇게 설계도를 구현하는 과정도 필요할 수 있다.

// 그래서 참고 느낌으로 알아두도록!!