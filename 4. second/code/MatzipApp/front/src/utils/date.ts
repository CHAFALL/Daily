function getDateDetails(dateString: Date | string) {
  const date = new Date(dateString);
  const year = date.getFullYear();
  const month = date.getMonth() + 1;
  const day = date.getDate();

  return {year, month, day};
}

function getDateWithSeparator(
  dateString: Date | string,
  separator: string = '',
) {
  const {year, month, day} = getDateDetails(dateString);

  return [
    String(year),
    String(month).padStart(2, '0'),
    String(day).padStart(2, '0'),
  ].join(separator);
}

function getDateLocaleFormat(dateString: Date | string) {
  const {year, month, day} = getDateDetails(dateString);

  return `${year}년 ${month}월 ${day}일`;
}

function getMonthYearDetails(initialDate: Date) {
  const month = initialDate.getMonth() + 1;
  const year = initialDate.getFullYear();

  // 매달 1일이 무슨 요일에서 시작하는 지
  const startDate = new Date(`${year}-${month}`);
  const firstDOW = startDate.getDay();

  // new Date("2023-6")는 자바스크립트 Date 객체를 생성합니다. 이 객체는 해당 연도와 월의 1일을 나타냅니다. 즉, 2023-06-01이 됩니다.

  // getDay() 메서드는 주어진 날짜의 요일을 숫자로 반환합니다. 0은 일요일, 1은 월요일, ... , 6은 토요일을 나타냅니다.

  const lastDateString = String(
    new Date(
      initialDate.getFullYear(),
      initialDate.getMonth() + 1,
      0,
    ).getDate(),
  );

  // 마지막 인자인 0은 해당 월의 0일을 나타내는데, 자바스크립트에서는 0일이 이전 달의 마지막 날을 의미합니다. 예를 들어, 6월의 0일은 5월의 마지막 날이 됩니다.

  const lastDate = Number(lastDateString);

  return {month, year, startDate, firstDOW, lastDate};
}

type MonthYear = {
  month: number;
  year: number;
  startDate: Date;
  firstDOW: number;
  lastDate: number;
};

function getNewMonthYear(prevData: MonthYear, increment: number) {
  const newMonthYear = new Date(
    prevData.startDate.setMonth(prevData.startDate.getMonth() + increment),
  );

  return getMonthYearDetails(newMonthYear);
}

function isSameAsCurrentDate(year: number, month: number, date: number) {
  const currentDate = getDateWithSeparator(new Date());
  const inputDate = `${year}${String(month).padStart(2, '0')}${String(
    date,
  ).padStart(2, '0')}`;

  return currentDate === inputDate;
}

export {
  getDateWithSeparator,
  getDateLocaleFormat,
  getMonthYearDetails,
  getNewMonthYear,
  isSameAsCurrentDate,
};

export type {MonthYear};

// padStart : 2자리가 아니면 앞에 0을 붙여라
