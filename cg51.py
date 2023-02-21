otter = int(input())
years = int(input())

for _ in range(years):
    otter = otter * 1.2
print(int(otter *4) if otter//1 == otter/1 else int(otter *4) +1)
