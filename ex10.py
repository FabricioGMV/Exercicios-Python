import requests
cep = input("Digite o CEP do destino (Sem traços): ")
url = f"https://viacep.com.br/ws/{cep}/json/"
result = requests.get(url)

dados = result.json()

if dados['localidade'] != "São Paulo":
    print("A viagem não é em São Paulo")

else:
    print(f"O bairro da viagem é para: {dados['bairro']}, em {dados['localidade']}")

    area = cep[:5]
    if area < "1600":
        print("Região: Zona Sul")
    elif area < "3000":
        print("Região: Zona Norte")
    elif area < "6000":
        print("Região: Zona Leste")
    elif area < "8000":
        print("Região: Zona Oeste")