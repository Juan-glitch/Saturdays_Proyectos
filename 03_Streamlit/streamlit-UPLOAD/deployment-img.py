import streamlit as st
from PIL import Image
from skimage import filters

# Permitimos al usuario subir un archivo JPG o NPG.
pic = st.file_uploader("Introduce tu imagen", ["JPG", "PNG"])

# Si lo hace:
if pic:
    
    # Cambiamos su formato a un formato de imagen más convencional, lo que no es necesario para trabajar con Streamlit pero sí con otras librerías.
    pic = Image.open(pic)

    # Tratamos la imagen.
    pic = filters.sobel(pic)

    # Y se la mostramos al usuario con el tamaño que el escoja.
    size = st.slider("Tamaño de la imagen", min_value = 100, max_value = 300, step = 10)

    st.image(pic, width = size)
