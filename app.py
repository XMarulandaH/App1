import streamlit as st
from PIL import Image 

st.title('La aplicación de Xiomarita') 

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend")
image = Image.open('dedito.jpg')

st.image(image, caption= 'Aqui va un dedito arriba')

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto) 
