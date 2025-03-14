casos = int(input())
r = []

for i in range(casos):
    kgs = float(input())
    while kgs > 1:
        kgs -= kgs/2
        r.append(kgs)
    print(f"{len(r)} dias")
    r = []