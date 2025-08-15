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
    ("Nuestro Cuarto mes Juntos", "Foto4.jpeg", """Valoro cada vez más lo que compartimos, esos momentos de dos gordos hermosos que nos encanta comer y disfrutar juntos. Ya sean nuestras meriendas, comidas, hamburguesas, pasteles o panchos, cada instante es un tesoro. Por eso, elijo quedarme a tu lado siempre, sin importar las circunstancias. Sin quererlo y sin remedio, cada día me enamoro más de vos, y juntos seguimos sumando recuerdos que atesoraremos para siempre.
"""),
    ("Nuestro Quinto mes Juntos", "Foto5.jpeg", """Apostamos por el otro, por un amor verdadero y duradero, porque hoy no me imagino un futuro, un plan, ni a mí mismo sin vos. Jamás pensé que algo tan bonito pudiera existir para mí, ni que encontraría a alguien que fuera mi calma y mi pilar al mismo tiempo. Juntos nos reímos, soñamos y nos amamos, y eso es lo que más me gusta de nuestra vida.
"""),
    ("Nuestro Sexto mes Juntos", "Foto6.jpeg", """Juntos, seguimos aprendiendo a amarnos de formas nuevas, sin miedo y con entrega total. El tiempo a tu lado me ha hecho sentir emociones que jamás creí posibles. Por eso, cada día reafirmo que sos la mejor decisión que he tomado. Y por eso, cada instante con vos es un tesoro que guardo para siempre.
"""),
    ("Nuestro Séptimo mes Juntos", "Foto7.jpeg", """Aprendimos a amarnos, a soportarnos y a tratarnos, entendiendo nuestras actitudes y diferencias. Con el tiempo, y sin miedo, nos fuimos acomodando el uno para el otro. A tu lado sentí emociones que creía imposibles, cambiando mi panorama por completo. Por eso, hoy reafirmo que sos lo mejor que me pasó en la vida y por eso sos un tesoro para mí.
"""),
    ("Nuestro Octavo mes Juntos", "Foto8.jpeg", """Amo hacer planes con vos, pero mi verdadera felicidad es simplemente el tiempo que pasamos juntos. La presencia de vos a mi lado es suficiente para que todo este amor tenga sentido. Agradezco cada instante que compartimos, donde encuentro paz. Ya sea cuando nos tomamos de la mano, cuando almorzamos o merendamos, o cuando simplemente dormimos juntos, no quiero que el tiempo pase nunca.
"""),
    ("Nuestro Noveno mes Juntos", "Foto9.jpeg", """Todo el tiempo que estuvimos juntos me hizo ver que no hay amor más grande que el que siento por vos. Es como si la vida me hubiera regalado a la persona más maravillosa y por eso para mí sos un milagro. Prometo seguir cuidando y amando lo nuestro para siempre. No voy a soltar tu mano nunca.
"""),
    ("Nuestro Décimo mes Juntos", "Foto10.jpeg", """Todo el tiempo que pasamos juntos me hizo ver que no hay amor más grande que el que siento por vos. Lo que siento es un milagro, como si la vida me hubiese regalado a la persona más linda para tener a mi lado. Prometo seguir cuidando y amando lo nuestro para siempre, y no soltarte nunca.
"""),
    ("Nuestro Undécimo mes Juntos", "Foto11.jpeg", """Con vos comprendí que cada día es una aventura distinta. Juntos, superamos pruebas que nos hicieron más fuertes y más unidos. Aprendí que el amor verdadero es constante y paciente. Ahora, nos hemos convertido en el refugio y la fuerza el uno para el otro.
"""),
    ("Nuestro Primer año Juntos", "Foto12.jpeg", """Juntos, construimos una vida llena de risas, apoyo incondicional y momentos inolvidables. A tu lado, comprendí que no hay amor más grande que el que siento por vos, y que la felicidad más pura se encuentra en las pequeñas cosas que compartimos. Sos mi calma, mi fuerza y el hogar al que siempre quiero volver. Gracias por ser el milagro que cambió mi mundo. Feliz año.
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


