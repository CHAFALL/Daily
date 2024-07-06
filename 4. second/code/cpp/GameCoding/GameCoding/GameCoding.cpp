#include <iostream>
using namespace std;// 일일이 std::를 치기 귀찮아서
#include "Helper.h"
#include "Map.h"
#include "Player.h"
#include <iomanip> // 줄맞춤을 해줌.

#pragma region 전체
#pragma region 챕터1

// char: 1byte (8 bit)
// short: 2
// int: 4
// __int64 (long long): 8

// float: 4 (근사치)
// double: 8

// bool: 1byte

// 절차적으로 코드가 실행됨.

// 전역

char ch;
float speed;
bool playSound;

// 비트연산 주의할 점: 음수가 포함이 되는 경우일 때(끝 자리 수는 어떻게 될까?)
// 실제로 동작하는 걸 보면 기존에 있던 그 수치를 그대로 유지!!!

#pragma endregion
#pragma region 챕터2

// 절차적으로 코드가 실행이 되므로 함수의 순서도 맞춰줘야됨
// 그래서 다음과 같이 미리 이런 해당 함수가 있을 것이다 미리 선언해줌.
// 
//int Add(int a, int b); -> 이렇게 약속을 했으면 컴파일 에러를 안내고 일단은 넘어가고 나중에 그 함수를 이어붙이면 되겟구나 생각함
// 나중에 가면 요런 파일들을 header 파일에다가 별도로 구분을 해둘것임!
// C++은 존재를 알리는 부분과 실제 구현부분을 이렇게 분리해서 만듬!!
// C++: 인자의 타입이나 인자의 개수가 다르면 함수 이름이 같더라도 재사용 가능. 

// 파일 분할 -> 절차적이라 C#과 달리 좀 더 어려움.

#pragma endregion
#pragma region 스택 이론

// 함수를 엄청 많이 호출하면(ex.DFS) 스택 오버플로우가 발생.

// 스택 메모리는 높은 주소에서 낮은 주소로 증가.
// 메모장을 공통으로 사용하는데 일부 영역을 할당받고 그 부분만 이용하다가 리턴이 되면 반납하는 느낌 (이때 메모리가 해체되는 개념은 아님. -> 그래서 함수가 날아간 이후에 이 영역을 이용하면 안됨!! )
// 메모장은 그대로 있는데 그냥 내가 사용할 영역만 계속 바꿔치기 하는 느낌. (반납할 때 정리(초기화)를 하고 반납하는 것이 아님)

// 함수 타고 들어가고 어떻게 다시 다음으로 갈 곳을 잘 찾아올까?? -> 함수를 위해 필요한 것들(인자)와 돌아오기 위한 주소들을 기입해줌!!

// 참고
// 인자를 stack에다가 밀어넣은다는 표현은 절반은 맞은 표현 -> (64비트 한정) 인자가 사소한 경우라면 스택에다가 밀어넣은 것이 아니라 레지스터를 통해서 전달을 받는 경우도 더러 있다. (내 손이 비어있으면.)

// 힙 같은 경우에는 진짜로 메모리를 동적으로 만들었다가 삭제했다가 하는 개념.

// x86 -> 32비트 프로그램임.
// 64비트와 32비트의 차이점? -> 레지스터의 크기 (CPU가 한번에 계산할 수 있는 크기) -> 레지스터 (CPU의 손발 느낌(비유: 사탕(메모리)을 집을 수 있는 만큼 CPU가 처리가능.))

#pragma endregion
#pragma region 텍스트 RPG


//enum PlayerType
//{
//    PT_None = 0,
//    PT_Knight = 1,
//    PT_Archer = 2,
//    PT_Mage = 3,
//};
//
//enum MonsterType
//{
//    MT_None = 0,
//    MT_Slime = 1,
//    MT_Orc = 2,
//    MT_Skeletion = 3,
//};
//
//// C++의 struct는 class와 유사
//// 일단은 struct는 데이터를 뭉쳐서 관리하는 기능이다 정도로만
//
//// C#에서는 struct와 class 문법이 완전히 다름 -> (struct는 복사가 일어나고 클래스는 참조 타입 이런식으로)
//
//struct StatInfo
//{
//    int hp;
//    int attack;
//    int defence;
//};
//
//// 내가 어떤 플레이어 타입인지를 들고 있는 것이 좋을 것이다!
//PlayerType playerType; // int로 선언을 해도 되긴 함. (C#에서는 enum과 int는 완전히 다른 개념이지만 c++은 동일하게 취급)
//// 이런 것은 나중에 하나로 묶어줄 것이다! (struct) -> 나중에는 전역으로 관리 안하고 힙 영역에 따로 동적으로 할당을 해가지고 관리 할 것이다. 
//StatInfo playerStat;
//
//MonsterType monsterType;
//StatInfo monsterStat;
//
//void EnterLobby();
//void SelectPlayer();
//void EnterField();
//void CreateRandomMonster();
//void EnterBattle();
//void WaitForNextKey();

#pragma endregion
#pragma region 포인터 이론

//void AddHp(int* hp, int value)
//{
//    *hp += value;
//}

#pragma endregion
#pragma region 포인터 연산
//void Swap(int* a, int* b)
//{
//    int temp = *a;
//    *a = *b;
//    *b = temp;
//}
#pragma endregion
#pragma region 포인터 연산 실습

//struct StatInfo
//{
//    int hp;
//    int attack;
//    int defence;
//};
//
//
//// 해당 방식의 아쉬운 점 : 복사를 하기 때문에 너무 많은 값을 수정할 때 조금...
//// 어차피 한번만 만들고 없앨꺼 아냐? (stack) -> 그래도 이런 함수를 굉장히 많이 호출하면 좀.
//StatInfo CreatePlayer()
//{
//    StatInfo info;
//
//    cout << "플레이어 생성" << endl;
//
//    info.hp = 100;
//    info.attack = 10;
//    info.defence = 2;
//
//    return info;
//}
//
//// 이렇게 하면 안되는 이유: 사용안하는 부분을 리턴해주는 꼴이 됨.
//// 근데 왜 크래쉬 발생 x? -> 가상의 선을 그어가지고 여기부터는 활용하면 안 된다고 했지만
//// 이 메모리가 접근 불가한 것은 아니므로
//
//// 주의할 점!!!!! -> 함수 안에 있는 것을 자꾸만 주소값으로 뱉으려고 하면 안됨!!!
//
//StatInfo* CreatePlayer2()
//{
//    StatInfo info;
//
//    cout << "플레이어 생성" << endl;
//
//    info.hp = 100;
//    info.attack = 10;
//    info.defence = 2;
//
//    return &info;
//}
//
//// 먼저 메모리를 할당한 다음에 그 내용물을 채워놓은 느낌.
//// 포인터를 받는다면 주소값만 받는 것이고 그 주소값을 타고 갔을 때 (큰) 데이터가 있다는 얘기지 얘가 달라지진 x
//// 호출할 때 부담 low
//// 그래서 몬스터나 플레이어 같이 정보가 어마무시하게 커지는 애들을 복사하는 것을 사용하고 싶지 않다고 할 때
//// 이렇게 포인터를 이용.
//void CreateMonster(StatInfo* info)
//{
//    cout << "몬스터 생성" << endl;
//
//    info->hp = 40;
//    //(*info).attack = 8;
//    info->attack = 8;
//    info->defence = 1;
//}
//
//// 둘 중에서 뭐가 더 낫다고 따지기 보다는 어차피 나중에가면 스택 메모리에다가 이렇게 관리하는 것 보다는 
//// 동적으로 할당해서 힙 메모리에다가 사용해도 될 것이기 때문에 이 두 방식을 자주 하진 x
//
//
//void Battle(StatInfo* player, StatInfo* monster)
//{
//    while (true)
//    {
//        int damage = player->attack - monster->defence;
//        if (damage < 0)
//            damage = 0;
//
//        monster->hp -= damage;
//        if (monster->hp < 0)
//            monster->hp = 0;
//
//        cout << "몬스터 HP : " << monster->hp << endl;
//
//        if (monster->hp == 0)
//            return;
//
//        damage = monster->attack - player->defence;
//        if (damage < 0)
//            damage = 0;
//
//        player->hp -= damage;
//        if (player->hp < 0)
//            player->hp = 0;
//
//        cout << "플레이어 HP : " << player->hp << endl;
//
//        if (player->hp == 0)
//            return;
//    }
//}

