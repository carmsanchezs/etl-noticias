# etl-noticias
En este repositorios podremos ver como se extrae la información de un sitio web con python usando BeautifulSoup

## Descripción

Este repositorio es de la primer asignación de la capacitación en InTechMon como Data Engineer. Está inspirado en el ejemplo proporcionado por nuestro mentor, Julio. Se centra en la extracción de datos de dos fuentes web diferentes:

**bs4_get_fake_jobs.py**: Este script, basado en el tutorial de Real Python disponible aquí, muestra cómo realizar web scraping para obtener datos de [fake python jobs](https://realpython.github.io/fake-jobs/)

**bs4_get_100GreatestMovies.py**: Este script lleva a cabo web scraping en la página de Empire para obtener las [100 mejores películas según Empire](https://www.empireonline.com/movies/features/best-movies-2/). La URL utilizada es esta. Los datos extraídos se almacenan en un archivo CSV llamado "data_100GreatestMovies.csv".

## Uso
Para utilizar estos scripts:

1. Asegúrate de crear tu [ambiente virtual](https://realpython.com/python-virtual-environments-a-primer/) e instalar las librerias necesarias que están en requiremets.txt

```bash
pip install -r requirements.txt
```

2. Ejecuta los scripts según tus necesidades. Por ejemplo, para ejecutar el script bs4_get_fake_jobs.py, simplemente ejecuta:

```bash
python bs4_get_fake_jobs.py
```
Esto aplicará el scraping en [fake python jobs](https://realpython.github.io/fake-jobs/)

o bien 

```bash
python bs4_get_100GreatestMovies.py
```
Esto aplicará el scraping en [100 mejores películas según Empire](https://www.empireonline.com/movies/features/best-movies-2/)

##Contribución
¡Las contribuciones son bienvenidas! Si deseas mejorar estos scripts, por favor, siéntete libre de hacer un fork del repositorio, realizar tus cambios y enviar un pull request.

## Créditos
Inspirado por Julio, nuestro mentor en InTechMom.
Tutorial de Real Python para el script bs4_get_fake_jobs.py.

## Licencia
Este proyecto está bajo la Licencia MIT. 


_¡Gracias por tu interés en el proyecto!_ 
_Made with love_:heart:



