# Read Feeds

* Autores: Noelia Ruiz Martínez, Mesar Hameed

Este complemento proporciona una forma sencilla de leer fuentes en formato Atom o RSS mediante NVDA.
Las fuentes no se actualizarán automáticamente.
En adelante, cuando mencionemos fuentes, nos referiremos tanto a las fuentes RSS como a las ATOM.

## Comandos

### Diálogo Leer fuentes

Puedes acceder al diálogo Leer fuentes desde el menú de NVDA, submenú Herramientas, opción Fuentes.

Contiene los siguientes controles:

* Filtrar por: Un cuadro de edición para buscar entre las fuentes guardadas previamente.
* Una lista de las fuentes guardadas, que recibe el foco al abrirse el diálogo.
* Lista de artículos: Abre un diálogo que muestra la lista de artículos de la fuente actual. Selecciona el artículo que deseas leer y pulsa Intro o el botón Abrir la página web del artículo seleccionado para abrir la página correspondiente en tu navegador. Pulsa el botón Acerca del artículo para abrir un diálogo que muestra el título y el enlace del artículo seleccionado; desde este diálogo podrás copiar esta información al portapapeles.
* Abrir fuente: Abre la fuente seleccionada con la aplicación predeterminada.
* Abrir fuente como HTML: Abre la fuente seleccionada en el navegador web predeterminado. Podrás mostrar u ocultar las fechas de publicación y los botones para copiar la información de los artículos al portapapeles.
* Copiar dirección de la fuente: Abre un diálogo para confirmar si deseas copiar la dirección de la fuente al portapapeles.
* Nueva: Abre un diálogo con un cuadro de edición para introducir la dirección de una nueva fuente. Si la dirección es válida y la fuente puede guardarse, su nombre, basado en el título de la fuente, aparecerá al final de la lista de fuentes.
* Cambiar nombre: Abre un diálogo con un cuadro de edición para cambiar el nombre de la fuente seleccionada.
* Eliminar: Abre un diálogo para eliminar la fuente seleccionada tras solicitar confirmación.
* Establecer como predeterminada: Establece la fuente seleccionada como predeterminada para que sus artículos puedan consultarse mediante los gestos de NVDA.
* Importar fuentes desde un archivo OPML: Abre un diálogo para añadir nuevas fuentes desde un archivo OPML.
* Guardar fuentes en un archivo OPML: Abre un diálogo para guardar las fuentes disponibles en el diálogo Fuentes en un archivo OPML.
* Preferencias: Abre el diálogo de configuración de Read Feeds, también disponible desde el menú de NVDA, Preferencias, Configuración, categoría Read Feeds.
* Cerrar: Cierra el diálogo Fuentes.

### Notas

* El cuadro de edición Filtrar por puede colocarse después del botón Abrir artículo desde el menú de NVDA, Preferencias, Configuración, categoría Leer fuentes, o pulsando el botón Preferencias del diálogo Fuentes.
* Este panel dispone de una opción para mostrar las fechas de los artículos en el diálogo Lista de artículos.


### Comandos de teclado

* Ctrl+Mayús+NVDA+Espacio: Anuncia la URL del artículo actual. Al pulsarlo dos veces se abrirá la página web.
* Ctrl+Mayús+NVDA+8: Actualiza la fuente seleccionada y anuncia su título más reciente.
* Ctrl+Mayús+NVDA+I: Anuncia el título y el enlace de la fuente actual. Al pulsarlo dos veces copiará el título y el enlace correspondiente al portapapeles.
* Ctrl+Mayús+NVDA+U: Anuncia el título de la fuente anterior.
* Ctrl+Mayús+NVDA+O: Anuncia el título de la fuente siguiente.

## Notificaciones

* Cuando se hayan copiado el título o la URL.
* Cuando no sea posible conectar o actualizar una fuente, o la URL no corresponda a una fuente válida.
* NVDA mostrará un mensaje de error si no se puede crear una nueva fuente.
* El título del diálogo de la lista de artículos muestra el nombre de la fuente seleccionada y el número de elementos disponibles.

## Cambios de la versión 44.0.0

* Se eliminó el paquete xml, ya incluido en NVDA.

## Cambios de la versión 39.0.0

* Se mejoraron las notificaciones al copiar el título o la URL.

## Cambios de la versión 34.0.0

* Se añadió compatibilidad con las fuentes rss.cbc.ca.

## Cambios de la versión 21.0

* Las fuentes con artículos sin título pueden mostrarse en el diálogo Artículos y abrirse como HTML.

## Cambios de la versión 20.0

* universalFeedParser se ha actualizado a la versión 5.0.1, añadiendo compatibilidad con más fuentes.

