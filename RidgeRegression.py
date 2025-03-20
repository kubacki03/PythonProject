import pandas as pd
from sklearn.linear_model import Ridge
import numpy as np

# Przykładowe dane (możesz użyć własnych)
file_path = "clean_data.xlsx"  # Zmień na właściwą ścieżkę do pliku
df = pd.read_excel(file_path)

# Załóżmy, że Y jest w pierwszej kolumnie
y_col = df.columns[0]
X = df.drop(columns=[y_col])  # Zmienna objaśniające
y = df[y_col]  # Zmienna zależna
# Tworzymy i trenujemy model Ridge Regression
ridge = Ridge(alpha=1.0)
ridge.fit(X, y)

# Pobieramy współczynniki i wyraz wolny
coef = ridge.coef_
intercept = ridge.intercept_

# Tworzymy wzór modelu
equation = "y = " + " + ".join([f"{coef[i]:.4f} * X{i}" for i in range(len(coef))]) + f" + {intercept:.4f}"

# Wyświetlamy wynik
print("Wzór modelu Ridge Regression:")
print(equation)
import statsmodels.api as sm

# Dodajemy kolumnę jedynkową dla wyrazu wolnego
X_with_intercept = sm.add_constant(X)

# Tworzymy i trenujemy model regresji liniowej (zamiast Ridge)
model = sm.OLS(y, X_with_intercept)

# Dopasowujemy model
results = model.fit()

# Wyświetlamy podsumowanie wyników, w tym p-value
print(results.summary())
