from etl.extract import extract
from etl.transform import transform

def main():
    data = extract()
    df = transform(data)
    print(df.head(5))  # Mostra as 5 primeiras linhas do DataFrame

if __name__ == "__main__":
    main()
