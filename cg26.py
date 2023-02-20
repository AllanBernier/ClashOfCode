k = input()
n = int(input())
T = k.split(",")
t = len(T) / n
for i in range(n):
    R = f"Team {str(i)}: "
    for j in range(i,len(T),3):
        R += f'{T[j]},'
    print(R[-len(R)])
