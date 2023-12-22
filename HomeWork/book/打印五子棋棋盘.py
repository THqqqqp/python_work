"""
    2023028107 李明睿
    打印五子棋棋盘
"""


def print_board(board):
    # print(board)
    print("  ", end="")
    for i in range(1, 10):
        print(i, end=" ")
    print()
    for i in range(1, 10):
        print(i, end=" ")
        for j in range(1, 10):
            print(board[i][j], end=" ")
        print()


if __name__ == "__main__":
    board = [[0 for i in range(10)] for j in range(10)]
    print_board(board)