import random

nums  = list(range(9))
random.shuffle(nums)
mt = [nums[0:3], nums[3:6], nums[6:9]]
print(mt)
print()

def check_null(mt):
    for i in range(3):
        for j in range(3):
            if mt[i][j] == 0:
                return i, j
    return None


def P_moves(x,y):
    moves = []
    if x < 2:
        moves.append('D')
    if x > 0:
        moves.append('U')
    if y < 2:
        moves.append('R')
    if y > 0:
        moves.append('L')
    return moves

def P_action(x, y, action):
    if action == 'U':
        x -= 1
    elif action == 'D':
        x += 1
    elif action == 'L':
        y -= 1
    else:
        y += 1
    return x, y

nx, ny = check_null(mt)
while mt != [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
    moves = P_moves(nx, ny)
    action = random.choice(moves)
    x, y = P_action(nx, ny, action)
    mt[nx][ny], mt[x][y] = mt[x][y], mt[nx][ny]
    nx, ny = x, y
    print(mt)
    print()

