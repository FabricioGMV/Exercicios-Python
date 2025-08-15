import requests

def buscar_pais(nome_pais):
    url = f"https://restcountries.com/v3.1/name/{nome_pais}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # erro caso status != 200
        dados = response.json()[0]   # pega o primeiro país retornado

        # Nome do país
        nome = dados["name"]["common"]

        # Linguagens (transforma em lista de strings)
        linguas = list(dados["languages"].values())

        # Região e Sub-região
        regiao = dados["region"]
        subregiao = dados["subregion"]

        # Capital
        capital = ", ".join(dados["capital"]) if "capital" in dados else "N/A"

        # Moeda
        moeda_info = list(dados["currencies"].values())[0]
        sigla_moeda = list(dados["currencies"].keys())[0]
        nome_moeda = moeda_info["name"]
        simbolo_moeda = moeda_info["symbol"]

        # Fronteiras
        fronteiras = dados.get("borders", [])

        print(f"🌍 País: {nome}")
        print(f"🗣️ Linguagem(ns): {', '.join(linguas)}")
        print(f"📍 Região: {regiao}")
        print(f"📍 Sub-região: {subregiao}")
        print(f"🏙️ Capital: {capital}")
        print(f"💰 Moeda: {sigla_moeda} - {nome_moeda} ({simbolo_moeda})")
        print(f"🌐 Fronteiras: {', '.join(fronteiras) if fronteiras else 'Nenhuma'}")

    except requests.exceptions.RequestException as e:
        print("Erro ao acessar a API:", e)
    except (KeyError, IndexError):
        print("Não foi possível encontrar informações para esse país.")


# Programa principal
if __name__ == "__main__":
    pais = input("Digite o nome do país em inglês (ex: brazil, japan, germany): ")
    buscar_pais(pais)