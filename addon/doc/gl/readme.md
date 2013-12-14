# Read Feeds #

* Autores: Noelia Ruiz Martínez, Mesar Hameed
* Descargar [versión estable][2]
* Descargar [versión de desenvoolvemento][1]

Este complemento proporciona unha maneira sinxela de ler fontes en formatos
de RSS ou Atom utilizando NVDA.  Os feeds non se actualizarán
automáticamente.  No futuro cando mencionemos feeds, referirémonos ós feeds
RSS e ATOM.

## Instalación ou actualización: ##

Se utilizaches unha versión anterior deste complemento, e hai un cartafol
personalFeeds ou RSS na carpeta personal de configuración do NVDA, ó se
instalar a versión 6.0 ou posterior, un cadro de diálogo preguntarache se
desexas actualizar ou instalar.  Selecciona Actualizar para conservar os
teus feeds gardados e continuar utilizándoos na nova versión instalada de
readFeeds.

## Ordes: ##

### Menú Read Feeds ###

Podes acceder ó submenú Read Feeds dende o menú NVDA, NVDA+N, onde están
dispoñibles as seguintes opcións de menú:

*	 Lista de artigos... Presenta a lista de artigos a partir do teu feed
   actual. Selecciona o artigo que desexes ler e preme o botón Aceptar para
   abrir a páxina correspondente no teu navegador.
*	 Enderezo temporal do feed... control + NVDA + shift + enter: Abre un
   diálogo para introducir un novo URL para seleccionar outro feed. O URL
   actual mostrarase neste diálogo.
*	 Cargar enderezo do feed dende ficheiro... NVDA+control+enter: Abre un
   diálogo para seleccionar un feed dende un ficheiro gardado que conteña
   unha URL do feed.
*	 Gardar enderezo do feed actual no ficheiro... NVDA+shift+enter: abre unha
   caixa de diálogo para seleccionar o ficheiro onde se gardará a URL do
   feed actual. Se o gardas no ficheiro especial addressFile.txt, este feed
   en particular empregarase como o teu feed predeterminado.
*	 Actualizar feed actual: control+shift+NVDA+8: Actualiza o feed
   seleccionado. Os feeds non será actualizado automaticamente cando o
   complemento Read Feeds arranque.
*	 Respaldar cartafol de feeds... abre un diálogo para escoller a carpeta
   onde podes gardar o directorio personalFeeds dos teus feeds. De maneira
   predeterminada o cartafol seleccionado é o directorio de configuración de
   NVDA, no que se creará o directorio personalFeeds.
*	 Restaurar feeds... Abre un diálogo para seleccionar un cartafol que
   substitúa os teus feeds no cartafol personalFeeds . Asegúrese de cargar
   un cartafol que conteña URLs de feeds.

### Ordes de teclado: ###

*	 Ctrl+Shift+NVDA+Espazo: Anuncia URL do artigo actual. Premendo dúas veces
   podes abrir a páxina web.
*	 Ctrl+Shift+NVDA+8: Actualiza o feed seleccionado e anuncia o seu título
   máis recente.
*	 Ctrl+Shift+NVDA+I: Anuncia o título do feed actual. Premendo dúas veces
   pode copiar o título e a liga relacionado ó portapapeis.
*	 Ctrl+Shift+NVDA+U: Anuncia o título do feed anterior.
*	 Ctrl+Shift+NVDA+O: Anuncia o seguinte título do feed.

## Notificacións: ##

*	 Cando o título ou o URL foron copiados.
*	 Cando non se pode conectar / actualizar un feed ou o URL non se
   corresponde a un feed válido.
*	 NVDA pode amosar unha mensaxe de erro se non fose posíble facer a copia
   de seguridade do cartafol personalFeeds.
*	 O título do diálogo lista de artigos amosa o nome do feed seleccionado e
   o número de elementos dispoñibles.

## Cambios para 1.0 ##
*	 Versión inicial.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf-dev

[2]: http://addons.nvda-project.org/files/get.php?file=rf

