import streamlit as st
import os

# --- Configuración inicial ---
st.set_page_config(page_title="Nuestro Aniversario ❤️ - Un año juntos", layout="centered")

# --- Función para cargar imágenes desde la carpeta ---
def get_image_path(nombre_archivo):
    return os.path.join(os.path.dirname(__file__), "Imagenes", nombre_archivo)

# --- Encabezado ---
st.markdown("<h1 style='text-align: center;'>Nuestro primer año juntos</h1>", unsafe_allow_html=True)
st.markdown("""
<h6 style='text-align: center;'>
Escribo cada una de estas líneas pensando en la persona que llegó a mi mundo y lo convirtió en uno mejor. Vos, la mujer que amo, te convertiste en un pilar fundamental para mí. Por eso, quiero decirte gracias por elegirme y dedicarte estas letras.
</h6>
""", unsafe_allow_html=True)
st.markdown("---")

# --- Datos de cada mes ---
momentos = [
    ("Nuestro Primer mes Juntos", "Foto1.jpeg", """Nuestro amor ya venía creciendo, pero el 16 de agosto decidimos darle una fecha especial. Juntos fortalecemos nuestra relación, amándonos cada vez más y acompañándonos en cada momento. Este año a tu lado ha sido una montaña rusa de emociones que nunca pensé vivir, porque jamás amé a nadie como te amo a vos. Por eso, ese 16 de agosto quise que fueras mía para siempre.
"""),
    ("Nuestro Segundo mes Juntos", "Foto2.jpeg", """Gracias a esta relación, cada día es una oportunidad para que seamos felices. Los desafíos que trajo el tiempo los superamos juntos y a tu lado no solo me dieron más razones para amarte, sino que me hacen valorar cada abrazo, beso o sonrisa. Me encuentro agradecido por todo lo que hemos vivido.
"""),
    ("Nuestro Tercer mes Juntos", "Foto3.jpeg", """Juntos, seguimos construyendo un amor que se siente más sólido y hermoso con cada paso que damos. Nunca imaginé que alguien pudiera inspirarme a ser una mejor persona como lo hacés vos. Cada día me doy cuenta de la suerte que tengo de tenerte en mi vida. Al lado tuyo aprendí que el amor crece todos los días, y jamás pensé que encontraría tanta paz y felicidad en una sola persona.
"""),
    ("Nuestro Cuarto mes Juntos", "Foto4.jpeg", """Valoro cada vez más lo que compartimos, esos momentos de dos gordos hermosos...
"""),
    ("Nuestro Quinto mes Juntos", "Foto5.jpeg", """Apostamos por el otro, por un amor verdadero y duradero...
"""),
    ("Nuestro Sexto mes Juntos", "Foto6.jpeg", """Juntos, seguimos aprendiendo a amarnos de formas nuevas...
"""),
    ("Nuestro Séptimo mes Juntos", "Foto7.jpeg", """Aprendimos a amarnos, a soportarnos y a tratarnos...
"""),
    ("Nuestro Octavo mes Juntos", "Foto8.jpeg", """Amo hacer planes con vos, pero mi verdadera felicidad es simplemente...
"""),
    ("Nuestro Noveno mes Juntos", "Foto9.jpeg", """Todo el tiempo que estuvimos juntos me hizo ver que no hay amor más grande...
"""),
    ("Nuestro Décimo mes Juntos", "Foto10.jpeg", """Todo el tiempo que pasamos juntos me hizo ver que no hay amor más grande...
"""),
    ("Nuestro Undécimo mes Juntos", "Foto11.jpeg", """Con vos comprendí que cada día es una aventura distinta...
"""),
    ("Nuestro Primer año Juntos", "Foto12.jpeg", """Juntos, construimos una vida llena de risas, apoyo incondicional...
"""),
]

# --- Mostrar cada mes ---
for titulo, archivo_imagen, texto in momentos:
    st.markdown(f"<h2 style='text-align: center;'>{titulo}</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(get_image_path(archivo_imagen), use_container_width=True)
    with col2:
        st.markdown(f"<div style='text-align: center; margin-top: 50px;'><p>{texto}</p></div>", unsafe_allow_html=True)
    st.markdown("---")

