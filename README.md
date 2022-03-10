# Ejercicios_Ordenar

Enlace a mi repositorio: [Ejercicios_Ordenar](https://github.com/Xavitheforce/Ejercicios_Ordenar)

En el repositorio encontrarás tanto los UML como los flowcharts(también disponibles en este documento tras cada codigo). A continuación voy a explicar brevemente el funcionamiento externo(interno= UML y codigo) de cada ejercicio():

1) Ejercicio de ordenar por dicotomía:

    Este ejercicios tiene 2 partes:
  
    La primera ordena la lista introducida previamente usando bucles que recorren esta lista y van comparando elemento a elemento.
  
    La segunda ordena la lista introducida previamente con ayuda de una lista en blanco a la que se le van metiendo los elementos de la primera. Este algoritmo compara cada vez que se introduce una palabra con la palabra que hay en la mitad de la lista y decide en base al BOOLEAN obtenido si introducirla hacia la derecha o hacia la izquierda(y la mueve en esa dirección hasta colocarla).
  
2) Ejercicio de ordenación topológica:

    Mi interpretación de este ejercicio ha sido bastante simple. De una lista de tareas con un par de numeros asociados coge cada par de numeros y los compara basandose en la posicion que tiene la tarea(el par representa el antes y despues = tras establecer el 1º, comprueba los despues del par y busca el elemento en la posicion indicada, y así hasta llegar a elementos inexistentes o acabar de ordenar las tareas)

3) Ejercicio de especificaciones:

    Este ejercicio crea una lista de largo aleatorio, con números dentro de un rango introducido aleatorios y la segmenta según le dice el usuario(obviamente el segmento debe ser igual o menor a la lista). El segmento producido lo divide en tantas partes como quiera el usuario (todo dentro de la misma lista inicial) y ejecuta las condiciones:
#para segmentar pide un minimo y un maximo. estos se refieren a la posicion del elemento 1 y a la del elemento final que van dentro del segmento.(si len(lista)=10, el segmento puede ser 2(minimo) a 8(maximo), y por lo tanto en la lista quedarán 1 elemento al principio, el segmento(que tendrá los elementos 2,3,4,...,8) y los elementos finales que no pertenecían al segmento(9,10)). cabe destacar que es notacion normal y no de listas de python(se entiende que el primer elemento es el 1 y no el 0)
 
  -busca el maximo de cada subsegmento
 
  -extrae el máximo(lo que mueve a la izquierda los elementos del subsegmento a la derecha de este)
 
  -introduce de nuevo ese máximo extraido a la derecha del todo del subsegmento
