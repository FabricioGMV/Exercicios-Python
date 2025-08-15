def CalcularNotas(valor):
    nota = []
    total = 0
    i = 0
    while i == 0:
        while total < valor:
            cem = 100
            cinquenta = 50
            dez = 10
            cinco = 5
            um = 1

            if total + cem <= valor:

                total += cem
                nota.append(cem)

            elif total + cem > valor:
                if total + cinquenta <= valor:
                    total += cinquenta
                    nota.append(cinquenta)
                
                elif total + cinquenta > valor:
                    if total + dez <= valor:
                        total += dez
                        nota.append(dez)
                    
                    elif total + dez > valor:
                        if total + cinco <= valor:
                            total += cinco
                            nota.append(cinco)

                        elif total + cinco > valor:
                            if total + um <= valor:
                                total += um
                                nota.append(um)

        i = -1
    print("Notas entregues:", nota)


valorDoSaque = int(input("Digite ai quanto vai sacar meu mano: "))

if 10 <= valorDoSaque <= 600:
    CalcularNotas(valorDoSaque)
else:
    print("Valor inválido! Digite entre 10 e 600.")