#pragma endregion
#pragma region 문자열
//// 우리버전
//// [Hello0...........]
//int StrLen(const char* str)
//{
//    int count = 0;
//
//    /*while (str[count] != 0)
//        count++;*/
//
//    while (str[count] != '\0')
//        count++;
//
//    return count;
//}
//
//char* StrCpy(char* dest, char* src)
//{
//    // 원래 주소의 위치를 저장
//    char* ret = dest;
//
//    /*int i = 0;
//    while (src[i] != 0)
//    {
//        dest[i] = src[i];
//        i++;
//    }
//
//    dest[i] = 0;*/
//
//    // 배열의 이름은 데이터의 첫번째 위치의 주소임을 이용하는 방식(포인터 이용)
//    while (*src != 0)
//    {
//        *dest = *src;
//        dest++;
//        src++;
//    }
//
//    *dest = 0;
//
//    return ret;
//}
//
//char* StrCat(char* dest, char* src)
//{
//    char* ret = dest;
//
//    /* int len = StrLen(dest);
//
//     int i = 0;
//     while (src[i] != 0)
//     {
//         dest[len + i] = src[i];
//         i++;
//     }
//
//     dest[len + i] = 0;*/
//
//     // 포인터 방식
//    while (*dest)
//    {
//        dest++;
//    }
//
//    while (*src)
//    {
//        *dest = *src;
//        dest++;
//        src++;
//    }
//
//    return ret;
//}
#pragma endregion
#pragma region 참조
//struct StatInfo
//{
//    int hp;
//    int attack;
//    int defence;
//};
//
//// 1) 값(복사) 전달 방식
//void PrintByCopy(StatInfo player)
//{
//    cout << "----------------" << endl;
//    cout << "HP : " << player.hp << endl;
//    cout << "ATT : " << player.attack << endl;
//    cout << "DEF : " << player.defence << endl;
//    cout << "----------------" << endl;
//}
//
//// 2) 주소 전달 방식 (원본을 건드리는 방식)
//// 사용하는 경우 
//// -> 1. 원본을 건드리고 싶을 때 (원격)
//// -> 2. 복사 비용 x
//// 장점: nullptr를 표현 가능!
//// 포인터 값은 경우에는 문법적으로 주소값을 넘겨야 됨-> (&) , 그래서 포인터임을 파악하기 쉬움.
//void PrintByPointer(StatInfo* player)
//{
//    cout << "----------------" << endl;
//    cout << "HP : " << (*player).hp << endl;
//    cout << "ATT : " << player->attack << endl;
//    cout << "DEF : " << player->defence << endl;
//    cout << "----------------" << endl;
//}
//
//// 3) 참조 전달 방식
//// 2번 방식을 1번처럼 쓰고 싶다!!
//// 타입의 뒤에 &를 붙여주면 참조라는 의미를 가짐.
//// 어 그럼 개꿀 아냐?  
//// 단점: 
//// 1. 비어있는 참조를 만들 수 없음... (무조건 존재 해야 됨!)
//// 2. 1번 방식인지 3번 방식인지 파악할 수 없음 (포인터인 경우 &를 달아줘서 파악 가능)
//// 그래서 원본을 쥐도 새도 모르게 건드릴 수 있는 위험이 존재
//// 버그의 96%는 클라건 서버건 null로 인한 오류
//
//// 그래서 나온 정책: 내부에서 절대로 건드릴 일 없이 출력만 하고 싶을 때 성능 향상을 위해 복사
//// 를 하지 않고 참조를 사용하는 경우다라고 하면 앞에다가 const를 붙이겠다라는 규칙을 정함.
//// -> 그러면 내부적으로 얘를 건드리지는 않을 것이지만 우리가 참조로 받는 장점을 챙기겠다라는 힌트
//// 를 줄 수 있음.
//
//// 근데 이게 아니라 진짜로 만약에 우리가 의도적으로 뭔가를 건드리기 위해서 참조값을 받았다 (-> 쓰기 귀찮아서 참조값으로)
//// -> 이런 경우에는 대문자 OUT를 다는 편이다
////#define OUT(@@@@) // -> OUT 부분이 @@@@로 바뀜, 그래서 비워놓으면 아무것도 없어져서 알려주는 용도로
//// 사용할 때 용이 -> (아! 수정하는 목적으로 참조를 쓰고 있구나!!)
//// 마찬가지로 호출하는 쪽에서도 OUT를 달아서 얘가 뭔가 변화가 일어나고 있다는 것을 명시가능
//
//// C#의 참조는 3번에 가까움.
//
//#define OUT
//void PrintByRef(OUT StatInfo& player)
//{
//    cout << "----------------" << endl;
//    cout << "HP : " << player.hp << endl;
//    cout << "ATT : " << player.attack << endl;
//    cout << "DEF : " << player.defence << endl;
//    cout << "----------------" << endl;
//}
//
////void PrintByRef(const StatInfo& player)
////{
////    cout << "----------------" << endl;
////    cout << "HP : " << player.hp << endl;
////    cout << "ATT : " << player.attack << endl;
////    cout << "DEF : " << player.defence << endl;
////    cout << "----------------" << endl;
////}
#pragma endregion
#pragma region 로또 번호 생성기
//// 로또 번호 생성기
//void Swap(int& a, int& b)
//{
//    int temp = a;
//    a = b;
//    b = temp;
//
//}
//
//// 버블
//void Sort(int* numbers, int count)
//{
//
//    for (int i = 0; i < count; i++)
//    {
//        for (int j = 0; j < count - 1 /*- i*/; j++)
//        {
//            if (numbers[j] > numbers[j + 1])
//                Swap(numbers[j], numbers[j + 1]);
//        }
//    }
//
//
//}
//
//void ChooseLotto(int* numbers)
//{
//
//    int count = 0;
//
//    while (count != 6)
//    {
//        // (0 + 1) ~ (44 + 1)
//        int randValue = 1 + rand() % 45;
//
//        // 이미 찾은 값인지?
//
//        bool found = false;
//
//        int i; // 아니면 i값을 밖으로 빼서도 가능 -> i == count이면? 이런식으로 
//        for (i = 0; i < count; i++)
//        {
//            // 이미 있는 값이면 while문에 영향을 미치고 싶다. (found 사용.)
//
//            if (numbers[i] == randValue)
//            {
//                found = true;
//                break;
//            }
//        }
//
//        if (found == false)
//        {
//            numbers[count] = randValue;
//            count++;
//        }
//    }
//
//    Sort(numbers, 6);
//}
#pragma endregion
#pragma region 달팽이문제
//const int MAX = 100;
//int board[MAX][MAX];
//int N;
//
//void PrintBoard()
//{
//    for (int y = 0; y < N; y++)
//    {
//        for (int x = 0; x < N; x++)
//        {
//            cout << setfill('0') << setw(2) << board[y][x] << " "; // 부족한 부분을 0으로 채워주고 그거를 2개짜리로 만들어줘라
//        }
//
//        cout << endl;
//    }
//}
//
//enum DIR
//{
//    RIGHT = 0,
//    DOWN = 1,
//    LEFT = 2,
//    UP = 3,
//
//};
//
//bool CanGo(int y, int x)
//{
//    if (y < 0 || y >= N)
//        return false;
//    if (x < 0 || x >= N)
//        return false;
//    if (board[y][x] != 0)
//        return false;
//
//    return true;
//    
//}
//
//void SetBoard()
//{
//    int dir = RIGHT;
//    int num = 1;
//    int y = 0;
//    int x = 0;
//
//    int dy[] = { 0, 1, 0, -1 };
//    int dx[] = { 1, 0, -1, 0 };
//
//
//    while (true)
//    {
//        board[y][x] = num;
//        
//        if (num == N * N)
//            break;
//
//        // 밖에서도 사용하려고 switch 밖으로 빼둠
//        int nextY = y + dy[dir];
//        int nextX = x + dx[dir];
//
//        /*switch (dir)
//        {
//            case RIGHT:
//                nextY = y;
//                nextX = x + 1;
//                break;
//            case DOWN:
//                nextY = y + 1;
//                nextX = x;
//                break;
//            case LEFT:
//                nextY = y;
//                nextX = x - 1;
//                break;
//            case UP:
//                nextY = y - 1;
//                nextX = x;
//                break;
//        }*/
//
//        if (CanGo(nextY, nextX))
//        {
//            y = nextY;
//            x = nextX;
//            num++;
//        }
//        else
//        {
//            dir = (dir + 1) % 4;
//
//            /*switch (dir)
//            {
//                case RIGHT:
//                    dir = DOWN;
//                    break;
//                case DOWN:
//                    dir = LEFT;
//                    break;
//                case LEFT:
//                    dir = UP;
//                    break;
//                case UP:
//                    dir = RIGHT;
//                    break;
//            }*/
//        }
//    }
//
//}
#pragma endregion
#pragma region 객체지향 개론
//// 객체지향 (Object Oriented Programming)
//// 시작 전부터 모든 것을 객체단위로 생각
//
//// struct와 class의 차이점
//// struct: 기본적으로 모든 멤버는 public 접근 제어자를 가집니다.
//// struct: 주로 데이터 구조를 정의하는 데 사용됩니다.
//// 즉, 멤버 변수만 가지는 간단한 데이터 집합을 표현할 때 사용됩니다.
//
//// class: 기본적으로 모든 멤버는 private 접근 제어자를 가집니다.
//// class: 주로 데이터와 그 데이터에 대한 동작(메서드)을
//// 함께 정의하는 객체 지향 프로그래밍을 위해 사용됩니다.
//
//// 설계도 (붕어빵틀) -> 이렇게 클래스만 만들었으면 아직까지는 얘는 어떠한 영역도 차지 x
//// 객체가 생성이 되는 순간 그 다음부터는 서로 독립적으로 완전히 다르게 동작
//class Knight
//{
//public:
//    // 초기값 세팅이나 부품끼리 연결을 해줄때 필요
//    // 생성자(constructor)
//    // 객체가 생성될 때 무조건 호출되는 함수
//    // 함수인데 리턴 타입을 적어주지 않음
//    // 생성자를 안 만들면 간접적으로 컴파일러가 기본 생성자 하나 (인자 x한 버전)를 만들어줌 (기본 생성자)
//    // 생성자를 직접 만들어 줄때는 초기화를 시켜주자
//
//    // 기본 생성자
//    Knight()
//    {
//        hp = 10;
//        attack = 0;
//        defence = 0;
//        cout << "Knight()" << endl;
//    }
//
//    // 복사 생성자
//    // 동일한 타입의 객체를 복사해 가지고 동일한 상태의 데이터를 갖는 다른 객체를 만들어줌
//    // 얘도 많이 쓰임
//    Knight(const Knight& other)
//    {
//        this->hp = other.hp;
//        this->attack = other.attack;
//        this->defence = other.defence;
//
//        cout << "Knight(const Knight & other)" << endl;
//    }
//
//    // 기타 생성자
//    // 이런 버전의 생성자를 만들어주면 컴파일러가 기본 생성자를 만들어주지 않음
//    Knight(int hp, int attack, int defence)
//    {
//        // 그래서 이렇게 this->를 쓰기 싫어서 _ 컨벤션 사용.
//        this->hp = hp;
//        this->attack = attack;
//        this->defence = defence;
//
//        cout << "Knight()" << endl;
//    }
//
//    // 정리할 때 필요
//    // 만약에 펫과 같이 종속이 된 것이 있다면 같이 처리해야될 때 사용도 됨.
//    // C++은 메모리를 직접 조작하는 언어이므로 메모리를 깔끔하게 정리해주는 것도 필요.
//    // 소멸자(destructor)
//    // 객체가 소멸이 될 때 만들어지는 함수
//    // 소멸자는 생성자와 달리 딱 하나만 존재 가능.
//    ~Knight()
//    {
//        cout << "~Knight()" << endl;
//    }
//
//    // (참고) 코드영역에 들어감 -> 메모리 차지 x
//    // 멤버 함수
//    void Attack() { cout << "Attack" << endl; }
//    void Die() { cout << "Die" << endl; }
//    void HealMe(int value)
//    {
//        Knight* thisPtr = this; // this를 통해 자신의 주소를 알 수 있다.
//        /*(생략되어 있음)this->*/hp += 10; // 멤버 변수에 있는 것 바로 사용 가능.
//    }
//public:
//    // (참고) 객체 생성 시 stack 영역에 들어감 
//    // -> 그래서 아무리 복잡해져도 메모리를 차지 하는 부분은 멤버 변수 쪽만.
//    // 멤버 변수 (네이밍 컨벤션 중 하나 _)
//    int hp;
//    int attack;
//    int defence;
//};
#pragma endregion
#pragma region 상속성
//// 이대로만(저번 시간까지) 하면 발생하는 문제점 2가지
//// 1. 코드 재사용 불가 -> 상속을 통해 해결
//// 2. 기사에 대한 함수, 메이지에 대한 함수 이런 식으로 다 만들어줘야됨 
//// -> 여러 타입을 상위 타입으로 관리해서 해결 (Fight부분)
//// -> 그렇다고 상위 타입의 변수로 관리 (데이터 손실이 발생)를 하는 것이 아니라 포인터(주소값)나 참조값으로 참조를 해가지고 관리
//// -> 이렇게 하면 데이터 손실이 발생하는 것이 아니라 그냥 얘를 상위 타입으로 간주를 하겠다는 의미가 됨.
//// -> 반대로도 가능
//
//
//// OOP 3대 요소 (면접 필수)
//// - 상속성 << inheritance , 공용적으로 쓰이는 데이터들을 위로 위로 올려가지고 관리
//// - 은닉성
//// - 다형성
//
//// 상속을 사용하는 때 : 무존건 겹친다고 상속으로 만들면 되는것이 아니라 Is-A Vs Has-A (Is-A일때 사용)
//
//// GameObject
//// - Creature
//// -- Player, Monster, Npc, Pet
//// - Projectile
//// -- Arrow, Fireball
//// - Env
//
//// Item
//// - Weapon
//// -- Sword, Bow, Lance
//// - Armor
//// -- Helmet, Boots, Armor, Glove
//// - Consumable
//// -- Potion, Scroll
//
//class Inventory
//{
//
//};
//
//enum PLAYERTYPE
//{
//    PT_KNIGHT = 1
//};
//
//class Player
//{
//public:
//    void Move() {}
//    void Attack() {}
//    void Die() {}
//
//public:
//    int _type; // 상위 타입에서 하위 타입을 관리하는 경우도 있음, 하위에도 타입 선언 있겠지? 여긴 안 써놧음
//    int _hp;
//    int _attack;
//    int _defence;
//    Inventory _inventory; // Has-A 일땐 이런 식으로 (일단 참고)
//};
//
//class Knight : public Player // 상속 문법
//{
//public:
//    
//public:
//    int _stamina;
//};
//
//class Archer : public Player 
//{
//public:
//
//public:
//    int _arrowCount;
//
//};
//
//class Mage : public Player 
//{
//public:
//
//public:
//    int _mp;
//};
//
//void Fight(Player* p1, Player* p2)
//{
//    //(Knight*)p1;
//    p1->_hp -= p2->_attack;
//}
#pragma endregion
#pragma region 은닉성
//// OOP 3대 요소
//// - 상속성 << inheritance , 공용적으로 쓰이는 데이터들을 위로 위로 올려가지고 관리
//// - 은닉성 << data hiding (캡슐화 encapsulation) , 몰라도 되는 것은 내가 숨기겠다(노출을 안하겠다)는 뜻
//// - 다형성
//
//// 은닉을 하는 이유 2가지
//// - 정말로 위험하고 남이 건드리면 안되는 코드가 있을 수 있거나 혹은 다른 경로로 애당초 접근을 원하는 경우
//// - 자동차의 경우 사용자가 얼마나 알아야 하나?
//
//// 접근 지정자
//// public, protected (상속받는 것들은 접근 가능), private
//
//class Car
//{
//public:
//    void MoveHandle(){}
//    void PushPedal(){}
//    void OpenDoor(){}
//    void TurnKey()
//    {
//        // ...
//        PutFuelInEngine();
//        // ...
//    }
//
//protected:
//    // 우리가 알 필요 없는 부분
//    void Disassemble(){}
//    void PutFuelInEngine(){}
//    void ConnectCircuit(){}
//
//public:
//    // 핸들
//    // 페달
//    // 엔진
//    // 문
//    // 전기선
//};
//
//// 상속 접근 지정자 : 다음 세대한테 부모님의 유산을 어떻게 물려줄지?
//// 부모님은 나한테 좋은 마음으로 이것저것을 물려주셨는데 나는 이기적이어서 그걸 물려줄지 고민.
//// public : 공개적 상속 (이걸 굳이 다른 것으로 바꿀 케이스를 보기가 매우 드뭄)
//// protected : 보호받는 상속 (내 자손들한테만 물려줄거야) (public -> protected)
//// private : 나까지만 꿀빰 (public, protected -> private)
//class SuperCar : public Car
//{
//public:
//    void Test()
//    {
//        MoveHandle();
//        Disassemble();
//    }
//};
//
//// 이런 식으로 부분적으로 숨겨 가지고 딱 내가 원하는 부분만 노출 시켜주는 것을 캡슐화라고 함
//
//class Knight
//{
//public:
//    void SetHp(int hp)
//    {
//        _hp = hp;
//        if (_hp <= 50)
//        {
//            //TODO
//        }
//    }
//
//    int GetHp() 
//    { 
//        return _hp; 
//    }
//
//    // 멤버 변수들을 멋대로 밖에서 접근해서 고치는 것 자체가 굉장히 안 좋음
//    // Get, Set으로 관리 -> 이렇게 하면 좋은점
//    // - 누군가가 HP를 고치는 코드를 일일이 찾아볼 필요 없이 디버깅해서 바로 찾을 수 있음. 
//    // - 모든 애들이 다 동일하게 Get이나 Set을 통해 접근하다 보니 
//    // 코드 추가해서 모든 코드가 동시에 적용가능
//private:
//    int _hp = 100;
//};
#pragma endregion
#pragma region 다형성
//// OOP 3대 요소
//// - 상속성 << inheritance , 공용적으로 쓰이는 데이터들을 위로 위로 올려가지고 관리
//// - 은닉성 << data hiding (캡슐화 encapsulation) , 몰라도 되는 것은 내가 숨기겠다(노출을 안하겠다)는 뜻
//// - 다형성 << polymorphism (poly + morphism) , 겉은 동일한데 상황에 따라서 기능이 다르게 동작
//
//// 오버로딩(overloading) = 함수 이름의 재사용
//// 오버라이딩(overriding) = 부모 클래스의 함수를 자식 클래스에서 재정의
//
//
//// 순수 가상 함수 -> 구현은 없고 인터페이스만 전달하는 용도로 사용하고 싶은 경우 사용, 
//// 순수 가상 함수를 한개라도 넣는 순간 추상 클래스가 됨.
//// 추상 클래스 -> 구현부 자체는 내가 만들 생각도 없고 클래스 자체는 추상적으로 존재하는 아이이기 때문에 얘만 독단적으로 살아갈 수 x
//// 해서 반드시 상속을 받아가지고 다른 애들을 통해서 간접적인 인생을 살아가는 클래스
//
//// move라는 것에 순수 가상 함수를 적용 했다면 혹시라도 Knight에서 move를 오버라이딩을 하지않는다면 오류 발생
//// 순수 가상 함수를 물려받았는데 구현을 안하면 안됨!!!!!!
//
//class Player
//{
//public:
//    // 이렇게 안해주면(virtual = 가상함수) 일반 함수는 그냥 정적 바인딩이 되어버림.
//    // MovePlayer(&k1); -> Player Move()로 뱉음 :(
//    // 가상 함수 해주면 동적 바인딩이 되어서 "Knight Move()"로 뱉음 -> 어떤 타입이었는지에 따라 해당하는 함수 실행
//    // 상위(부모) 클래스에 virtual를 해주면 상속 받은 모든 애들에게도 void Move() 앞에 virtual이 붙음
//    // 어지간하면 생략하지 않고 자식 클래스에다가도 꼼꼼하게 붙여주자!!
//    // 가상 함수 동작 원리 -> 가상 함수 테이블이 생김 (stack에 할당 되겠지??)
//    // vftable (virtual function table)
//    // vftable [주소1 | 주소2 | 주소3]
//    // 예를 들어 Player타입이면 주소1번, Knight타입이면 주소2번를 넣어줌
//    // 이런식으로 실질적으로 어떤 주소값을 여기다 기입해가지고 그 주소를 찾아가서 내가 원하는 함수를 호출
//    //virtual void Move() { cout << "Player Move()" << endl; }
//
//
//    // 둘 다 동일 (순수 가상 함수)
//    virtual void Move() = 0;
//    //virtual void Move() abstract;
//    
//
//    // 소멸자 같은 경우도 꼭 virtual로 만들어줘야 됨. (메모리 누수 발생할 수 있음)
//    virtual ~Player() {}
//
//public:
//    int _hp = 100;
//};
//
//class Knight : public Player
//{
//public:
//    //내 위에 있는 플레이어는 과연 virtual를 붙였는지 헷갈릴 수 있고 애매할 수 있으니깐 override를 붙여줌 (실수의 여지 방지를 위해 탄생.)
//    // override가 의미하는 바: 내가 가상함수이기는 한데 부모님이 만들어준 가상함수를 나도 override해서 재정의를 하겠다.
//    // 그래서 혹시라도 내가 override키워드를 붙였는데 부모님이 virtual를 빼먹었다면 바로 얘가 알려줌.
//    /*virtual*/ void Move() override { cout << "Knight Move()" << endl; }
//
//public:
//    int _stamina = 200;
//};
//
//// 바인딩 (Binding) = 묶는다
//// - 정적 바인딩 (static binding = 컴파일 시점 결정) - 일반 함수
//// - 동적 바인딩 (dynamic binding = 실행 시점 결정)
//void MovePlayer(Player* player)
//{
//    player->Move();
//}
#pragma endregion
#pragma region 멤버 변수 초기화
//class Player
//{
//public:
//    Player()
//    {
//        cout << "Player()" << endl;
//    }
//
//    ~Player()
//    {
//        cout << "~Player()" << endl;
//    }
//};
//
//
//class Inventory
//{
//public:
//    Inventory()
//    {
//        cout << "Inventory()" << endl;
//    }
//
//    Inventory(int a)
//    {
//        _a = a;
//        cout << "Inventory(int)" << endl;
//    }
//
//    ~Inventory()
//    {
//        cout << "~Inventory()" << endl;
//    }
//public:
//    int _a = 0; // 초기화 (3)
//};
//
//// 초기화 해주는 이유 : 기존의 쓰레기값을 가지고 있을 수는 없자너..
//
//class Knight : public Player
//{
//public:
//    // 매번마다 똑같은 코드를 반복하기 어렵다.. (초기화 해줄 것이 많음)
//    // -> 생성자끼리 서로 호출할 수 있는 문법 존재 (ex. Knight(0))
//    Knight() : /*Knight(0), */_hp(0), _inventory(100), _hpRef(_hp), _hpConst(_hp)  // 초기화 (1) -> 여기서 하는 것이 조금 더 효율성이 좋음 (두번 처리할 확률이 없어짐.)
//        
//    // (1) 과 (2) 의 차이점?
//    // - (1) 멤버 초기화 리스트를 사용하는 방식
//    // -- 멤버 변수들이 객체가 생성될 때 즉시 초기화되므로 효율적입니다.
//    // - (2) 생성자 본문에서 초기화하는 방식
//    // -- 멤버 변수들이 먼저 기본 생성자로 초기화된 후, 생성자 본문에서 다시 할당됩니다.
//    // 따라서 두 번 초기화하는 오버헤드가 발생할 수 있습니다.
//
//    // (3) 방식도 괜찮음, (2)방식이 젤 별로.
//
//    // - (1) 방식
//    /*
//    Player() (기반 클래스 생성자)
//    Inventory(int) (멤버 객체 초기화)
//    Knight() (파생 클래스 생성자)
//    ~Knight() (파생 클래스 소멸자)
//    ~Inventory() (멤버 객체 소멸자)
//    ~Player() (기반 클래스 소멸자)
//    */
//
//    // - (2) 방식
//    /*
//    Player() (기반 클래스 생성자)
//    Inventory() (멤버 객체 기본 생성자)
//    Inventory(int) (멤버 객체 재할당)
//    Knight() (파생 클래스 생성자)
//    ~Knight() (파생 클래스 소멸자)
//    ~Inventory() (멤버 객체 소멸자)
//    ~Player() (기반 클래스 소멸자)
//    */
//
//    /*
//        선처리 영역
//        Player()
//        _inventory = Inventory()
//    */
//    {   
//        //_hp = 0; // 초기화 (2)
//        //_inventory = Inventory(100);
//        cout << "Knight()" << endl;
//    }
//
//    Knight(int hp) : _hp(hp), _hpRef(_hp), _hpConst(_hp)
//    {
//        cout << "Knight(int)" << endl;
//    }
//
//    ~Knight()
//    {
//        cout << "~Knight()" << endl;
//    }
//
//public:
//    int _hp;
//    int _defence = 20; // 초기화 (3) , 모든 생성자에서 다 같이 처리 가능.
//
//    // 말도 안되지만 아래 2개와 같은 경우가 있다면?
//    // 참조값은 포인터와는 다르게 누군가를 꼭 가리키고 있어야 되고
//    // const값도 처음에 세팅이 되는 그 값만 유지할 수 있고 바뀔 수 없다는 점이 있어서
//    // (1)에서만 초기화 가능
//    int& _hpRef;
//    const int _hpConst;
//
//    //Inventory* _inventory; // 포인터로 들고 있는다는 것은 언젠가 이 주소를 누군가가 가리키게끔 세팅해주겠지라는 의미를 내재
//    Inventory _inventory; // 이렇게 하면 Knight를 만드는 순간에 이 인벤토리도 같이 스택에 만들어짐 (메모리 영역 확보됨)
//};
//
////Knight k2; // 전역변수 -> 메모리 어딘가에 만들어질 것이고 끝나는 순간까지 유지
#pragma endregion
#pragma region 연산자 오버로딩
//// 연산자 오버로딩 -> 거의 사용할 일 x , 연산자를 커스텀해서 다룰 수 있다 정도로만 인지하세요!
//// -  멤버 연산자 함수 버전
//// -- a op b 형태에서 왼쪽을 기준으로 실행 (a가 반드시 클래스 타입이어야 됨.) -> 10 + pos1 이런식으로 반대로는 안됨.
//// -  전역 연산자 함수 버전
//// -- a op b 형태라면, a/b 모두를 연산자 함수의 피연산자로 사용
//
//class Pos
//{
//public:
//
//    Pos()
//    {
//
//    }
//
//    /*explicit*/ Pos(int b)
//    {
//        x = b;
//        y = b;
//    }
//
//    // 멤버 연산자 함수 버전
//    Pos operator+(const Pos& b)
//    {
//        Pos pos;
//        pos.x = x + b.x;
//        pos.y = y + b.y;
//
//        return pos;
//    }
//
//    Pos operator+(int b)
//    {
//        Pos pos;
//        pos.x = x + b;
//        pos.y = y + b;
//
//        return pos;
//    }
//
//    bool operator == (const Pos& b)
//    {
//        return x == b.x && y == b.y;
//    }
//
//    // 대입 연산자 -> 재정의해서 오버로딩 가능 (이건 좀 중요.)
//   /* void operator=(int b)
//    {
//        x = b;
//        y = b;
//    }*/
//
//    // (참고)
//    // pos1 = pos2 = pos3 이렇게 3단이상까지 가능하게 하려면.. 
//    /*Pos& operator=(int b)
//    {
//        x = b;
//        y = b;
//
//        return *this;
//    }*/
//
//    int x = 1;
//    int y = 1;
//
//};
//
//// 전역 연산자 함수 버전
//Pos operator+(int a, const Pos& b)
//{
//    Pos pos;
//    pos.x = a + b.x;
//    pos.y = a + b.y;
//
//    return pos;
//
//}

