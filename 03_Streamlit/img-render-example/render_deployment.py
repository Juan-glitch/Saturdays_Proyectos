import streamlit as st
import pandas as pd

show = st.beta_container()

with st.sidebar:
    opt = st.radio("Opción", ["Gráfico", "Mapa"])

    if opt == "Gráfico":
        width = st.slider("Ancho", min_value = 300, max_value = 900, step = 10, value = 600)
        height = st.slider("Alto", min_value = 100, max_value = 300, step = 10, value = 200)
        gtype = st.selectbox("Tipo de grafico",
            ("area_chart", "bar_chart", "line_chart"),
            # Recuerda, el parámetro format_func sirve para diferenciar lo que queremos recibir 
            # (area_char, bar_chart...) de lo que queremos mostrarle al usuario (Gráfico de barras...).
            format_func = lambda t : "Area" if t == "area_chart" else "Barras" if t == "bar_chart" else "Lineas"
            )

        show.title("Gráficos simples")

        show.write("Como ves no es difícil preparar un entorno con gráficos generados dinámicamente a través de streamlit:")

        # Datos aleatorios.
        data = pd.DataFrame([[1,3,2],[3,2,2],[4,5,2]], columns = ["C1","C2","C3"])
        # La función getattr permite llamar a una función a través de su librería y su nombre en forma de string.
        getattr(show, gtype) (data, width = width, height = height, use_container_width = False)

        # Recuerda que los contenedores en streamlit se usan como llamadas a la propia librería, así que en la función
        # anterior show es equivalente a st salvo por la ubicación en la que aparecen los resultados.

    else:
        show.title("Donde estamos")
        show.write("Tampoco es difícil generar un mapa, aquí puedes ver la mayoría de las ciudades en las puedes encontrar una comunidad Saturdays:")
        # Estas son las coordenadas de las ciudades.
        locations = pd.DataFrame([
            [41.3879, 2.16992],
            [20.6736, -103.344],
            [40.4167, -3.70325],
            [-2.19616, -79.88621],
            [37.38283, -5.97317],
            [39.46975, -0.37739],
            [-0.225219, -78.5248],
            [25.6714, -100.309],
            [25.2646, 55.3077],
            [9.748917, -83.753428],
            [38.3452, -0.481006],
            [36.83814, -2.45974],
            [43.36029, -5.84476],
            [43.26271, -2.92528],
            [37.89155, -4.77275],
            [51.5072, -0.1275],
            [37.98704, -1.13004],
            [39.5695100, 2.6474500],
            [41.119, 1.24546],
            [39.46975, -0.37739],
            [19.4194, -99.1455],
            [-17.414, -66.1653],
            [-27.33056, -55.86667],
            [29.0892, -110.961],
            [-16.4897, -68.1193],
            [-12.0453, -77.0311],
            [-0.225219, -78.5248],
            [32.22174, -110.92648],
            [-20.348404, 57.552152]
            ],
            columns = ["lat", "lon"]) 

        # Mostrar coordenadas en el mapa.
        show.map(locations)
