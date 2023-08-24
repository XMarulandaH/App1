import streamlit as st
from PIL import Image 

st.title('La aplicación de Xiomarita') 

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend")
image = Image.open('gato.png')

st.image(image, caption= 'Interfaces multimodales')
