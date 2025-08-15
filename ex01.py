x = str(input("digite ai meu mano: "))

if x == "A" or x == 'a' : 
    Litros = (int(input("digite ai um numero meu mano: ")))
    V_alcoon = 1.9
    if Litros >=  20 :
        desconto = (Litros * 0.03)  * 100
        V_Total = Litros * V_alcoon
        Result = ((desconto * V_Total) / 100 ) - V_Total 
        Result_P = Result * -1
        print (f"Resutado: {Result_P:.2f}")
    else :
        desconto = (Litros * 0.05)  * 100
        V_Total = Litros * V_alcoon
        Result = ((desconto * V_Total) / 100 ) - V_Total
        Result_P = Result * -1
        print (f"Resutado: {Result_P:.2f}")

elif x == "G" or x == 'g' :
    Litros = (int(input("digite ai um numero meu mano: ")))
    V_Gasolina = 2.5
    if Litros >=  20 :
        desconto = (Litros * 0.04)  * 100
        V_Total = Litros * V_Gasolina
        Result = ((desconto * V_Total) / 100 ) - V_Total 
        Result_P = Result * -1
        print (f"Resutado: {Result_P:.2f}")
    else :
        desconto = (Litros * 0.06)  * 100
        V_Total = Litros * V_Gasolina
        Result = ((desconto * V_Total) / 100 ) - V_Total
        Result_P = Result * -1
        print (f"Resutado: {Result_P:.2f}")