n, m = [int(i) for i in input().split()]
s = int(input())
r = sum(input().count('o') for _ in range(n))
print(r*s)