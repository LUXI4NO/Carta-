import streamlit as st
import os

# --- Configuración inicial ---
st.set_page_config(page_title="Nuestro Aniversario ❤️ - Un año juntos", layout="centered")

# --- Encabezado ---
st.markdown("<h1 style='text-align: center;'>Nuestro primer año juntos</h1>", unsafe_allow_html=True)
st.markdown("""
<h6 style='text-align: center;'>
Escribo cada una de estas líneas pensando en la persona que llegó a mi mundo y lo convirtió en uno mejor.
Vos, la mujer que amo, te convertiste en un pilar fundamental para mí.
Por eso, quiero decirte gracias por elegirme y dedicarte estas letras.
</h6>
""", unsafe_allow_html=True)
st.markdown("---")

# --- Datos de cada mes ---
momentos = [
    ("Nuestro Primer mes Juntos", "Imagenes/Foto1.jpeg", """Nuestro amor ya venía creciendo, pero el 16 de agosto decidimos darle una fecha especial...
"""),
    ("Nuestro Segundo mes Juntos", "Imagenes/Foto2.jpeg", """Gracias a esta relación, cada día es una oportunidad para que seamos felices...
"""),
    ("Nuestro Tercer mes Juntos", "Imagenes/Foto3.jpeg", """Juntos, seguimos construyendo un amor que se siente más sólido y hermoso...
"""),
    ("Nuestro Cuarto mes Juntos", "Imagenes/Foto4.jpeg", """Valoro cada vez más lo que compartimos, esos momentos de dos gordos hermosos...
"""),
    ("Nuestro Quinto mes Juntos", "Imagenes/Foto5.jpeg", """Apostamos por el otro, por un amor verdadero y duradero...
"""),
    ("Nuestro Sexto mes Juntos", "Imagenes/Foto6.jpeg", """Juntos, seguimos aprendiendo a amarnos de formas nuevas...
"""),
    ("Nuestro Séptimo mes Juntos", "Imagenes/Foto7.jpeg", """Aprendimos a amarnos, a soportarnos y a tratarnos...
"""),
    ("Nuestro Octavo mes Juntos", "Imagenes/Foto8.jpeg", """Amo hacer planes con vos, pero mi verdadera felicidad es simplemente...
"""),
    ("Nuestro Noveno mes Juntos", "Imagenes/Foto9.jpeg", """Todo el tiempo que estuvimos juntos me hizo ver que no hay amor más grande...
"""),
    ("Nuestro Décimo mes Juntos", "Imagenes/Foto10.jpeg", """Todo el tiempo que pasamos juntos me hizo ver que no hay amor más grande...
"""),
    ("Nuestro Undécimo mes Juntos", "Imagenes/Foto11.jpeg", """Con vos comprendí que cada día es una aventura distinta...
"""),
    ("Nuestro Primer año Juntos", "Imagenes/Foto12.jpeg", """Juntos, construimos una vida llena de risas, apoyo incondicional...
"""),
]

# --- Mostrar cada mes ---
for titulo, imagen, texto in momentos:
    st.markdown(f"<h2 style='text-align: center;'>{titulo}</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(imagen, use_container_width=True)
    with col2:
        st.markdown(f"<div style='text-align: center; margin-top: 50px;'><p>{texto}</p></div>", unsafe_allow_html=True)
    st.markdown("---")
