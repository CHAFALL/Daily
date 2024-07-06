#include "Player.h"
#include "Map.h"
#include "Helper.h"

#pragma region 텍스트 RPG
//bool canMove = true;
//int GPlayerX = 2;
//int GPlayerY = 2;
//
//void MovePlayer(int x, int y)
//{
//    // 범위 체크
//    if (x < 0 || x >= MAP_SIZE)
//        return;
//    if (y < 0 || y >= MAP_SIZE)
//        return;
//    // 벽 체크
//    int index = y * MAP_SIZE + x;
//    if (GMap1D[index] == 1)
//        return;
//    if (GMap2D[y][x] == 1)
//        return;
//
//    // 기존 위치 정리
//    {
//        int index = GPlayerY * MAP_SIZE + GPlayerX;
//        GMap1D[index] = 0;
//
//        GMap2D[GPlayerY][GPlayerX] = 0;
//    }
//
//    // 새 위치 이동
//    // (기존 위치 정리와 매우 유사해 괄호를 통해서 영역을 나눠 재사용!)
//    {
//        GPlayerX = x;
//        GPlayerY = y;
//        int index = GPlayerY * MAP_SIZE + GPlayerX;
//        GMap1D[index] = 2;
//
//        GMap2D[GPlayerY][GPlayerX] = 2;
//    }
//}
//
//
//void HandleMove()
//{
//    // 키보드를 떼고 있으면, 다음 번엔 움직일 수 있다.
//    if (GMoveDir == MD_NONE)
//    {
//        canMove = true;
//        return;
//    }
//
//    // 움직일 수 있는지?
//    if (canMove == false)
//        return;
//
//    canMove = false;
//
//    switch (GMoveDir)
//    {
//    case MD_LEFT:
//        MovePlayer(GPlayerX - 1, GPlayerY);
//        break;
//    case MD_RIGHT:
//        MovePlayer(GPlayerX + 1, GPlayerY);
//        break;
//    case MD_UP:
//        MovePlayer(GPlayerX, GPlayerY - 1);
//        break;
//    case MD_DOWN:
//        MovePlayer(GPlayerX, GPlayerY + 1);
//        break;
//    }
//
//}
#pragma endregion

#pragma region 클래스 분리 연습
//void Player::Attack()
//{
//}
//
//void Player::Die()
//{
//}
//
//void Player::HealMe(int value)
//{
//}

#pragma endregion

