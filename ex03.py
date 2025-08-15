N1 = float(input("Digite a primeira nota: "))
N2 = float(input("Digite a segunda nota: "))

media = (N1 + N2) / 2

if media >= 9 and media <= 10:
    conceito = "A"
    status = "APROVADO"
    print("Sua Nota1 foi:", N1)
    print("Sua Nota2 foi:", N2)
    print(f"Sua média foi: {media:.2f}")
    print("você está: ", status)
    print("Seu conceito foi: ", conceito)

elif media >= 7.5 and media <= 9:
    conceito1 = "B"
    status = "APROVADO"
    print("Sua Nota1 foi:", N1)
    print("Sua Nota2 foi:", N2)
    print(f"Sua média foi: {media:.2f}")
    print("você está: ", status)
    print("Seu conceito foi: ", conceito1)
    
elif media >= 6 and media <= 7.5:
    conceito2 = "C"
    status = "APROVADO"
    print("Sua Nota1 foi:", N1)
    print("Sua Nota2 foi:", N2)
    print(f"Sua média foi: {media:.2f}")
    print("você está: ",status)
    print("Seu conceito foi: ",conceito2)

elif media >= 4 and media <= 6:
    conceito3 = "D"
    status = "REPROVADO"
    print("Sua Nota1 foi:", N1)
    print("Sua Nota2 foi:", N2)
    print(f"Sua média foi: {media:.2f}")
    print("você está: ",status)
    print("Seu conceito foi: ",conceito3)

else:
    conceito4 = "E"
    status = "REPROVADO"
    print("Sua Nota1 foi:", N1)
    print("Sua Nota2 foi:", N2)
    print(f"Sua média foi: {media:.2f}")
    print("você está: ",status)
    print("Seu conceito foi: ",conceito4)
