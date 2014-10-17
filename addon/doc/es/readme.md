# Read Feeds #

* Autores: Noelia Ruiz Martínez, Mesar Hameed
* Descargar [versión estable][2]
* Descargar [versión de desarrollo][1]

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

Puedes acceder al submenú Read Feeds desde el menú NVDA, NVDA+N, donde están
disponibles las siguientes opciones de menú:

- Lista de artículos...  Presenta la lista de artículos desde el actual
feed. Selecciona el artículo que quieras leer y pulsa el botón Aceptar para
abrir la página correspondiente en tu navegador.  - Dirección temporal de
feed... control + NVDA + shift + intro: abre un diálogo para escribir una
dirección web nueva para seleccionar otro feed. la dirección web actual se
mostrará en este cuadro de diálogo.  - Cargar dirección del feed desde
fichero... NVDA+control+intro: abre un diálogo para seleccionar un feed
desde un fichero guardado que contenga una dirección web de un feed.  -
Guardar dirección actual de feed a fichero... NVDA+shift+intro: abre un
diálogo para seleccionar el fichero donde se guardará la dirección web
actual del feed.  Si guardas en el fichero especial addressFile.txt, este
feed en particular se utilizará como tu feed predeterminado.  - Refrescar
feed actual: control+shift+NVDA+8: Actualiza el feed seleccionado. Los feeds
no se actualizarán automáticamente cuando se inicie el complemento Read
Feeds.  - Respaldar carpeta de feeds...  Abre un diálogo para elegir una
carpeta donde se puede guardar el directorio personalFeeds de tus feeds. De
manera predeterminada la carpeta seleccionada es el directorio de
configuración de NVDA, que creará el directorio personalFeeds.  - Restaurar
feeds...  Abre un diálogo para seleccionar una carpeta que sustituya los
feeds en la carpeta personalFeeds. Asegúrate de cargar una carpeta que
contenga las direcciones web de los RSS.

Nota: Si quieres eliminar  una URL del feed previamente guardado, elimina
sólo el fichero correspondiente.

### Órdenes de teclado: ###

- Ctrl+Shift+NVDA+Espacio: Anuncia la dirección web del presente
artículo. Pulsándola dos veces Se abrirá la página web.  -
Ctrl+Shift+NVDA+8: Refresca el feed seleccionado y anuncia su título más
reciente.  - Ctrl+Shift+NVDA+I: Anuncia el título del feed actual
. Pulsánhdolo dos veces copiará el título y el enlace relacionado al
portapapeles.  - Ctrl+Shift+NVDA+U: Anuncia el título del feed anterior.  -
Ctrl+Shift+NVDA+O: Anuncia el título del siguiente feed.

## Notificaciones: ##

- Cuando el título o la dirección web se hayan copiado.  - Cuando no se
pueda conectar/actualizar un feed, o la dirección web no se corresponda con
un feed válido.  - NVDA mostrará un mensaje de error si no fuera posible
hacer copias de seguridad de la carpeta personalFeeds.  - El título del
cuadro de diálogo Lista de artículos muestra el nombre de la fuente
seleccionada y el número de artículos disponibles.

## Cambios para 2.0 ##
*	 La ayuda del complemento está disponible en el Administrador de
   Complementos.

## Cambios para 1.0 ##
*	 Versión inicial.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf-dev

[2]: http://addons.nvda-project.org/files/get.php?file=rf

