import numpy as np
import random

mt = np.random.randint(0, 2, size=(4, 4))
print(mt)
print()
x, y = 0, 0 # vi trí máy hút bụi
def P_moves(x,y):
    moves = []
    if x < 3:
        moves.append('D')
    if x > 0:
        moves.append('U')
    if y < 3:
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


while np.any(mt):
    state = mt[x][y]
    if state == 1:
        mt[x][y] = 0

    moves = P_moves(x, y)
    action = random.choice(moves)
    x,y = P_action(x, y, action)
    print(mt)
    print()

