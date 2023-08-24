import streamlit as st
from PIL import Image 

st.title('La aplicación de Xiomarita') 

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend")
image = Image.open('dedito.jpg')

st.image(image, caption= 'Aqui va un dedito arriba')

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto) 

st.subheader("Ahora usemos 2 columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('¡Correcto!')

with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("Qué modalidad es la principal en tu interfaz", ('visual', 'auditiva', 'tactil'))
  if modo == 'visual':
    st.write('La vista es fundamental para tu interfaz')
  if modo == 'auditiva':
    st.write('La audición es fundamental para tu interfaz')
  if modo == 'tactil':
    st.write('El tacto es fundamental para tu interfaz')

st.subheader("Uso de botones")
if st.button('Presiona el botón'):
  st.write('Gracias por presionar')
else:
  st.write('No has presionado aún')

st.subheader("Selectbox") #despliega un listado 
in_mod = st.selectbox(
  "Selecciona la modalidad",
  ("Audio", "Visual", "Háptico"),
)
if in_mod == "Audio"
  set_mod = "Reproducir audio"
elif in_mod == "Visual":
  set_mod = "Reproducir video"
elif in_mod == "Háptico":
  set_mod = "Activar vibración"
st.write(" La acción es:", set_mod)