## Cambios de la versión 15.0

* Compatible con NVDA 2023.1.

## Cambios de la versión 14.0

* Se corrigió un error que impedía añadir algunas fuentes.

## Cambios de la versión 13.0

* El complemento no puede utilizarse en pantallas seguras.
* Las fuentes se gestionan mediante archivos OPML.
* Debido a los cambios en el sistema de gestión de fuentes, se han producido cambios en el archivo de configuración donde se establece la fuente predeterminada. Utiliza el diálogo Fuentes si deseas volver a configurarla.
* Los antiguos archivos de texto utilizados en versiones anteriores se importarán automáticamente al nuevo formato OPML al iniciar el complemento.
* La función para copiar y restaurar fuentes ha sido sustituida por la posibilidad de importar desde archivos OPML y guardar en ellos.
* Las fuentes con un formato incorrecto pueden procesarse antes de añadirse para hacerlas compatibles con el complemento.
* En el panel de configuración de Leer fuentes, una nueva opción permite mostrar las fechas de los artículos en el diálogo Lista de artículos.

## Cambios de la versión 12.0

* Se corrigió un error que provocaba que los atajos de los elementos del menú Herramientas de NVDA no funcionaran como se esperaba.

## Cambios de la versión 11.0

* Compatible con NVDA 2021.1

## Cambios de la versión 10.0

* Se añadió un botón para abrir la fuente seleccionada como HTML en el navegador web predeterminado.
* Si no puede crearse una nueva fuente, se notificará mediante un diálogo de error.
* Se mejoró el orden y la presentación de algunos artículos.
* Se ha ampliado la compatibilidad con más fuentes.
* Al abrir el diálogo Fuentes, el foco se situará en la lista de fuentes en lugar del cuadro de edición de búsqueda.
* Puedes elegir si el cuadro de edición de búsqueda se coloca después de la lista de fuentes, lo que resulta útil para mantener el foco en la lista incluso al cambiar desde otra ventana sin cerrar el diálogo Fuentes.
* Se añadió un botón para copiar al portapapeles la dirección de la fuente desde el diálogo Fuentes.

## Cambios de la versión 9.0

* Requiere NVDA 2019.3 o una versión posterior.

## Cambios de la versión 8.0

* Al actualizar el complemento, las fuentes guardadas en la versión anterior del complemento se copiarán automáticamente a la nueva versión, a menos que prefieras importar las fuentes guardadas en la carpeta principal de configuración de NVDA.
* Al utilizar el diálogo para copiar fuentes, si la carpeta elegida no se llama personalFeeds, se creará una subcarpeta con ese nombre para evitar la eliminación de directorios que contengan datos importantes, como Documentos o Descargas.

## Cambios de la versión 7.0

* El diálogo Fuentes incluye un botón para abrir una carpeta que puede contener una copia de seguridad de las fuentes.
* Al utilizar el cuadro de edición para filtrar fuentes, si no se encuentra ningún resultado, la lista de fuentes y los demás controles se deshabilitan para que NVDA no anuncie «desconocido» en la lista vacía.
* Si el diálogo de la lista de artículos no puede mostrarse, por ejemplo debido a errores en la fuente, NVDA mostrará un error para que el diálogo Fuentes pueda seguir utilizándose sin necesidad de reiniciar NVDA.

## Cambios de la versión 6.0

* Cuando la fuente predeterminada se ha actualizado y deja de funcionar debido a problemas del servidor, los artículos anteriores no se eliminan y pueden seguir leyéndose mediante las combinaciones de teclas correspondientes.
* Se corrigió una regresión: la fuente predeterminada puede volver a actualizarse dos veces.

## Cambios de la versión 5.0

* Se ha mejorado el diálogo de la lista de artículos.
* Compatible con NVDA 2018.3 o posterior (obligatorio).

## Cambios de la versión 4.0

* Se añadió un botón para abrir la fuente seleccionada desde el diálogo Fuentes.

## Cambios de la versión 3.0

* Se eliminaron los diálogos para gestionar los archivos de fuentes. Ahora esta funcionalidad está integrada en el diálogo Fuentes.
* Se mejoró la presentación visual de los diálogos para ajustarse al aspecto de los diálogos mostrados en NVDA.
* La fuente predeterminada se guarda en la configuración de NVDA. Por lo tanto, es posible establecer distintas fuentes predeterminadas en los perfiles de configuración.
* Requiere NVDA 2016.4.

## Cambios de la versión 2.0

* La ayuda del complemento está disponible desde el Administrador de complementos.

## Cambios de la versión 1.0

* Versión inicial.
