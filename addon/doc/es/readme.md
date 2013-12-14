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

*	 Lista de artículos ... Presenta la lista de artículos de tu feed
   actual. Selecciona el artículo que desees leer y pulsa el botón Aceptar
   para abrir la página correspondiente en tu navegador.
*	 Dirección Temporal del feed... control + NVDA + shift + enter: Abre un
   cuadro de diálogo para escribir una nueva dirección URL para seleccionar
   otro feed. La URL actual se muestra en este cuadro de diálogo.
*	 Cargar dirección del feed de fichero... NVDA+control+enter: Abre un
   diálogo para seleccionar una fuente de un fichero guardado que contenga
   una URL del feed.
*	 Guardar  dirección actual del feed a fichero... NVDA+shift+enter: abre un
   diálogo para seleccionar el fichero donde se guardará el URL del feed
   actual. Si lo guardas en el fichero especial addressFile.txt, este feed
   en particular se utilizará como tu feed predeterminado.
*	 Actualizar feed actual: control+shift+NVDA+8: Actualiza el feed
   seleccionado. Los feeds no se actualizarán automáticamente cuando el
   complemento Read Feeds se inicie.
*	 Respaldar carpeta feeds... abre un diálogo para elegir una carpeta donde
   puedes guardar el directorio personalFeeds de tus feeds. Por omisión la
   carpeta seleccionada es el directorio de configuración del NVDA, donde se
   creará el directorio personalFeeds.
*	 Restaurar feeds... Abre un diálogo para seleccionar la carpeta que
   reemplace tus feeds en la carpeta personalFeeds. Asegúrese de cargar una
   carpeta que contenga las URLs de los feeds.

### Órdenes de teclado: ###

*	 Ctrl+Shift+NVDA+Espacio: Anuncia la URL del artículo actual. Pulsando dos
   veces se abrirá la página web.
*	 Ctrl+Shift+NVDA+8: Actualiza el feed seleccionado y anuncia su título más
   reciente.
*	 Ctrl+Shift+NVDA+I: Anuncia el título del feed actual. Pulsando dos veces
   se copia el título y el enlace relacionado al portapapeles.
*	 Ctrl+Shift+NVDA+U: Anuncia el título del feed anterior.
*	 Ctrl+Shift+NVDA+O: Anuncia el título del siguiente feed.

## Notificaciones: ##

*	 Cuando el título o la URL se hayan copiado.
*	 Cuando no pueda conectarse/actualizar  un feed, o la URL no se
   corresponda con un feed válido.
*	 NVDA mostrará un mensaje de error si no fuera posible hacer copias de
   seguridad de la carpeta personalFeeds.
*	 El título del diálogo lista de artículos muestra el nombre del feed
   seleccionado y el número de elementos disponibles.

## Cambios para 1.0 ##
*	 Versión inicial.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf-dev

[2]: http://addons.nvda-project.org/files/get.php?file=rf

