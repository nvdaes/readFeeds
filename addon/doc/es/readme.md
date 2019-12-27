# Read Feeds #

* Autores: Noelia Ruiz Martínez, Mesar Hameed
* Compatibilidad con NVDA: de 2018.3 a 2019.2
* Descargar [versión estable][1]
* Descargar [versión de desarrollo][2]

Este complemento proporciona una manera fácil de leer fuentes en formatos de
RSS o Atom utilizando NVDA.  Los feeds no se actualizarán automáticamente.
En adelante cuando mencionemos feeds, nos referiremos a los feeds RSS y
ATOM.

## Instalación o actualización: ##

Si has utilizado una versión anterior de este complemento, y hay una carpeta
personalFeeds o RSS en la carpeta personal de configuración de NVDA, al
instalar la versión 6.0 o posterior, un cuadro de diálogo te preguntará si
deseas actualizar o instalar.  Selecciona Actualizar para preservar tus
feeds guardados y continuar utilizándolos en la nueva versión instalada
dereadFeeds.

## Órdenes: ##

### Menú Read Feeds ###

Puedes acceder al submenú Read Feeds desde el menú NVDA, submenú
herramientas, donde están disponibles las siguientes opciones:

#### Feeds... ####

Abre un diálogo con los siguientes controles:

* Filtrar por: un cuadro de edición para buscar feeds guardados con
  anterioridad.
* Una lista de los feeds guardados.
* Lista de artículos: abre un diálogo que presenta la lista de artículos de
  tu feed actual. Selecciona el artículo que desees leer y pulsa Intro o el
  botón Abrir página web del artículo seleccionado para abrir la página
  correspondiente en tu navegador. Presiona el botón Acerca del artículo
  para abrir un diálogo que muestre el título y el enlace del artículo
  seleccionado; desde este diálogo, podrás copiar esta información al
  portapapeles.
* Abrir feed: abre el feed seleccionado en la aplicación predeterminada.
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
* Abrir carpeta que contiene una copia de seguridad de las fuentes: Abre una
  carpeta que podría contener una copia de seguridad de las fuentes. Esto
  puede ser útil para explorar y eliminar fuentes que no deberían importarse
  cuando el complemento se actualice.
* Cerrar: cierra el diálogo Feeds.

##### Notas #####

* Si se crea un feed llamado tempFeed, por favor renómbralo, ya que este
  fichero podría reemplazarse cuando sea necesario crear un feed cuyo nombre
  ya exista.
* El feed configurado como el predeterminado puede eliminarse. el feed
  addressFile se utilizará como el predeterminado cuando la configuración se
  reinicie, así no puede eliminarse.

####Copiar carpeta feeds... ####

Abre un diálogo para elegir una carpeta donde puedes guardar el directorio
personalFeeds de tus feeds. Por omisión la carpeta seleccionada es el
directorio de configuración de NVDA, el cual creará el directorio
personalFeeds.

#### Restaurar feeds... ####

Abre un diálogo para seleccionar una carpeta que reemplaza tus feeds en la
carpeta personalFeeds. Asegúrate de cargar una carpeta conteniendo URLs de
feeds.

### Órdenes de teclado: ###

* Ctrl+Shift+NVDA+Espacio: anuncia la URL actual de los artículos. Pulsando
  dos veces abrirá la página web.
* Ctrl+Shift+NVDA+8: refresca el feed seleccionado y anuncia su título más
  reciente.
* Ctrl+Shift+NVDA+I: anuncia el título y el enlace del feed actual. Pulsando
  dos veces copiará el título y el enlace relacionado al portapapeles.
* Ctrl+Shift+NVDA+U: anuncia el título del feed anterior.
* Ctrl+Shift+NVDA+O: anuncia el título del feed siguiente.

## Notificaciones: ##

* Cuando el título o la URL se haya copiado.
* Cuando no se pueda conectar/refrescar un feed, o la URL no se corresponda
  con un feed válido.
* NVDA mostrará un mensaje de error si no fue posible respaldar o restaurar
  la carpeta personalFeeds.
* El título del diálogo de lista de artículos muestra el nombre del feed
  seleccionado y el número de elementos disponibles.

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

[1]: https://addons.nvda-project.org/files/get.php?file=rf

[2]: https://addons.nvda-project.org/files/get.php?file=rf-dev

[3]: https://addons.nvda-project.org/files/get.php?file=rf-o
