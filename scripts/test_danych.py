import pandas as pd

# Ładujemy plik z danymi o szczepieniach
try:
    df = pd.read_csv('data/cdc_vaccines_usa.csv')
    print("PLIK ZAŁADOWANY!")
    print("Oto nazwy kolumn, które widzi program:")
    print(df.columns.tolist())
except Exception as e:
    print("BŁĄD:", e)