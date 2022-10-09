# Importamos las librerias:

from sklearn import datasets
from sklearn import tree
import joblib
import pandas as pd

# Cargamos los datos, iris contendra data (los parametros) y target (la clase).
iris = datasets.load_iris()

# Comvertimos los parametros en un pandas.DataFrame.
df_x = pd.DataFrame(iris.data, columns=["longitud_sepalo", "anchura_sepalo", "longitud_petalo", "anchura_petalo"])

# Guardamos el máximo y mínimo de cada columna en una lista y está en un archivo independiente.
max_values = []
min_values = []

for i in df_x:
    max_values.append(max(df_x[i]))
    min_values.append(min(df_x[i]))

joblib.dump(max_values,"max.pkl")
joblib.dump(min_values,"min.pkl")

# Aquí preparariamos el modelo, en este ejemplo hemos escogido un dataset sencillo que no necesita preparacion asi que entrenamos el modelo directamente.
tree = tree.DecisionTreeClassifier()

model = tree.fit(iris.data, iris.target)

# Guardamos el modelo entrenado en un archivo independiente.

joblib.dump(model, "iris.pkl")
