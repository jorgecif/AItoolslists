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


if selected == "Imágenes":

		st.title(f"Herramientas IA para la generación de imágenes")
		st.write("Algunas herramientas:")
		"""
		* Herramientas que me permiten buscar prompts como referencia
			* http://lexica.art 
			* https://prompthero.com/ 

		* Herramientas para generar imágenes a partir de prompts:
			* Stable Diffusion
				* https://stablediffusionweb.com/#demo 
			* Lexica ART
				* https://lexica.art/aperture
			* Midjourney
				* http://midjourney.com/ 
				* Discord Server: https://discord.gg/midjourney 
			* https://www.bluewillow.ai/ 
				* Discord Server: https://discord.gg/UrgFx5RS 
			* Bing Image Creator (Dall-e)
				* https://www.bing.com/images/create 
			* Scribble Diffusion 
				* https://scribblediffusion.com/
			* ControlNet 
				* https://stablediffusionweb.com/ControlNet#demo
			* Dream by Wombo
				* https://dream.ai/create
			* Leonardo AI
				* https://leonardo.ai/			

		* Herramientas para editar imágenes con IA:
			* Leonardo AI 
			    * Hacer que continue una imagen - extender - Outpainting
				* Añadir un objeto a una imagen
				* https://leonardo.ai/
			* PlaygroundAI
				* Quitar un objeto de una imagen
				* https://playgroundai.com/
			* Pixelbin
				* Eliminar fondo
				* Elimnar marca de agua de imágenes
				* Eliminar logos de imágenes
				* Mejorar la calidad de una imagen (de imagen pixelada a nítida - escala la imagen)
				* Comprimir imagen y reducir su tamaño
				* https://www.pixelbin.io/products
			* Clipdrop
				* Cambiar la iluminación de una imagen - Relight
				* Eliminar textos de una imagen (carteles, marcas, etc)
				* Generar imágenes alternativas similares a una de referencia
				* https://clipdrop.co/
			* Clipdrop - Stable Diffusion - Reimagine
				* Crear variaciones de imagen a partir otra
				* https://clipdrop.co/stable-diffusion-reimagine?ref=producthunt	
			* Clipdrop - Stable Diffusion - Uncrop
				* Herramienta para expandir imágenes - outpainting
				* https://clipdrop.co/uncrop			
		"""

if selected == "Texto":
		st.title(f"Herramientas IA para el procesamiento de texto")
		st.write("Algunas herramientas:")
		"""
		* Herramientas para el procesamiento y generación de textos (Grandes modelos de lenguaje o LLM):
			* https://chat.openai.com/chat
			* https://bing.com/chat
			* https://www.notion.so/
		* Herramientas para parafrasear un texto manteniendo su significado:
			* https://www.paraphraser.io/
		* Herramienta para crear un chat de preguntas y respuestas con documentos en PDF: 
			* https://www.chatpdf.com/

		"""



if selected == "Audio":


		st.title(f"Herramientas IA para el procesamiento de audio")
		st.write("Algunas herramientas:") 
		"""
		* Herramientas para transcribir textos:
			* https://podcastle.ai/
			* https://www.notta.ai/
			* Herramienta para extraer audio de un video: https://audio-extractor.net/es/
		"""

if selected == "Otras":

		st.title(f"Otras herramientas que pueden ser útiles")
		st.write("Algunas herramientas:")
		"""
		* Herramientas para el procesamiento de audio:
			* Herramienta para hacer videos: Microsoft Climchamp (para editar videos, recortar, etc): https://clipchamp.com/ 

		"""








if selected == "Créditos":
	st.title(f"Seleccionaste la opción {selected}")
	st.write(' ')
	st.write(' ')
	st.subheader("Qüid Lab")
	body = '<a href="https://www.quidlab.co">https://www.quidlab.co</a>'
	linkedin = 'Linkedin: <a href="https://www.linkedin.com/in/jorgecif/">https://www.linkedin.com/in/jorgecif/</a>' 
	twitter = 'Twitter (X): <a href="https://twitter.com/jorgecif/">https://twitter.com/jorgecif/</a>' 
	st.markdown(body, unsafe_allow_html=True)
	st.write('Creado por: *Jorge O. Cifuentes* :fleur_de_lis:')
	st.markdown(linkedin, unsafe_allow_html=True)
	st.markdown(twitter, unsafe_allow_html=True)

	st.write('Email: *jorge@quidlab.co* ')
	st.write("Quid Lab AI tools")
	st.write("Version 1.0")
	st.text("")







