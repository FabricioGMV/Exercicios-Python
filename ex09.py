import requests

moeda = input("Digite a sigla da moeda (ex: USD, EUR, GBP): ").upper()

url = "https://api.exchangerate-api.com/v4/latest/BRL"
resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    cotacao = dados["rates"].get(moeda)

    if cotacao:
        if moeda == "USD":
            nome = "dólares americanos"
        elif moeda == "EUR":
            nome = "euros"
        elif moeda == "GBP":
            nome = "libras esterlinas"
        else:
            nome = moeda

        print(f"O Real vale {cotacao:.2f} {nome}.")
    else:
        print("Moeda não encontrada.")
else:
    print("Erro ao acessar a API.")
