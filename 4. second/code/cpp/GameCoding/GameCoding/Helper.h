#pragma once


#pragma region 챕터2

// #pragma once가 해주는 역할 : define이 되어 있으면 넘어가고 안 되어있으면 define 해줘 (중복 제거)

// 선언하는 부분을 대부분 header 파일에다가 넣어줌
// 여기에 있는 것을 include로 불러오는 곳에 복붙을 해줌!!!!

// 자유롭게 원하는 것을 넣을 수 있되 조심! (최대한 간략하게 유지하자!!) -> 불필요한 것이 복붙되면.. 느려짐.

//void Test(int);
//void Test2();
//
//
//// 해당 변수가 나중에 등장을 할 것이다를 표현 (extern)
//extern int GTest;

#pragma endregion

enum MoveDir
{
    MD_NONE,
    MD_LEFT,
    MD_RIGHT,
    MD_UP,
    MD_DOWN,
};

void HandleKeyInput();

void SetCursorPosition(int x, int y);

void SetCursorOnOff(bool visible);

extern MoveDir GMoveDir;