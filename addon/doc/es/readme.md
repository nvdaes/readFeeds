# Read Feeds #

* Autores: Noelia Ruiz Martínez, Mesar Hameed
* Descargar [versión estable][1] (compatible desde NVDA 2019.3 en adelante)
* Descargar [versión beta][2] (compatible desde NVDA 2019.3 en adelante)

Este complemento proporciona una manera fácil de leer fuentes en formatos de
RSS o Atom utilizando NVDA.  Los feeds no se actualizarán automáticamente.
En adelante cuando mencionemos feeds, nos referiremos a los feeds RSS y
ATOM.

## Órdenes ##

### El diálogo de Read Feeds ###

Puedes acceder al diálogo de Read Feeds desde el menú NVDA, submenú
Herramientas, elemento Read Feeds.

Contiene los siguientes controles:

* Filtrar por: un cuadro de edición para buscar feeds guardados con
  anterioridad.
* Una lista de los feeds guardados, que recibe el foco cuando se abre el
  diálogo.
* Lista de artículos: abre un diálogo que presenta la lista de artículos de
  tu feed actual. Selecciona el artículo que desees leer y pulsa Intro o el
  botón Abrir página web del artículo seleccionado para abrir la página
  correspondiente en tu navegador. Presiona el botón Acerca del artículo
  para abrir un diálogo que muestre el título y el enlace del artículo
  seleccionado; desde este diálogo, podrás copiar esta información al
  portapapeles.
* Abrir feed: abre el feed seleccionado en la aplicación predeterminada.
* Abrir feed como HTML: abre el feed seleccionado en el navegador web
  predeterminado. Podrás mostrar u ocultar fechas de publicación y botones
  para copiar información sobre los artículos al portapapeles.
* Copiar dirección del feed: abre un diálogo para confirmar si quieres
  copiar la dirección del feed al portapapeles.
* Nuevo: abre un diálogo con un cuadro de edición para introducir la
  dirección de un feed nuevo. Si la dirección es válida y el feed puede
  guardarse, su nombre, basado en el título del feed, aparecerá al fondo de
  la lista de feeds.
* Renombrar: abre un diálogo con un cuadro de edición para renombrar el feed
  seleccionado.
* Eliminar: abre un diálogo para eliminar el feed seleccionado después de
  una confirmación.
* Configurar predeterminado: configura el feed seleccionado como el
  predeterminado, así que su artículo puede accederse con gestos de NVDA.
* Importar feeds desde archivo OPML: abre un diálogo para añadir nuevos
  feeds desde un archivo OPML.
* Guardar feeds en archivo OPML: abre un diálogo para guardar los feeds
  disponibles en el diálogo de feeds en un archivo OPML.
* Preferencias: abre el diálogo de opciones de Read Feeds, también
  disponible en el menú NVDA, Preferencias, Opciones, categoría Read Feeds.
* Cerrar: cierra el diálogo Feeds.

### Notas

* El cuadro de edición Filtrar por se puede situar tras el botón Abrir
  artículo desde el menú NVDA, Preferencias, Opciones, categoría Read Feeds,
  o pulsando el botón Preferencias en el diálogo de feeds.
* Este panel tiene una opción para mostrar la fecha de los artículos en el
  diálogo de lista de artículos.


### Órdenes de teclado ###

* Ctrl+Shift+NVDA+Espacio: anuncia la URL actual de los artículos. Pulsando
  dos veces abrirá la página web.
* Ctrl+Shift+NVDA+8: refresca el feed seleccionado y anuncia su título más
  reciente.
* Ctrl+Shift+NVDA+I: anuncia el título y el enlace del feed actual. Pulsando
  dos veces copiará el título y el enlace relacionado al portapapeles.
* Ctrl+Shift+NVDA+U: anuncia el título del feed anterior.
* Ctrl+Shift+NVDA+O: anuncia el título del feed siguiente.

## Notificaciones ##

* Cuando el título o la URL se haya copiado.
* Cuando no se pueda conectar/refrescar un feed, o la URL no se corresponda
  con un feed válido.
* NVDA mostrará un mensaje de error si no fue posible respaldar o restaurar
  la carpeta personalFeeds o si no se puede NVDA mostrará un mensaje de
  error si no se puede crear un nuevo feed.
* El título del diálogo de lista de artículos muestra el nombre del feed
  seleccionado y el número de elementos disponibles.

## Cambios para 21.0

* Las fuentes con artículos sin título se pueden presentar en el diálogo de
  artículos, y abrirse como HTML.

## Cambios para 20.0

* se actualiza universalFeedParser a la versión 5.0.1, añadiendo soporte
  para más fuentes.

