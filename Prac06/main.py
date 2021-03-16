def solution(board):
    w = len(board[0])
    h = len(board)

    for x in range(1, h):
        for y in range(1, w):
            if board[x][y] == 1:
                board[x][y] = min(board[x - 1][y - 1], min(board[x - 1][y], board[x][y - 1])) + 1
    return max([item for row in board for item in row])**2




if __name__ == '__main__':
    print(solution([[0,1,1,1],
                    [1,1,1,1],
                    [1,1,1,1],
                    [0,0,1,0]]))