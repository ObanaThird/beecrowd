import math

n_casos = int(input())

for i in range(n_casos):
    casos = list(map(int, input().split()))
    r = math.gcd(casos[0], casos[1])
    print(r)
    i += 1