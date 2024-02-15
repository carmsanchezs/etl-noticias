import requests
from bs4 import BeautifulSoup
import pandas as pd
import mysql.connector
import datetime

# Definimos la URL de la noticia donde queremos sacar la info
url = "https://as.com/futbol/internacional/luis-enrique-cambia-al-psg-n/"

# Enviamos una solicitud a la URL y obtenemos el contenido HTML
response = requests.get(url)
html_content = response.content

# Creamos un objeto BeautifulSoup a partir del HTML que sacamos
soup = BeautifulSoup(html_content, "html.parser")

# Extraemos el título de la noticia ubicada en la etiqueta "h1" con clase "art__hdl__tl"
titulo = soup.find("h1", class_="art__hdl__tl").text
print("titulo:",titulo)

# Extraemos la descripción de la noticia ubicada en la etiqueta "h2" con clase "art__hdl__opn"
descripcion = soup.find("h2", class_="art__hdl__opn").text
print("descripcion:", descripcion)

# Extraemos la URL de la imagen que está en "img" con clase "mm__img"
imagen_url = soup.find("img", class_="mm__img").get("src")
print("linkimagen",imagen_url)

#fecha de la noticia
fecha_hora = datetime.datetime.now()

# Creamos un DataFrame de Pandas
df = pd.DataFrame({
    "titulo": [titulo],
    "descripcion": [descripcion],
    "imagen_url": [imagen_url],
    "fecha": [fecha_hora]
})
#imprimimos la variable df para visualizar la información de la nociticas
print(df)

# Establecemos la conexión con la base de datos MySQL, en mi caso usé una en local host. OJO, esto no es necesario, solo si quieren almacenar la información de la noticia
mydb = mysql.connector.connect(
    host="IP DEL SERVER",
    user="USUARIO DE LA BASE DE DATOS",
    password="CONTRASEÑA DE LA BASE DE DATOS",
    database="NOMBRE DE LA BASE DE DATOS",
    port="3306"
)

# Insertamos los datos en la tabla noticie creada anteriormente con los campos name, descripcion, image, fecha
cursor = mydb.cursor()
sql = "INSERT INTO noticie (name, descripcion, image, fecha) VALUES (%s, %s, %s, %s)"
valores = (titulo, descripcion, imagen_url, fecha_hora)
print(valores)
cursor.execute(sql, valores)
mydb.commit()
cursor.close()

# Al imprimir este mensaje es sinónbimo de la finalización de la consulta.
print("Noticia almacenada correctamente en nuestra base de datos")
