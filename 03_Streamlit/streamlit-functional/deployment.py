import joblib
import streamlit as st

# iris = joblib.load("iris.pkl")
# max_val = joblib.load("max.pkl")
# min_val = joblib.load("min.pkl")

# ...to deploy online
# Tenemos que usar la siguiente librería para descargar el contenido "raw" y poder hacer que el kernel lo encuentre.
from urllib.request import urlopen

iris = joblib.load(urlopen("https://github.com/Juan-glitch/SaturdaysAI_vol.3/blob/main/streamlit-functional/iris.pkl?raw=true"))
max_val = joblib.load(urlopen("https://github.com/Juan-glitch/SaturdaysAI_vol.3/blob/main/streamlit-functional/max.pkl?raw=true"))
min_val = joblib.load(urlopen("https://github.com/Juan-glitch/SaturdaysAI_vol.3/blob/main/streamlit-functional/min.pkl?raw=true"))

st.title("Iris Classifier")

left, center, right = st.beta_columns([5,1,5]) 
# En realidad no usaremos center, sólo está para crear un espacio entre las columnas

pred = [

    left.slider("Longitud del sépalo", min_val[0], max_val[0]),
    right.number_input("Anchura del sépalo", min_val[1], max_val[1], step = 0.3),

    left.slider("Longitud del pétalo", min_val[2], max_val[2]),
    right.number_input("Anchura del pétalo", min_val[3], max_val[3], step = 0.3)

]

if st.button("Predecir"):
    val = iris.predict([pred])

    if val == 0:
        name = "Setosa :hibiscus:"
    elif val == 1:
        name = "Versicolor :tulip:"
    else:
        name = "Virginica :blossom:"

    st.markdown("La variedad es "+ name)
