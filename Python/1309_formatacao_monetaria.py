while True:
    try:
        valor = input()
        centavos = input()
        centavos = centavos.zfill(2)
        valor_inteiro = valor.split('.')[0] if '.' in valor else valor
        valor_formatado = "{:,}".format(int(valor_inteiro)).replace(".", ",")
        print(f"${valor_formatado}.{centavos}")

    except EOFError:
        break