import requests
import os

# Repositório e caminho
owner = "digitalinnovationone"
repo = "trilha-python-dio"
branch = "01_estrutura_de_dados"
path = "01 - Estrutura de dados/05 - Funções"

# Monta a URL da API do GitHub para a pasta
api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}?ref={branch}"

# Cabeçalho opcional para evitar rate limit (coloque seu token se quiser)
headers = {"Accept": "application/vnd.github.v3+json"}

# Requisição para a API
response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    files = response.json()
    for file in files:
        if file["name"].endswith(".py"):
            download_url = file["download_url"]
            file_name = file["name"]

            content = requests.get(download_url).text
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✅ Baixado: {file_name}")
else:
    print(f"❌ Erro ao acessar API do GitHub: {response.status_code}")