#pragma endregion
#pragma region static과 싱글톤
//// struct vs class
//// C#에서 struct와 class는 천지차이 struct는 복사타입, class는 참조타입으로 동작
//// C++에서는 그런 차이가 거의 없음
//// -> 접근지정자를 입력해두지 않으면 struct는 public으로 class는 private로 되어있다는 차이점만 존재
//// 접근지정자 차이로 선택을 하지 마라!! -> struct는 여러가지 데이터를 모아가지고 관리하는 용도로 사용하고, class는 객체 지향 용도로 활용해라!!
//
//
//// 모든 애들이 다 공용으로 똑같은 값을 들고 있어야 된다고 하면 굳이 메모리를 차지해서 낭비할 필요가 없다!!
//// 모든 Marine이 공용으로 쓰는 것? -> static으로 관리해!!
//
//// static을 통해서 어떤 마린 객체 하나하나의 종속적인 데이터가 아니라 모든 마린들이 다 공용으로 활용하는 공공제가 됨.
//
//class Marine
//{
//public:
//    // 특정 마린 객체와 연관
//    void TakeDamage(int damage)
//    {
//        hp -= damage;
//    }
//
//    // 특정 마린 객체와 무관
//    static void SetAttack(int value)
//    {
//        // 조심할 점: 무관한 것은 무관한 것을 건드려도 되고 유관한 것은 유관한 것을 건드려도 된다. 단 반대는 안됨!!!
//    }
//
//public:
//    // 특정 마린 객체와 연관
//    int hp = 40;
//    
//    //특정 마린 객체와 무관
//    // static은 여기다가 초기화 하는 것이 아님!!
//    static int attack;
//
//};
//
//// 밖에서 등장하기 때문에 밖에서 초기화
//int Marine::attack = 6;
//
//
//// 사용 예
//class Player
//{
//public:
//    Player()
//    {
//        id = s_idGenerator++;
//    }
//public:
//    int id;
//    static int s_idGenerator;
//};
//
//int Player::s_idGenerator = 1;
//
//// 사용 예2 -> 지역 변수 앞에 static을 붙이면?
//// 이렇게 하면 태생부터 스택에 들어가는 애가 아니고 메모리 영역 어딘가에다가 스태틱 변수가 위치해서 일단은 거기서 만들어짐
//// 다만 맨 처음으로 GenerateId()가 첫번째로 호출이 될 때 이 10으로 초기화 하는 부분만 그때 한번만 호출이 되고 그 다음부터는 
//// 그냥 전역변수처럼 쭉 활용이 된다는 특징이 있다.
//
//int GenerateId()
//{
//    static int s_id = 10;
//    return s_id++;
//}
//
//
//
//// 자료구조&알고리즘 ->자료를 내가 어떻게 메모리에 들고 있을 지 그리고 그것을 어떤한 알고리즘에 의해가지고 가공을 시킬지 연구하는 학문
//// 디자인 패턴 -> 어떤 식으로 코드를 구성해야 좋을지를 다루는 학문
//// - 싱글톤, 옵저버, 콤포넌트,....
//
//// 싱글톤 -> 정말 딱 1개만 존재하고 어디서든 사용할 수 있는 [매니저] 클래스
//
//class UserManager
//{
//public:
//    static UserManager* GetInstance()
//    {
//        static UserManager um;
//        return &um;
//    }
//
//public:
//    void AddUser() { _userCount++; }
//    int GetUserCount() { return _userCount; }
//
//private:
//    int _userCount = 0;
//};
//
//#define GET_MANAGER (UserManager::GetInstance()) // 치기 귀찮을 때
#pragma endregion
#pragma region 객체 지향 마무리 -> 다중 상속 (비추), 인터페이스

