# src/etl/extract.py
import requests
import pandas as pd

# Configurações do time e temporada
TEAM_ID = 2790      # Fluminense
SEASON = 2023       # Temporada desejada

# Token da sua conta gratuita
API_TOKEN = "5691c9bb5e104aec987ce55794daed62"

HEADERS = {
    "X-Auth-Token": API_TOKEN
}

BASE_URL = "https://api.football-data.org/v4"

def extract():
    """
    Extrai partidas de um time específico usando a API Football-Data.org.
    Retorna uma lista de partidas (raw data) para transformação posterior.
    """
    url = f"{BASE_URL}/teams/{TEAM_ID}/matches?season={SEASON}"

    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()

        matches = data.get("matches", [])
        print(f"Extração realizada com sucesso! Total de partidas: {len(matches)}")
        return matches

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Erro ao conectar com a API: {err}")
    except KeyError:
        print("Erro ao processar os dados retornados da API.")

    return []
