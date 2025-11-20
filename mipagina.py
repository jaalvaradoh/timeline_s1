import streamlit as st

st.set_page_config(page_title="Sesion 2 | ISIL", layout="centered")

st.title("Desarrollo de la Inteligencia artificial")

st.write("Interactúa con la barra deslizante para explorar los hitos más importantes en la historia de la IA.")

# -------------------------
# URLs de imágenes en GitHub
# -------------------------
base_url = "https://raw.githubusercontent.com/jaalvaradoh/timeline_s1/main/timeline_images/"

imagenes = {
    1: base_url + "timeline1.png",
    2: base_url + "timeline2.png",
    3: base_url + "timeline3.png",
    4: base_url + "timeline4.png",
    5: base_url + "timeline5.png"
}

# -------------------------
# Slider
# -------------------------

opcion = st.slider(
    "Selecciona un punto del timeline",
    min_value=1,
    max_value=5,
    value=1,
    step=1
)

# Mostrar imagen según slider
st.image(imagenes[opcion], use_container_width=True) # width=600)

st.write(f"Imagen mostrada: timeline{opcion}.png")

if opcion == 1:
  st.info("📘 **1950 – Test de Turing** | Alan Turing propone un criterio para evaluar la inteligencia de una máquina.")
if opcion == 2:
  st.info("🏛️**1956 – Nace el campo de la IA en Dartmouth** | John McCarthy acuña el término *Inteligencia Artificial*.")

