import streamlit as st

st.set_page_config(page_title="Timeline con Imágenes", layout="centered")

st.title("📌 Timeline con Slider e Imágenes desde GitHub")

st.write("Usa el slider para navegar entre las imágenes del timeline.")

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
st.image(imagenes[opcion], use_container_width=True)

st.write(f"Imagen mostrada: timeline{opcion}.png")
