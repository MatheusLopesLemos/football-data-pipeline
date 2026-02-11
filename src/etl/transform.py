import pandas as pd

def transform(data):
    """
    Recebe a lista de partidas (data) extraída da API
    e retorna um DataFrame limpo e organizado.
    """
    if not data:
        return pd.DataFrame()  # Retorna DataFrame vazio se não houver dados

    rows = []
    for match in data:
        rows.append({
            "match_id": match["id"],
            "date": match["utcDate"],
            "competition": match["competition"]["name"],
            "home_team": match["homeTeam"]["name"],
            "away_team": match["awayTeam"]["name"],
            "home_score": match["score"]["fullTime"]["home"],
            "away_score": match["score"]["fullTime"]["away"],
            "status": match["status"]
        })

    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date").reset_index(drop=True)

    print(f"Transformação concluída. Total de partidas: {len(df)}")
    return df
