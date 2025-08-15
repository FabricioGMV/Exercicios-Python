cardapio = {
    100: ("cachorro quente", 1.20),
    101: ("bauru simples", 1.30),
    102: ("bauru com ovo", 1.50),
    103: ("hamburger", 1.20),
    104: ("cheeseburguer", 1.30),
    105: ("refrigerante", 1.00)
}

total = 0 

while True: 
    codigo = int(input("código do item (encerra): "))
    if codigo == 0: 
     break 
    if codigo in cardapio:
       nome, preco = cardapio[codigo]
       quantidade = int(input(f'quantidade de {nome}:'))
       valor = preco * quantidade 
       print(f'{nome}: R$ {valor:.2f}')
       total += valor 
    else:
       print("Inválido.")

       print(f'Total do pedido: R$ {total:.2f}')
