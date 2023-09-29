import streamlit as st
import PIL.Image
from streamlit_option_menu import option_menu



st.set_page_config(
    page_title="Herramientas AI - Qüid Lab",
    page_icon="random",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Oculto botones de Streamlit
#hide_streamlit_style = """
#				<style>
#				#MainMenu {visibility: hidden;}
#
#				footer {visibility: hidden;}
#				</style>
#				"""
#st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Funciones




# Logo sidebar
image = PIL.Image.open('logo_blanco.png')
st.sidebar.image(image, width=None, use_column_width=None)

with st.sidebar:
    selected = option_menu(
        menu_title="Selecciona",  # required
        options=["Home", "Imagenes",  "Texto", "Audio", "Otras", "Créditos"],  # required
        icons=["house", "caret-right-fill", "caret-right-fill","caret-right-fill",
                        "caret-right-fill", "envelope"],  # optional
        menu_icon="upc-scan",  # optional
        default_index=0,  # optional
    )



if selected == "Home":
	st.title("Experimenta con IA - Listado de herramientas externas")
	st.write("En este listado hemos recopilado algunas herramientas que pueden ser de utilidad para la generación de imágenes y texto por medio de IA.\n \n Recuerda que siempre tienes que revisar y validar cualquier respuesta que obtengas de una herramienta IA.\n\n\n\n")
	st.write(' ')
	st.write("**Instrucciones:** \n ")
	"""
	* Selecciona "Imagenes" en el menú de la izquierda si quieres ver el listado de herramientas IA para la generación de imágenes
	* Selecciona "Texto" en el menú de la izquierda si quieres ver el listado de herramientas IA basadas en grandes modelos de lenguaje que te servirán para procesar y/o generar texto.
	* Selecciona "Audio" en el menú de la izquierda si quieres ver el listado de herramientas IA para el procesamiento de audio.
	* Selecciona "Otros" en el menú de la izquierda si quieres ver otras herramientas que pueden ser de utilidad para el proceso de innovación.
	* Recuerda que estas experimentando y lo importante, más que el resultado, es reconocer las ventajas de la IA.

	\n \n \n NOTA: Esta herramienta es un demo experimental y está sujeta a la demanda de uso. 

	"""






