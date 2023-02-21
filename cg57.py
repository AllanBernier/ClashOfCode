text_input = input().split(" ")
r = float(text_input[0] )
a = ['hundred','thousand','million']
b = [100,1000,1000000]
for i in range(len(a)):
    if text_input[1] == a[i]:
        r *= b[i]
print(int(r))