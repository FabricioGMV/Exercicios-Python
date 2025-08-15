salario = float(input("Digite o salário inicial: R$ "))
ano = 1995
percentual = 1.5

while ano < 2025:
    if ano >= 1996:
        aumento = salario * (percentual / 100)
        salario += aumento
        percentual *= 2
    ano += 1

print(f"Salário atual em 2025: R$ {salario:.2f}")