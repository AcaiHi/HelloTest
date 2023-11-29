n = int(input())

for i in range(n):
    c = input()
    a = int(input())
    b = int(input())

    if c == '-':
        print(a - b)
    elif c == '+':
        print(a + b)
    else:
        print("Unsupported operation")
