x, y = input().split()
if x == y:
    print('DRAW')
elif x == 'ROCK':
    if y == 'SCISSORS':
        print('PLAYER1')
    else:
        print('PLAYER2')
elif x == 'SCISSORS':
    if y == 'PAPER':
        print('PLAYER1')
    else:
        print('PLAYER2')
elif x == 'PAPER':
    if y == 'ROCK':
        print('PLAYER1')
    else:
        print('PLAYER2')

# SORRY I KNOW MODULO TO SOLVE THIS 