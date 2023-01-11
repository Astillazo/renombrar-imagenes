# Renombrador de imágenes

El objetivo de este proyecto es agilizar el renombrado de imágenes que se encuentren en una misma carpeta para que tengan un nombre con el mismo formato.

Tiene dos posibles aplicativos:

- Remplazar todo el nombre excetpo la _**extensión**_ y la parte que contenga un tamaño con el formato _**LADO x LADO**_, p. ej: _**300x250**_, añadiendo un _**prefjio**_.
- Añadir un _**prefjio**_ y mantener el resto del nombre de la imagen y la _**extensión**_.


## Requisitos
- Python 3.8
- Docker
- Línea de comando UNIX


## Preparar el entorno
Una vez que tenemos clonado el repositorio, vamos a la carpeta de este y ejecutamos el siguiente comando `docker build . --no-cache -t python-rename-images`, la cuál creará un contenedor de Docker, con python 3.8, para ejecutar el script.

Otra opción es usar _**virualenv**_ en vez de _**Docker**_.

## Ejecución
Para ejecutar la versión de python del contenedor desde la línea de comandos, usaremos lo siguiente `docker run --rm -it -v $(pwd)/src:/code python-rename-images python rename-files-with-extension.py`, si hacemos esto, podremos ver los distintos parámetros que tenemos y podemos usar con este script:
````
usage: rename-files-with-extension.py [-h] --prefix PREFIX --folder FOLDER
                                      [--keep_name_remaining KEEP_NAME_REMAINING]
                                      [--action ACTION]
````

Como vemos tenemos los siguientes _obligatorios_:
- **PREFIX**: Con este parámetros, indicamos el prefijos que queremos añadir a todos los nombre de las imágenes de la carpeta donde el script trabajará.
- **FOLDER**: aquí tendremos la ruta de la carpeta, relativa al directorio donde se encuentra el script `src`, en la cuál se encuentran las imágenes a tratar.

Por otra parte, tenemos los parámetros _opcionales_:
- **KEEP_NAME_REMAINING**: Si se provee este parámetro con culaquier opción, se mantendrá el nombre _**actual**_, sin el _**tamaño**_, tras el _**prefijo**_ y el _**tamaño**_.
- **ACTION**: Actualmente solo existe una opción y el la que se ejecuta si no se provee este parámetros, pero lo he añadido para futuras iteraciónes de este script.


## Contacto
En mi web están las distintas formas de contactarme --> [Antonio Madera](https://antoniomadera.com)
