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
        options=["Home", "Iniciar", "Créditos"],  # required
        icons=["house", "caret-right-fill", "caret-right-fill","caret-right-fill",
                        "caret-right-fill", "envelope"],  # optional
        menu_icon="upc-scan",  # optional
        default_index=0,  # optional
    )



if selected == "Home":
	st.title("Experimenta con IA - Adivina el prompt")
	st.write("Esta herramienta te permitirá desarrollar habilidades en el arte de la escritura de prompts.\n \n para la generación de imágenes con IA.\n\n\n\n")
	st.write(' ')
	st.write("**Instrucciones:** \n ")


	"""
	* Selecciona iniciar en el menú de la izquierda.
	* Selecciona una imagen de la lista desplegable. Hay 10 imágenes disponibles.
    * Escribe el prompt que creas se utilizó para generar la imagen. Recuerda que debes escribirlo en inglés pues la mayoría de este tipo de herramientas funcionan sólo en este idioma.
	* Haz clic en el botón "Adivinar".
	* Se mostrará un puntaje de acuerdo a la similitud con el prompt real usado para generar la imagen.
		* El primer valor corresponde al puntaje actual 
		* El segundo al valor más alto de todos los intentos realizados. 

		* Las flechas hacia abajo o hacia arriba indicarán si el puntaje ha subido o bajado de acuerdo a los intentos anteriores.
	* Como último recursos se incluye un checkbox que si lo marcas hará que aparezca el prompt real utilizado para generar la imagen.

	

	\n \n \n NOTA: Esta herramienta es un demo experimental y está sujeta a la demanda de uso. 

	"""