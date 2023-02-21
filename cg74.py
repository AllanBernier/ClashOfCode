hp1, d1 = [int(i) for i in input().split()]
hp2, d2 = [int(i) for i in input().split()]

turn = 0
while True:
    turn += 1
    hp1 -= d2
    hp2 -= d1

    if hp1 <= 0:
        print(f'2 {turn}')
        exit()
    if hp2 <= 0:
        print(f'1 {turn}')
        exit()