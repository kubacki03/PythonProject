import pandas as pd
import openpyxl
# Wczytaj plik
file_path = "scieki.xlsx"  # Zmień na właściwą ścieżkę do pliku
df = pd.read_excel(file_path)

# Załóżmy, że Y jest w pierwszej kolumnie
y_col = df.columns[0]

# Oblicz korelację
correlations = df.corr()[y_col]

# Wybierz zmienne, które mają wartość bezwzględną korelacji >= 0.3
selected_columns = correlations[abs(correlations) >= 0.3].index

# Filtrowanie DataFrame
filtered_df = df[selected_columns]

# Zapisz wynik do nowego pliku
filtered_df.to_excel("clean_data.xlsx", index=False)

print("Zapisano plik 'przefiltrowane_dane.xlsx' zawierający tylko istotne zmienne.")
