import streamlit as st

st.set_page_config(page_title="Timeline de la Inteligencia Artificial", layout="centered")

st.title("🧠 Timeline del Desarrollo de la Inteligencia Artificial")
st.write("Interactúa con la barra deslizante para explorar los hitos más importantes en la historia de la IA.")

# Datos del timeline
eventos = {
    1950: "📘 **1950 – Test de Turing** | Alan Turing propone un criterio para evaluar la inteligencia de una máquina.",
    
    1956: "🏛️ **1956 – Nace el campo de la IA en Dartmouth** | John McCarthy acuña el término *Inteligencia Artificial*.",
    
    1997: "♟️ **1997 – Deep Blue vence a Garry Kasparov**| Primer triunfo de una máquina sobre un campeón mundial de ajedrez.",
    
    2012: "📈 **2012 – Revolución del Deep Learning (AlexNet)** | Una red neuronal profunda supera ampliamente otros métodos en reconocimiento de imágenes.",
    
    2022: "🤖 **2022 – Avances en modelos generativos** | El mundo presencia la llegada masiva de modelos como GPT, DALL·E y sistemas multimodales."
}

# Barra deslizante
anio = st.slider("Selecciona un año para ver el hito correspondiente:",
                 min_value=min(eventos.keys()),
                 max_value=max(eventos.keys()),
                 step=1)

# Mostrar evento más cercano al año elegido
anios_ordenados = sorted(eventos.keys())
anio_mostrado = min(anios_ordenados, key=lambda x: abs(x - anio))

st.subheader(f"📅 Evento alrededor de {anio}:")
st.markdown(eventos[anio_mostrado])

# Mostrar todo el timeline
st.write("---")
st.header("📜 Timeline completo")
for a in anios_ordenados:
    st.markdown(f"### {a}")
    st.markdown(eventos[a])
    st.write("---")
