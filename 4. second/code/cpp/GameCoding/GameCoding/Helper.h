#pragma once


#pragma region é��2

// #pragma once�� ���ִ� ���� : define�� �Ǿ� ������ �Ѿ�� �� �Ǿ������� define ���� (�ߺ� ����)

// �����ϴ� �κ��� ��κ� header ���Ͽ��ٰ� �־���
// ���⿡ �ִ� ���� include�� �ҷ����� ���� ������ ����!!!!

// �����Ӱ� ���ϴ� ���� ���� �� �ֵ� ����! (�ִ��� �����ϰ� ��������!!) -> ���ʿ��� ���� ���ٵǸ�.. ������.

//void Test(int);
//void Test2();
//
//
//// �ش� ������ ���߿� ������ �� ���̴ٸ� ǥ�� (extern)
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