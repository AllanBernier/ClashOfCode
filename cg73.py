s = input().upper()
print(''.join(str(s[:i+1].count(s[i])) for i in range(len(s)-1,-1,-1)[::-1]))

## Attention 80%
