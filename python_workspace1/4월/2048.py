import random
import os
import sys
import time

# 게임 보드 초기화
def init_board():
    board = [[0] * 4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

# 새로운 타일 추가
def add_new_tile(board):
    empty_cells = [(r, c) for r in range(4) for c in range(4) if board[r][c] == 0]
    if empty_cells:
        r, c = random.choice(empty_cells)
        board[r][c] = random.choice([2, 4])

# 보드 출력
def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')  # 화면 클리어
    for row in board:
        print("\t".join([str(cell) if cell != 0 else '.' for cell in row]))
        print()

# 보드 왼쪽으로 이동
def slide_left(board):
    new_board = []
    for row in board:
        new_row = [x for x in row if x != 0]  # 0을 제외한 모든 값 모음
        for i in range(len(new_row) - 1):
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                new_row[i + 1] = 0
        new_row = [x for x in new_row if x != 0]  # 0이 아닌 값들만 다시 모음
        new_row.extend([0] * (4 - len(new_row)))  # 남은 공간에 0 추가
        new_board.append(new_row)
    return new_board

# 게임 보드 오른쪽으로 이동
def slide_right(board):
    return [row[::-1] for row in slide_left([row[::-1] for row in board])]

# 게임 보드 위로 이동
def slide_up(board):
    return list(map(list, zip(*slide_left(list(map(list, zip(*board)))))))

# 게임 보드 아래로 이동
def slide_down(board):
    return list(map(list, zip(*slide_right(list(map(list, zip(*board)))))))

# 키 입력 처리
def get_move():
    move = input("Enter move (W/A/S/D): ").lower()
    while move not in ['w', 'a', 's', 'd']:
        print("Invalid move! Please enter W, A, S, or D.")
        move = input("Enter move (W/A/S/D): ").lower()
    return move

# 게임 실행
def main():
    board = init_board()
    print_board(board)
    
    while True:
        move = get_move()
        if move == 'w':
            new_board = slide_up(board)
        elif move == 's':
            new_board = slide_down(board)
        elif move == 'a':
            new_board = slide_left(board)
        elif move == 'd':
            new_board = slide_right(board)
        
        if new_board != board:
            board[:] = new_board
            add_new_tile(board)
            print_board(board)

        if is_game_over(board):
            print("Game Over!")
            break

# 게임 오버 체크
def is_game_over(board):
    for r in range(4):
        for c in range(4):
            if board[r][c] == 0:
                return False
            if r < 3 and board[r][c] == board[r + 1][c]:
                return False
            if c < 3 and board[r][c] == board[r][c + 1]:
                return False
    return True

if __name__ == '__main__':
    main()
