def rafael(x, y):
    return (((3*x)**2)+y**2)

def beto(x, y):
    return ((2*(x**2))+((5*y)**2))

def carlos(x, y):
    return (((-100)*x)+y**3)

testes = int(input())

for i in range(testes):
    x, y = map(int, input().split())
    res_rafa = rafael(x, y)
    res_beto = beto(x, y)
    res_carlos = carlos(x, y)
    res_list = [[res_rafa, "Rafael ganhou"],[res_beto, "Beto ganhou"], [res_carlos, "Carlos ganhou"]]
    res = max(res_list)
    print(res[1])