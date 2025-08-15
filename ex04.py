gabarito = ['A', 'C', 'B', 'D', 'A', 'B', 'C', 'D', 'A', 'B']
notas = []
alunos = 0

def atv():
    nota = 0

    for i in range(10):
        result = input(f"Questão {i+1}: ").upper()
        if result == gabarito[i]:
            nota += 1

    notas.append(nota)

while True:
    duvida = input("Restam alunos? s/n: ").lower()

    if duvida == 's':
        alunos += 1
        atv()
    elif duvida == 'n':
        break
    else:
        print("Resposta inválida. Digite 's' ou 'n'.")

maior = max(notas) if notas else 0
menor = min(notas) if notas else 0

print(f'As notas são: ', ', '.join(str(v) for v in notas))
print(f'Maior nota: {maior}')
print(f'Menor nota: {menor}')
print(f'Quantidade de alunos: {alunos}')