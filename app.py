import streamlit as st

st.set_page_config(page_title="Timeline de la Inteligencia Artificial", layout="centered")

st.title("🧠 Timeline del Desarrollo de la Inteligencia Artificial")
st.write("Interactúa con la barra deslizante para explorar los hitos más importantes en la historia de la IA.")

# --- Datos del timeline ---
eventos = {
    1950: {
        "texto": "📘 **1950 – Test de Turing** | Alan Turing propone un criterio para evaluar la inteligencia de una máquina.",
        "imagen": "print(f"{timeline_images/timeline1}.png")
    },
    1956: {
        "texto": "🏛️ **1956 – Nace el campo de la IA en Dartmouth** | John McCarthy acuña el término *Inteligencia Artificial*.",
        "imagen": print(f"{timeline_images/timeline2}.png")
    },
    1997: {
        "texto": "♟️ **1997 – Deep Blue vence a Garry Kasparov** | Primer triunfo de una máquina sobre un campeón mundial de ajedrez.",
        "imagen": "timeline_images/timeline3.png"
    },
    2012: {
        "texto": "📈 **2012 – Revolución del Deep Learning (AlexNet)** | Una red neuronal profunda supera ampliamente otros métodos en reconocimiento de imágenes.",
        "imagen": "timeline_images/timeline4.png"
    },
    2022: {
        "texto": "🤖 **2022 – Avances en modelos generativos** | Llegan modelos como GPT, DALL·E y sistemas multimodales.",
        "imagen": "timeline_images/timeline5.png"  # si solo tienes 4 imágenes, usa timeline4.png nuevamente
    }
}

# --- URL base de GitHub (raw) ---
BASE_URL = "https://raw.githubusercontent.com/TU_USUARIO/TU_REPO/main/timeline_s1/"

# --- Barra deslizante ---
anio = st.slider(
    "Selecciona un año para ver el hito correspondiente:",
    min_value=min(eventos.keys()),
    max_value=max(eventos.keys()),
    step=1
)

# --- Mostrar evento más cercano ---
anios_ordenados = sorted(eventos.keys())
anio_mostrado = min(anios_ordenados, key=lambda x: abs(x - anio))

evento = eventos[anio_mostrado]

st.subheader(f"📅 Evento alrededor de {anio}:")
st.markdown(evento["texto"])

# Mostrar imagen asociada
st.image(BASE_URL + evento["imagen"], use_column_width=True)

# --- Timeline completo ---
st.write("---")
st.header("📜 Timeline completo")

for a in anios_ordenados:
    st.markdown(f"### {a}")
    st.markdown(eventos[a]["texto"])
    st.image(BASE_URL + eventos[a]["imagen"], use_column_width=True)
    st.write("---")
