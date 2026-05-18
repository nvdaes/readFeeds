# Read Feeds

- Autores: Noelia Ruiz Martínez, Mesar Hameed
- Compatible con NVDA 2021.1
- Download [stable version][1]
- Download [development version][2]

Este complemento proporciona una manera fácil de leer fuentes en formatos de
RSS o Atom utilizando NVDA.
Los feeds no se actualizarán automáticamente.
En adelante cuando mencionemos feeds, nos referiremos a los feeds RSS y
ATOM.

## Installation or Update:

If you used a previous version of this addon, and there is an RSS or personalFeeds folder in your personal NVDA configuration folder,
when installing the current version, a dialog will ask if you want to upgrade or install.
Choose update to preserve your saved feeds and to continue using them in the new installed version of readFeeds.

## Commands:

### Read Feeds menu

Puedes acceder al diálogo de Read Feeds desde el menú NVDA, submenú
Herramientas, elemento Read Feeds.

#### Feeds...

Opens a dialog with the following controls:

- Filtrar por: un cuadro de edición para buscar feeds guardados con
  anterioridad.
- A list of the saved feeds.
- Lista de artículos: abre un diálogo que presenta la lista de artículos de
  tu feed actual. Selecciona el artículo que desees leer y pulsa Intro o el
  botón Abrir página web del artículo seleccionado para abrir la página
  correspondiente en tu navegador. Presiona el botón Acerca del artículo
  para abrir un diálogo que muestre el título y el enlace del artículo
  seleccionado; desde este diálogo, podrás copiar esta información al
  portapapeles.
- Abrir feed: abre el feed seleccionado en la aplicación predeterminada.
- Nuevo: abre un diálogo con un cuadro de edición para introducir la
  dirección de un feed nuevo. Si la dirección es válida y el feed puede
  guardarse, su nombre, basado en el título del feed, aparecerá al fondo de
  la lista de feeds.
- Renombrar: abre un diálogo con un cuadro de edición para renombrar el feed
  seleccionado.
- Eliminar: abre un diálogo para eliminar el feed seleccionado después de
  una confirmación.
- Configurar predeterminado: configura el feed seleccionado como el
  predeterminado, así que su artículo puede accederse con gestos de NVDA.
- Open folder containing a backup of feeds: Opens a folder which may contain a backup of feeds. This can be useful to explore and delete feeds which shouldn't be imported when the add-on is updated.
- Cerrar: cierra el diálogo Feeds.

##### Notas

- If a feed named tempFeed is created, please rename it, as this file could be replaced when needed to create a feed whose name already exists.
- The feed set as the default can't be removed. The addressFile feed will be use as the default when the configuration is reset, so it can't be deleted.

\####Copy feeds folder... ####

Opens a dialog to choose a folder where you can save the personalFeeds directory of your feeds. By default the selected folder is the NVDA's configuration directory, which will create the personalFeeds directory.

#### Restore feeds...

Opens a dialog to select a folder which replaces your feeds in the personalFeeds folder. Make sure you load a folder containing feeds URLs.

### Órdenes de teclado

- Ctrl+Shift+NVDA+Espacio: anuncia la URL actual de los artículos. Pulsando
  dos veces abrirá la página web.
- Ctrl+Shift+NVDA+8: refresca el feed seleccionado y anuncia su título más
  reciente.
- Ctrl+Shift+NVDA+I: anuncia el título y el enlace del feed actual. Pulsando
  dos veces copiará el título y el enlace relacionado al portapapeles.
- Ctrl+Shift+NVDA+U: anuncia el título del feed anterior.
- Ctrl+Shift+NVDA+O: anuncia el título del feed siguiente.

## Notificaciones

- Cuando el título o la URL se haya copiado.
- Cuando no se pueda conectar/refrescar un feed, o la URL no se corresponda
  con un feed válido.
- NVDA mostrará un mensaje de error si no fue posible respaldar o restaurar
  la carpeta personalFeeds o si no se puede NVDA mostrará un mensaje de
  error si no se puede crear un nuevo feed.
- El título del diálogo de lista de artículos muestra el nombre del feed
  seleccionado y el número de elementos disponibles.

## Cambios para 8.0

- Cuando se actualice el complemento, las fuentes guardadas en la versión
  anterior del complemento se copiarán automáticamente a la nueva versión, a
  menos que prefieras importar fuentes guardadas en la carpeta de
  configuración principal de NVDA.
- Al usar el diálogo para copiar fuentes, si la carpeta elegida no se llama
  personalFeeds, se creará una subcarpeta con este nombre para evitar la
  eliminación de directorios que contengan datos importantes, como
  Documentos o Descargas.

## Cambios para 7.0

- El diálogo Fuentes incluye un botón para abrir una carpeta que podría
  contener una copia de seguridad de las fuentes.
- Al usar el cuadro de edición para filtrar fuentes, si no se encuentran
  resultados, la lista de fuentes y otros controles están deshabilitados, de
  manera que NVDA no anuncie "desconocido" en la lista vacía.
- Si el diálogo de lista de artículos no se puede mostrar, por ejemplo
  debido a errores en la fuente, NVDA disparará un error, de forma que el
  diálogo de fuentes pueda usarse sin reiniciar NVDA.

## Cambios para 6.0

- Cuando se refresca el feed por defecto y deja de funcionar por errores en
  el servidor, los artículos anteriores no se borran y pueden leerse con los
  atajos correspondientes.
- Solucionada regresión: El feed por defecto puede actualizarse dos veces
  nuevamente.

## Cambios para 5.0

- El diálogo lista de artículos se ha mejorado.
- Compatible con NVDA 2018.3 o posterior (requerido).
- If needed, you can download the [last version compatible with NVDA 2017.3][3].

## Cambios para 4.0

- Añadido un botón para abrir el feed seleccionado desde el diálogo Feeds.

## Cambios para 3.0

- Se han eliminado los diálogos para gestionar los ficheros de feeds. Ahora
  su funcionalidad se incluye en el diálogo Feeds.
- Se ha mejorado la presentación visual de los diálogos, adhiriéndose a la
  apariencia de los diálogos mostrada en NVDA.
- El feed predeterminado se guarda en la configuración de NVDA. Por lo
  tanto, es posible configurar diferentes feeds predeterminados en los
  perfiles de configuración.
- Se requiere NVDA 2016.4.

## Cambios para 2.0

- La ayuda del complemento está disponible en el Administrador de
  Complementos.

## Cambios para 1.0

- Versión inicial.

[1]: http://addons.nvda-project.org/files/get.php?file=rf
[2]: http://addons.nvda-project.org/files/get.php?file=rf-dev
[3]: http://addons.nvda-project.org/files/get.php?file=rf-o