// C++의 경우 상속을 여러개 받아줄 수 있다.
// 다중상속을 처음에는 허락을 해줬지만 여러 이유로 인해 노답임을 깨달음 -> 똑같은 함수가 여러번 등장한다면 뭘 써야되는거지??
// 그래서 다중상속을 쓸 일이 있다는 것은 설계 오류다 판단!
// 대부분의 현대 언어는 다 막아놓음.
// 그럼에도 불구하고 인터페이스라는 조금 다른 개념은 씀. (문법 자체는 다중상속)


class IFly
{
    virtual void Fly() = 0;
    virtual void Land() = 0;

};

class Object
{
    //virtual void Shout() = 0; // 순수 가상 함수
};

class Player : public Object, public IFly // IFly라는 애를 구현할 애는 fly랑 land라는 함수를 지원해야돼!
{
public:

    Player() {}
    ~Player() {}

    virtual void  Fly() override {}
    virtual void  Land() override {}

    virtual void Shout() {}

    void SetHp(int hp) { this->hp = hp; }
    void Move() {}

private:
    int hp = 10;
};

void AddObject(Player* player)
{
    player->Shout();
}

// 왜 굳이 힘들게 인터페이스?
// fly만 받을 수 있는 테스트 함수 이용가능
void FlyTest(IFly* fly)
{

}
#pragma endregion
#pragma endregion


