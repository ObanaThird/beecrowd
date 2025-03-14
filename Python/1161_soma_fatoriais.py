import math

while True:
    try:
        m, n = map(int, input().split())
        r = math.factorial(m) + math.factorial(n)
        print(r)

    except EOFError:
        break