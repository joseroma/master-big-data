## Enunciado ejercicio 1

Dado un archivo que contiene en cada línea una palabra o conjunto de palabras seguido de un valor numérico, denominado “sentimiento”, y un conjunto de tweets, se pide calcular para cada tweet un valor denominado “sentimiento del tweet”, que se obtiene como la suma de los “sentimientos” de los términos que aparecen en el tweet.


Obsérvese que:

- Cada línea del fichero Tweets.txt contiene una cadena JSON.
- No todas las líneas del archivo Tweets.txt contiene tweets.
- Cada tweet es representado por una cadena en formato JSON, en la que el tweet es almacenado en la clave text.

Para procesar el archivo hay que tener en cuenta que cada palabra o conjunto de palabras están separadas de su valor mediante el carácter “\t”. El archivo podría almacenarse en un diccionario usando el siguiente trozo de código (figura 9.2.).

Como resultado, se debe mostrar por pantalla un valor numérico en cada línea que represente el “sentimiento” de un tweet.

No todos los tweets que se van a considerar tienen contenido, por lo que hay que filtrar aquellos que tienen de los que no tienen.

El programa tendrá 2 parámetros de entrada: el archivo que contiene los sentimientos de los términos y el archivo que contiene los tweets. Estos parámetros se pueden leer como input desde el teclado, directamente en el código o como parámetros con sys.args.


## Resumen

### Input

El programa tendrá 2 parámetros de entrada: 
	- Los términos y valores de los sentimientos [Archivo]
	- Los tweets [Archivo]
	
Estos parámetros se pueden leer como:
	- input desde el teclado, directamente en el código 
	- o como parámetros con sys.args.


## Resultado

Como resultado, se debe mostrar por pantalla un valor numérico en cada línea que represente el “sentimiento” de un tweet.

***Importante recordar***

No todos los tweets que se van a considerar tienen contenido, por lo que hay que filtrar aquellos que tienen de los que no tienen.