int main()
{

#pragma region 전체
#pragma region 챕터1
    // 지역변수는 stack으로 관리.

    //ch = 'a';
    //speed = 3.5; // 이렇게 하면 더블로 인식한 것을 float에다가 넣어줌.
    //speed = 3.5f; // 이렇게 해야 바로 float 형식으로 알아먹음.

    //playSound = 7;

    //cout << (int)ch << " " << playSound << endl;// endl 줄바꿈.


    // 별찍기
    // *****
    // *****
    // *****
    // *****
    // *****

    /*int N;
    cin >> N;*/

    // 방식 1

    /*for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cout << "*";
        }

        cout << endl;
    }*/

    // 방식 2

    //for (int i = 0; i < N; i++)
    //{
    //    string stars(N, '*'); // N번 '*' 문자열 생성
    //    cout << stars << endl;
    //}

    // 구구단
    /*for (int i = 2; i < 10; i++)
    {
        for (int j = 1; j < 10; j++)
        {
            cout << i << " * " << j << " = " << i * j << endl;
        }

        cout << "------------" << endl;
    }*/

    // 가위 바위 보 -> 가위(0) 바위(1) 보(2) 이런식으로 하면 유지보수
    // 힘드니깐 아래와 같이 해주기
    // 방식 1
    const int SCISSORS = 0;
    const int ROCK = 1;
    const int PAPER = 2;
    // 방식 2 (이걸 추천!)
    enum ENUM_GBB
    {
        GBB_SCISSORS,
        GBB_ROCK,
        GBB_PAPER
    };


#pragma endregion
#pragma region 텍스트 RPG
    /*srand((unsigned int)time(0));
    EnterLobby();*/
#pragma endregion
#pragma region 챕터2

    /*Test2();
    GTest = 10;*/

#pragma endregion
#pragma region 챕터3

    //// C# int[] arr;
    //int arr[5] = { 1, 2, 3, 4, 5 }; // 만약에 인덱스를 초과한다면 크래쉬 발생하겠지? (메모리 침범)

    //// 그래서 나중에 배열의 칸이 바뀔 수 있으므로 5부분을 int MaxLength = 5 이런식으로 관리해줌. 

    //for (int i = 0; i < 5; i++)
    //{
    //    arr[i] = i + 10;
    //}

#pragma endregion
#pragma region 배열 실습

    //SetCursorOnOff(false);
    ////MovePlayer(3, 2);

    //while (true)
    //{
    //    // 입력
    //    HandleKeyInput();

    //    // 로직
    //    HandleMove();

    //    // 출력
    //    PrintMap2D();
    //}

#pragma endregion
#pragma region 포인터 이론

//// 데이터 오염은 프로그램이 할당된 메모리 범위를 벗어나 다른 메모리를 수정하거나 읽을 때 발생하는 오류를 말합니다.
//// 이런 오류는 프로그램의 불안정성을 유발하고, 심각한 경우 보안 취약점으로 이어질 수 있습니다.

//// 막 몇년동안 버그가 안 생기다가 지뢰 잘못 밟아서 펑 터질 수 있음.(원인 유발자가 아니라 찾기 hard)
//// C++과 포인터와 관련된 주소값이 들어가기 시작하면 조심해야됨!!! (위와 같은 오류가 발생하면 찾기 hard)

//int hp = 100;

//// 포인터의 핵심 : 주소값을 건네줄 수 있어서 원본 데이터를 고쳐줄 수 있음.

//// 포인터 : [타입]* [이름]; (void도 타입으로 가능)
//// void* 이렇게 하면 주소값을 담아두는 것으로만 쓰겠다를 의미
//// 주소값을 담는 바구니
//// 변수의 크기 : 
//// 주소체계가 다 8바이트로 되어있기 때문에(64비트) 이 포인터라는 표시를 하는 순간
//// 얘는 무조건 8바이트짜리 변수라고 생각하면 된다. (타입 상관 없이)
//// 타입이 의미하는 바 : 주소값을 타고가면 무엇이 있느냐? -> 타고 갔다고 100프로 이 타입이 있는 것은 x
//// 그냥 주장만 그렇게 하는 것임 문법적으로 아닐 수 있음. (아니면 난리남.)
//int* ptr = &hp; // &: 요 아이의 주소값을 알려주세요!!

//// (*ptr) : 해당 주소로 이동을 뿅 하는 느낌.

//// ptr += 1; // 만약에 주소값이 100이라면 104로 이동 (왜?? int는 4바이트니깐 주소값 + 4 * 1만큼 이동)
//// 즉, 단순하게 숫자를 더한다기 보단 다음칸으로 이동해라라는 의미를 지님.

//int** pptr = &ptr; // 포인터도 포인터를 가리킬 수 있음 (무한으로 가능.)
//// 양파 까기: (int*)* -> (int*) -> (int) : 최종적으로 타고 가면 주소가 아니라 int가 나오겠구나.


//AddHp(ptr, 10);

//cout << *ptr << endl;
#pragma endregion
#pragma region 포인터 연산

//// 포인터는 시작 주소를 가지고 있음.

//// 포인터 연산
//// - 주소 연산자 (&)
//// - 산술 연산자 (+-)
//// - 간접 연산자 (*)
//// - 간접 멤버 연산자 (->)

////int a = 10;
////int b = 20;
////Swap(&a, &b);

////cout << a << endl;
////cout << b << endl;

////int numbers[100] = { 1, 2, 3, 4, 5, 6 };

//////int* ptr = &numbers[0];
////int* ptr = numbers; // 이렇게 해도 됨 (C++에서 배열의 이름을 호출하면 시작 주소를 얻어올 수 있다.)
////*(ptr + 3) = 666; // 내가 가리키고 있는 다음 칸인 실질적으로 (4 * 3)byte가 증가한 주소값을 가리킴
////// ptr[3] = 666; // 축약형
////ptr += 1;
////*ptr = 777;

//StatInfo monster;
//monster.hp = 100;
//monster.attack = 10;
//monster.defence = 1;
//StatInfo* ptr = &monster;

//// 똑같은 것임. (아래가 좀 더 쓰기 좋겠지??)
//cout << (*ptr).hp << endl;
//cout << ptr->hp << endl;
#pragma endregion
#pragma region 포인터 연산 실습
/*StatInfo player;
    player = CreatePlayer();



    StatInfo monster;
    CreateMonster(&monster);

    Battle(&player, &monster);*/
#pragma endregion
#pragma region 문자열
    //// 옛날 스타일
    //// 0이라는 키를 만날 때까지 쭉 문자열을 표시. 
    //// 이렇게 null 처리를 해줘야지만 얘가 끝났음을 파악할 수 있음.
    //// 이래서 6칸짜리 배열인 것임!
    ////char str[] = { 'H', 'e', 'l', 'l', 'o' , '\0'};


    //// (참고)
    //// const의 위치에 따라서 포인터가 가리키는 값을 상수로 만들 것인지
    //// 포인터 차제를 상수로 만들 것인지 차이가 있다
    //const char* a ; //이 선언은 a가 "상수 문자를 가리키는 포인터"라는 의미입니다.
    //// 포인터 a가 가리키는 값(문자)은 변경할 수 없습니다. 하지만 포인터 a 자체는 다른 메모리 주소를 가리키도록 변경할 수 있습니다.

    //// 앞 뒤로 둘 다 쓰일 수 있음.

    //// (결론)
    //// 별표 앞에 const가 있다면? -> 가리키고 있는 원본을 상수화 (즉, 타고 간 다음의 애를 건들지 마!)
    //// 별표 뒤에 const가 있다면? -> 가리키는 포인터를 상수화 (태워줄 애를 건들지 마!)


    //// 결론: 문자열이란? -> 어떤 캐릭터 타입의 배열을 만든 다음에 거기에다가 문자를 넣어주고 끝났다는
    //// 의미로 0이라는 값을 넣어주는 것

    //const int BUF_SIZE = 100;

    //char a[BUF_SIZE] = "Hello";
    //char b[BUF_SIZE] = "World";

    //int len = strlen(a); // null은 빼고 알려줌
    ////int len = StrLen(a);
    //cout << len << endl;


    //// 알 필요 없지만 에러 방지를 위해서 -> 메모리 초과 경고 관련 
    //#pragma warning(disable: 4996)

    //char c[BUF_SIZE];

    ////strcpy(c, a); // c라는 목적지에다가 a를 복사
    //StrCpy(c, a);
    //cout << c << endl;

    ////cout << strcat(a, b) << endl; // a에 b를 덧붙임.
    //cout << StrCat(a, b) << endl; // a에 b를 덧붙임.

    // C++에서 cout을 사용하여 문자열을 출력할 때,
    // 만약 문자열 포인터를 출력하면 그 문자열의 내용이 출력됩니다.
    // 이는 cout이 char* 를 특별히 처리하기 때문입니다.
#pragma endregion
#pragma region 참조
//StatInfo player = { 100, 10, 1 }; // 바로 초기화 , (1)
//PrintByCopy(player);
//PrintByPointer(&player);
//
//StatInfo* ptr = &player; // (2)
////StatInfo* ptr = nullptr;
//
//
//StatInfo& ref = player; // 사용하는 거는 (1)번과 유사하지만 
//// 내부적으로 구현이 되는 코드의 동작 원리는 (2)번과 유사
//// 즉, 주소값을 이용해가지고 원본을 건드린다에 가깝
//
//PrintByRef(OUT player);
#pragma endregion
#pragma region 로또 번호 생성기
//srand((unsigned)time(0));
//int lotto[6];
//ChooseLotto(lotto);
//
//for (int i = 0; i < 6; i++)
//    cout << lotto[i] << endl;
#pragma endregion
#pragma region 달팽이문제 
//cin >> N;
//
//SetBoard();
//
//PrintBoard();
#pragma endregion
#pragma region 객체지향 개론
//// C#이랑 C++의 차이점
    //// C++에서는 struct랑 class 차이가 거의 x하고 꼭 동적할당(new)을 해야 되진 않고
    //// 이렇게 스택 영역에다가도 얼마든지 객체를 만들 수 있음

    //// 객체 (instance)
    //// 4개다 같은 것임.
    //Knight k1(100, 10, 1);
    //Knight k2 = Knight(100, 10, 1);
    //Knight k3{ 100, 10, 1 };
    //Knight k4 = { 100, 10, 1 };

    //// 복사 생성자 사용법
    //Knight k5(k1);

    //k1.Attack();
    //k1.Die();
    //k1.HealMe(10);

    //cout << k1.hp << endl;
#pragma endregion
#pragma region 상속성
    //// 캐스팅이란
    //// 어떤 변수가 있는 상태에서 다른 타입으로 변신을 시켜주는 것
    //int a = 10;
    //float b = (float)a;

    //Knight k1;

    //// 아래와 같이 하면 데이터 손실이 없이 왔다갔다 가능
    //// Player 타입이라고 했으면 공통된 부분인 영역만 접근이 가능하지만
    //// Knight 타입의 포인터로 인지를 했다고 다시 정정하면 모든 영역에 다시 접근 가능
    //
    //// Player 타입의 포인터 p1을 선언하고, k1의 주소를 p1에 할당합니다. 
    //// Player 타입의 포인터로 Knight 객체를 가리킬 수 있다는 것을 보여줍니다.
    //// 업캐스팅
    //Player* p1 = &k1;
    //// 명시적 캐스팅을 사용하여 Player* 타입을 Knight* 타입으로 변환합니다.
    //// 다운캐스팅
    //Knight* p3 = (Knight*)p1;

    //Mage m1;

    //// Player 타입의 포인터로 Mage 객체를 가리킬 수 있다는 것을 보여줍니다.
    //Player* p2 = &m1;

    //Fight(&k1, &m1);
#pragma endregion
#pragma region 은닉성
/*Car c;

    Knight k1;

    k1.SetHp(100);*/
#pragma endregion
#pragma region 다형성
    //Knight k1;
    //
    //k1.Move();
    //MovePlayer(&k1);
#pragma endregion
#pragma region 멤버변수 초기화
//    {
//        Knight k1; // 지역 변수 특성상 괄호 범위 안에서만 유효
//    }
//    
//    // C#의 아래방식은 C++의 동적 할당으로 관리하는 것과 동일
//    // C# Knight k1 = new Knight();
//    // C++ Knight* k1 = new Knight(); // 동적 할당
//
//
//
//    // 아래 2방식의 차이점
//    // 즉, 일반적인 정수 (ex. int)가 아니라 요런 class타입이나 struct 같은 애들로 인해서
//    // 생성자 소멸자가 같이 개입을 하는 순간에 아래의 2방식은 성능 차이가 발생할 수 있다!!!
//    for (int i = 0; i < 10; i++)
//    {
//        Knight k3; // for문 하나 돌때마다 생성과 소멸이 반복
//        cout << k3._hp << endl;
//    }
//
//    // 아래의 경우 k4가 생성이 되고 for문을 돌 때까지는 애가 소멸되지 않음
//
//    Knight k4;
//    for (int i = 0; i < 10; i++)
//    {
//        cout << k4._hp << endl;
//    }
//
#pragma endregion
#pragma region 연산자 오버로딩
//int a = 10;
//int b = 20;
//int c;
//
//c = a; // 대입 연산
//
//
//// 생성
//Pos pos4(10);
//Pos pos5 = 20; // 같은 줄에 선언과 값을 넣어주는 것은 생성자를 통해서 우리가 무언가를 하는 행동.
//
//
//Pos pos1;
//Pos pos2;
//
//// 대입 -> 대입이라는 것은 다 만들어진 다음에 우리가 어떤 값을 넣어주는 것을 말함
//// 대입 연산자를 주석처리하면 생성자로 감. (생성할 때만 얘를 받아주면 좋겠어!!! -> 간접적으로 컴파일러가 눈치껏 해주는 것을 막고 싶어!! (explicit))
//pos1 = 10;
//pos2 = 20;
//
//Pos pos3 = pos1 + 10;
////Pos pos4 = pos1.operator+(pos2);
#pragma endregion
#pragma region static과 싱글톤
/* Marine m1;
    m1.hp = 40;
    m1.TakeDamage(10);

    Marine m2;
    m2.hp = 10;

    Marine::attack = 7;

    Marine::SetAttack(10);

    for (int i = 0; i < 10; i++)
        UserManager::GetInstance()->AddUser();

    cout << GET_MANAGER->GetUserCount() << endl;*/
#pragma endregion
#pragma region 객체 지향 마무리 -> 다중 상속 (비추), 인터페이스
    /*Player p;
    FlyTest(&p);*/
#pragma endregion
#pragma endregion


    
    
}



