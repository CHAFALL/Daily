export class ColumnNumericTransformer {
  // 이 메서드는 엔티티의 속성 값을 데이터베이스에 저장하기 전에 호출됩니다.
  to(data: number): number {
    return data;
  }
  // 이 메서드는 데이터베이스에서 값을 읽어올 때 호출됩니다.
  from(data: string): number {
    return parseFloat(data);
  }
}
