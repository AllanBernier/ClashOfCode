sequence = input().split()

if (sequence[len(sequence)-1] == "?"):
    print(int(sequence[len(sequence)-3]) + int(sequence[len(sequence)-2]))
elif( sequence[0] == "?"):
    print(int(sequence[2]) - int(sequence[1]))
elif ( sequence[1] == "?"):
    print(int(sequence[2]) - int(sequence[0]))
