import os
import pandas as pd
from sqlalchemy import create_engine

#Konfiguracja ścieżek i bazy danych - zmieniony driver na pg8000
INPUT_FILE = "data.csv"
DB_URL = "postgresql+pg8000://bi:bi@localhost:5454/ntpd"

#Sprawdzenie czy plik wejściowy istnieje
if not os.path.exists(INPUT_FILE):
    print(f"Błąd: Nie znaleziono pliku '{INPUT_FILE}'.")
    exit()

print(f"Wczytywanie połączonego pliku: {INPUT_FILE}")
df = pd.read_csv(INPUT_FILE)

#Inicjalizacja połączenia z bazą PostgreSQL
print("Nawiązywanie połączenia z bazą danych...")
engine = create_engine(DB_URL)

#Ładowanie danych do tabeli (zgodnie z wytycznymi z laboratorium)
print("Ładowanie danych do tabeli 'transactions'...")
df.to_sql("transactions", engine, if_exists="replace", index=False)

print(f"Sukces! Dane zostały poprawnie załadowane.")
print(f"Nazwa tabeli w bazie: transactions")
print(f"Liczba przesłanych wierszy: {len(df)}")