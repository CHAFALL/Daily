#include "Helper.h"
//#include <iostream>
//using namespace std;
#include <windows.h> // �ְܼ� ���õ� ���� ��� ����.

#pragma region é��2
// �����θ� cpp���ٰ�

//int GTest; // �۷ι�(G������)
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



// ���� �÷��̾ �ٶ󺸰� �ִ� ����
MoveDir GMoveDir;

void HandleKeyInput()
{
    // ���� ���ӿ��� cin, cout���� Ű���� �Է� ��� �Ұ�
    // (�ؽ�Ʈ RPG���� �ƿ� ���α׷��� ���絵 ������ ��������)
    // � Ű�� �Է����� �ʴ��� �갡 ��� �ٻڰ� �����̸鼭 �� ���� ���� ������ ����� �ϹǷ�
    // �Լ� �߿��� ���ŷ, ����ŷ(�̰� �̿�!) ����� �ִ�.

    // ������ -> Ű���带 ������ �´� �� ������ üũ�� �ϴ� ���� �ƴ϶� �׳� ������ �־ �̰�
    // ��� ���� ������ ����. -> HandleMove()�Լ����� ó������ ����.

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
    // ���߿� ������ API���� �ٷ� ����.
    // ǥ�ؿ��� �����ϴ� �͵��� �̷��� ::�� �ٿ��� ���ִ� ��찡 ����. (���� ������ ������ ǥ��)
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

