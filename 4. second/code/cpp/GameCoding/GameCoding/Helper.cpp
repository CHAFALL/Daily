#include "Helper.h"
//#include <iostream>
//using namespace std;
#include <windows.h> // 콘솔과 관련된 것을 들고 있음.

#pragma region 챕터2
// 구현부를 cpp에다가

//int GTest; // 글로벌(G컨벤션)
//
//void Test(int)
//{
//	Test2();
//}
//
//void Test2()
//{
//	cout << "Hello World" << endl;
//}
#pragma endregion



// 현재 플레이어가 바라보고 있는 방향
MoveDir GMoveDir;

void HandleKeyInput()
{
    // 실제 게임에선 cin, cout으로 키보드 입력 사용 불가
    // (텍스트 RPG에선 아예 프로그램이 멈춰도 문제가 없었지만)
    // 어떤 키를 입력하지 않더라도 얘가 계속 바쁘게 움직이면서 맵 같은 것을 렌더링 해줘야 하므로
    // 함수 중에선 블록킹, 논블록킹(이걸 이용!) 방식이 있다.

    // 문제점 -> 키보드를 눌렀다 뗏다 할 때마다 체크를 하는 것이 아니라 그냥 누르고 있어도 이게
    // 계속 여기 안으로 들어옴. -> HandleMove()함수에서 처리해줄 것임.

    if (::GetAsyncKeyState(VK_LEFT) & 0x8000)
        GMoveDir = MD_LEFT;
    else if (::GetAsyncKeyState(VK_RIGHT) & 0x8000)
        GMoveDir = MD_RIGHT;
    else if (::GetAsyncKeyState(VK_UP) & 0x8000)
        GMoveDir = MD_UP;
    else if (::GetAsyncKeyState(VK_DOWN) & 0x8000)
        GMoveDir = MD_DOWN;
    else
        GMoveDir = MD_NONE;
}

void SetCursorPosition(int x, int y)
{
    // 나중에 윈도우 API에서 다룰 것임.
    // 표준에서 제공하는 것들은 이렇게 ::을 붙여서 써주는 경우가 많다. (내가 만들지 않음을 표시)
    HANDLE output = ::GetStdHandle(STD_OUTPUT_HANDLE);
    COORD pos = { (short)x, (short)y };
    ::SetConsoleCursorPosition(output, pos);
}

void SetCursorOnOff(bool visible)
{
    HANDLE output = ::GetStdHandle(STD_OUTPUT_HANDLE);
    CONSOLE_CURSOR_INFO cursorInfo;
    ::GetConsoleCursorInfo(output, &cursorInfo);
    cursorInfo.bVisible = visible;
    ::SetConsoleCursorInfo(output, &cursorInfo);
}