#pragma region 텍스트 RPG

//void EnterLobby()
//{
//    while (true)
//    {
//        cout << "---------------------" << endl;
//        cout << "로비에 입장했습니다!" << endl;
//        cout << "---------------------" << endl;
//
//        // 플레이어 직업 선택
//        SelectPlayer();
//
//        cout << "---------------------" << endl;
//        cout << "(1) 필드 입장 (2) 게임 종료" << endl;
//        cout << "---------------------" << endl;
//
//        int input;
//        cin >> input;
//
//        if (input == 1)
//        {
//            EnterField();
//        }
//        else
//        {
//            return;
//        }
//
//    }
//}
//
//void SelectPlayer()
//{
//
//    while (true)
//    {
//        cout << "---------------------" << endl;
//        cout << "직업을 골라주세요!" << endl;
//        cout << "(1) 기사 (2) 궁수 (3) 법사" << endl;
//        cout << "> ";
//
//        int choice;
//        cin >> choice;
//
//        //playerType = (PlayerType) choice; // 이렇게도 가능!
//
//        if (choice == PT_Knight)
//        {
//            cout << "기사 생성중..." << endl;
//            playerStat.hp = 150;
//            playerStat.attack = 10;
//            playerStat.defence = 5;
//            playerType = PT_Knight;
//            break;
//        }
//        else if (choice == PT_Archer)
//        {
//            cout << "궁수 생성중..." << endl;
//            playerStat.hp = 100;
//            playerStat.attack = 15;
//            playerStat.defence = 3;
//            playerType = PT_Archer;
//            break;
//        }
//        else if (choice == PT_Mage)
//        {
//            cout << "법사 생성중..." << endl;
//            playerStat.hp = 80;
//            playerStat.attack = 25;
//            playerStat.defence = 0;
//            playerType = PT_Mage;
//            break;
//        }
//
//    }
//
//
//
//}
//
//void EnterField()
//{
//    while (true)
//    {
//        cout << "---------------------" << endl;
//        cout << "필드에 입장했습니다!" << endl;
//        cout << "---------------------" << endl;
//
//        cout << "[Player] HP : " << playerStat.hp << " / ATT : " << playerStat.attack << " / DEF : " << playerStat.defence << endl;
//
//        // 몬스터 스폰
//        CreateRandomMonster();
//
//        cout << "---------------------" << endl;
//        cout << "(1) 전투 (2) 도주" << endl;
//        cout << "> ";
//
//        int input;
//        cin >> input;
//
//        if (input == 1)
//        {
//            EnterBattle();
//
//            if (playerStat.hp == 0)
//                return;
//        }
//        else
//        {
//            return;
//        }
//    }
//
//}
//
//void CreateRandomMonster()
//{
//    int randomChoice = 1 + (rand() % 3); // 1~ 3만2천얼마 사이 rand 시드 값 필요 (srand)
//
//    switch (randomChoice)
//    {
//
//    case MT_Slime:
//        cout << "슬라임 생성중...! (HP:30 / ATT:2 / DEF:0)" << endl;
//        // 참고로 이런 것들은 이렇게 하드코딩할 일은 솔직히 없을 것이고 나중에 가면 이거를 Excel이라거나 Json, XML 같은 파일 형태로 빼가지고 기획자가 관리
//        monsterStat.hp = 30;
//        monsterStat.attack = 2;
//        monsterStat.defence = 0;
//        monsterType = MT_Slime;
//        break;
//    case MT_Orc:
//        cout << "오크 생성중...! (HP:40 / ATT:10 / DEF:3)" << endl;
//        monsterStat.hp = 40;
//        monsterStat.attack = 10;
//        monsterStat.defence = 3;
//        monsterType = MT_Orc;
//        break;
//    case MT_Skeletion:
//        cout << "해골 생성중...! (HP:80 / ATT:15 / DEF:5)" << endl;
//        monsterStat.hp = 80;
//        monsterStat.attack = 15;
//        monsterStat.defence = 5;
//        monsterType = MT_Skeletion;
//        break;
//
//    }
//}
//
//void EnterBattle()
//{
//    while (true)
//    {
//        int damage = playerStat.attack - monsterStat.defence;
//        if (damage < 0)
//        {
//            damage = 0;
//        }
//
//        // 선빵
//        monsterStat.hp -= damage;
//        if (monsterStat.hp < 0)
//        {
//            monsterStat.hp = 0;
//        }
//        cout << "몬스터 남은 체력 : " << monsterStat.hp << endl;
//
//        if (monsterStat.hp == 0)
//        {
//            cout << "몬스터를 처치했습니다." << endl;
//            WaitForNextKey();
//            return;
//        }
//
//        // 반격
//        damage = monsterStat.attack - playerStat.defence;
//        if (damage < 0)
//        {
//            damage = 0;
//        }
//
//        playerStat.hp -= damage;
//        if (playerStat.hp < 0)
//        {
//            playerStat.hp = 0;
//        }
//
//        cout << "플레이어 남은 체력 : " << playerStat.hp << endl;
//
//        if (playerStat.hp == 0)
//        {
//            cout << "당신은 사망했습니다... GAME OVER" << endl;
//            WaitForNextKey();
//            return;
//        }
//    }
//}
//
//void WaitForNextKey()
//{
//    cout << "계속하려면 1을 눌러주세요." << endl;
//    cout << "> ";
//
//    int input;
//    cin >> input;
//
//    system("cls"); // 내용 정리
//}


#pragma endregion



