import pandas as pd
import statsmodels.api as sm

# Wczytaj plik
file_path = "przefiltrowane_dane.xlsx"  # Zmień na właściwą ścieżkę do pliku
df = pd.read_excel(file_path)

# Załóżmy, że Y jest w pierwszej kolumnie
y_col = df.columns[0]
X = df.drop(columns=[y_col])  # Zmienna objaśniające
Y = df[y_col]  # Zmienna zależna

# Dodaj stałą do modelu
X = sm.add_constant(X)

# Dopasowanie modelu regresji liniowej
model = sm.OLS(Y, X).fit()

# Pobierz wartości p-value
p_values = model.pvalues

# Wybierz zmienne o istotnym poziomie (np. p < 0.05)
selected_columns = p_values[p_values < 0.05].index

# Filtrowanie DataFrame (zachowujemy tylko istotne zmienne)
filtered_df = df[[y_col] + list(selected_columns[1:])]

# Zapisz wynik do nowego pliku
filtered_df.to_excel("model.xlsx", index=False)

# Wyświetl podsumowanie modelu
print(model.summary())

print("Zapisano plik 'model.xlsx' zawierający tylko istotne zmienne.")
