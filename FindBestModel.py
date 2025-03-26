import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score


models = {
        'Linear Regression': LinearRegression(),
        'Ridge Regression': Ridge(),
        'Lasso Regression': Lasso(),
        'Random Forest': RandomForestRegressor(),
        'Gradient Boosting': GradientBoostingRegressor(),
        'Support Vector Regressor': SVR()
    }

file_path = "data/clean_data.xlsx"
df = pd.read_excel(file_path)



y_col = df.columns[0]
X = df.drop(columns=[y_col])
y = df[y_col]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

best_model = None
best_score = float('-inf')
results = []

for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        results.append((name, r2, rmse))

        if r2 > best_score:
            best_score = r2
            best_model = model

results_df = pd.DataFrame(results, columns=['Model', 'R2 Score', 'RMSE'])
results_df = results_df.sort_values(by='R2 Score', ascending=False)
print(best_model)
print(results_df)




