# Read Feeds #

* Autores: Noelia Ruiz Martínez, Mesar Hameed
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

- Filtrar por: un cuadro de edición para buscar feeds anteriormente
buscados.  - Una lista de los feeds guardados.  - Lista de artículos: abre
un diálogo que presenta la lista de artículos de tu feed actual. Selecciona
el artículo que quieras leer y pulsa el botón Aceptar para abrir la página
correspondiente en tu navegador.  - Nuevo: abre un diálogo con un cuadro de
edición para introducir la dirección de un feed nuevo. Si la dirección es
válida y el feed se puede guardar, su nombre, basado en el título del feed,
aparecerá en la parte inferior de la lista de feeds.  - Renombrar: abre un
diálogo con un cuadro de edición para renombrar el feed seleccionado.  -
Eliminar: abre un diálogo para eliminar el feed seleccionado después de la
confirmación.  - Configurar predeterminado: configura el feed seleccionado
como el predeterminado, tal que puede accederse a sus artículos con gestos
de NVDA.  - Cerrar: cierra el diálogo Feeds.

##### Notas #####
- Si se crea un feed llamado tempFeed, por favor renómbralo, ya que este
fichero podría reemplazarse cuando sea necesario crear un feed cuyo nombre
ya exista.  - El feed configurado como el predeterminado puede
eliminarse. el feed addressFile se utilizará como el predeterminado cuando
la configuración se reinicie, así no puede eliminarse.

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

- Ctrl+Shift+NVDA+Espacio: Anuncia la dirección web del presente
artículo. Pulsándola dos veces Se abrirá la página web.  -
Ctrl+Shift+NVDA+8: Refresca el feed seleccionado y anuncia su título más
reciente.  - Ctrl+Shift+NVDA+I: Anuncia el título del feed actual  y el
enlace. Pulsánhdolo dos veces copiará el título y el enlace relacionado al
portapapeles.  - Ctrl+Shift+NVDA+U: Anuncia el título del feed anterior.  -
Ctrl+Shift+NVDA+O: Anuncia el título del siguiente feed.

## Notificaciones: ##

- Cuando el título o la dirección web se hayan copiado.  - Cuando no se
pueda conectar/actualizar un feed, o la dirección web no se corresponda con
un feed válido.  - NVDA mostrará un mensaje de error si no fuera posible
hacer copias de seguridad de la carpeta personalFeeds.  - El título del
cuadro de diálogo Lista de artículos muestra el nombre del feed seleccionado
y el número de elementos disponibles.


## Cambios para 3.0 ##
- Los diálogos para gestionar ficheros de feed se han eliminado. Ahora su
funcionalidad se incluye en el diálogo Feeds.  - La presentación visual de
los diálogos se ha mejorado, adhiriéndose a la apariencia de los diálogos
mostrados en NVDA.  - El feed predeterminado se guarda en la configuración
de NVDA. Por lo tanto, es posible configurar diferentes feeds
predeterminados en los perfiles de configuración.  - Requiere de NVDA
2016.4.


## Cambios para 2.0 ##
- La ayuda del complemento está disponible en el Administrador de
Complementos.

## Cambios para 1.0 ##
- Versión inicial.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf

[2]: http://addons.nvda-project.org/files/get.php?file=rf-dev
