valores = []

while True:
    numero = int(input("Digite um número (digite -1 para encerrar): "))
    if numero == -1:
        break
    valores.append(numero)

print(f'Valores lidos: {len(valores)}')
print(f'Ordem original:', ', '.join(str(v) for v in valores))
print(f'Ordem inversa:', ', '.join(str(v) for v in reversed(valores)))

soma = sum(valores)
media = soma / len(valores) if valores else 0 
acima_da_media = sum(1 for v in valores if v > media)

print(f'Soma dos valores: {soma}')
print(f'Média dos valores: {media:.2f}')
print(f'Valores acima da média: {acima_da_media}')