## Cambios para 14.0

* Corregido un fallo que hacía imposible añadir algunos feeds.

## Cambios para 13.0

* El complemento no se puede usar en pantallas seguras.
* Los feeds se gestionan desde archivos OPML.
* A causa de los cambios en el sistema de gestión de feeds, hay cambios en
  el archivo de configuración donde se configura el feed predeterminado. Usa
  el diálogo de feeds si quieres volver a configurarlo.
* Tus antiguos ficheros de texto usados en versiones anteriores se
  importarán automáticamente en formato OPML cuando se inicie el
  complemento.
* La función de copiar y restaurar feeds se ha reemplazado con la capacidad
  de importar y guardar en archivos OPML.
* Los feeds mal formados pueden procesarse antes de añadirlos para que sean
  compatibles con el complemento.
* En el panel de opciones de Read Feeds, una nueva opción permite mostrar la
  fecha de los artículos en el diálogo de lista de artículos.

## Cambios para 12.0

* Corregido un problema que hacía que los atajos del menú Herramientas de
  NVDA no funcionaran como se esperaba.

## Cambios para 11.0

* Compatible con NVDA 2021.1

## Cambios para 10.0 ##

* Añadido un botón para abrir el feed seleccionado como HTML en el navegador
  web predeterminado.
* Si no se puede crear un nuevo feed, un diálogo de error lo notificará.
* Mejorado el orden y la presentación de algunos artículos.
* Se pueden soportar más feeds.
* Cuando se abra el diálogo de feeds, la lista de feeds recibirá el foco en
  lugar del cuadro de edición para filtrar.
* Puedes elegir si el cuadro de búsqueda se sitúa tras la lista de feeds,
  útil para poner el foco en la lista incluso al pasar desde otra ventana
  sin cerrar el diálogo de feeds.
* Añadido un botón para copiar la dirección del feed al portapapeles desde
  el diálogo de feeds.

## Cambios para 9.0 ##

* Se requiere NVDA 2019.3 o posterior.

## Cambios para 8.0 ##

* Cuando se actualice el complemento, las fuentes guardadas en la versión
  anterior del complemento se copiarán automáticamente a la nueva versión, a
  menos que prefieras importar fuentes guardadas en la carpeta de
  configuración principal de NVDA.
* Al usar el diálogo para copiar fuentes, si la carpeta elegida no se llama
  personalFeeds, se creará una subcarpeta con este nombre para evitar la
  eliminación de directorios que contengan datos importantes, como
  Documentos o Descargas.

## Cambios para 7.0 ##

* El diálogo Fuentes incluye un botón para abrir una carpeta que podría
  contener una copia de seguridad de las fuentes.
* Al usar el cuadro de edición para filtrar fuentes, si no se encuentran
  resultados, la lista de fuentes y otros controles están deshabilitados, de
  manera que NVDA no anuncie "desconocido" en la lista vacía.
* Si el diálogo de lista de artículos no se puede mostrar, por ejemplo
  debido a errores en la fuente, NVDA disparará un error, de forma que el
  diálogo de fuentes pueda usarse sin reiniciar NVDA.

## Cambios para 6.0 ##

* Cuando se refresca el feed por defecto y deja de funcionar por errores en
  el servidor, los artículos anteriores no se borran y pueden leerse con los
  atajos correspondientes.
* Solucionada regresión: El feed por defecto puede actualizarse dos veces
  nuevamente.

## Cambios para 5.0 ##

* El diálogo lista de artículos se ha mejorado.
* Compatible con NVDA 2018.3 o posterior (requerido).
* Si fuese necesario, puedes descargar la [última  versión compatible con
  NVDA 2017.3][3].

## Cambios para 4.0 ##

* Añadido un botón para abrir el feed seleccionado desde el diálogo Feeds.

## Cambios para 3.0 ##

* Se han eliminado los diálogos para gestionar los ficheros de feeds. Ahora
  su funcionalidad se incluye en el diálogo Feeds.
* Se ha mejorado la presentación visual de los diálogos, adhiriéndose a la
  apariencia de los diálogos mostrada en NVDA.
* El feed predeterminado se guarda en la configuración de NVDA. Por lo
  tanto, es posible configurar diferentes feeds predeterminados en los
  perfiles de configuración.
* Se requiere NVDA 2016.4.

## Cambios para 2.0 ##

* La ayuda del complemento está disponible en el Administrador de
  Complementos.

## Cambios para 1.0 ##

* Versión inicial.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=readFeeds

[2]: https://www.nvaccess.org/addonStore/legacy?file=readFeeds-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=rf-o
