# Read Feeds #

* Autores: Noelia Ruiz Martínez, Mesar Hameed
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

- Lista de artigos...  Presenta a lista de artigos dende o actual
feed. Selecciona o artigo que queras ler e preme o botón Aceptar para abrir
a páxina correspondente no teu navegador.  - Enderezo temporal de
feed... control + NVDA + shift + intro: abre un diálogo para escreber un
enderezo web novo para seleccionar outro feed. O enderezo web actual
amosarase neste cadro de diálogo.  - Cargar enderezo do feed dende
ficheiro... NVDA+control+intro: abre un diálogo para seleccionar un feed
dende un ficheiro gardado que conteña un enderezo web dun feed.  - Gardar
enderezo actual de feed a ficheiro... NVDA+shift+intro: abre un diálogo para
seleccionar o ficheiro onde se gardará o enderezo web actual do feed.  Se
gardas no ficheiro especial addressFile.txt, este feed en particular
utilizarase como o teu feed predeterminado.  - Refrescar feed actual:
control+shift+NVDA+8: Actualiza o feed seleccionado. Os feeds non se
actualizarán automáticamente cando se inicie o complemento Read Feeds.  -
Salvagardar cartafol de feeds...  Abre un diálogo para escoller un cartafol
onde se pode gardar o directorio personalFeeds dos teus feeds. De maneira
predeterminada o cartafol seleccionado é o directorio de configuración do
NVDA, que creará o directorio personalFeeds.  - Restaurar feeds...  Abre un
diálogo para seleccionar un cartafol que sustitúua os feeds no cartafol
personalFeeds. Asegúrate de cargar un cartafol que conteña os enderezos web
dos RSS.

### Ordes de teclado: ###

- Ctrl+Shift+NVDA+Espazo: Anuncia o enderezo web do presente
artigo. preméndoa dúas veces abrirase a páxina web.  - Ctrl+Shift+NVDA+8:
Refresca o feed seleccionado e anuncia o seu título máis recente.  -
Ctrl+Shift+NVDA+I: Anuncia o título do feed actual . preméndoo dúas veces
copiará o título e a liga relacionada ó portapapeis.  - Ctrl+Shift+NVDA+U:
Anuncia o título do feed anterior.  - Ctrl+Shift+NVDA+O: Anuncia o título do
seguinte feed.

## Notificacións: ##

- Cando o título ou o enderezo web se copiaran.  - Cando non se poida
conectar/actualizar un feed, ou o enderezo web non se corresponda cun feed
válido.  - NVDA amosará unha mesaxe de erro se non fora posible facer copias
de seguridade do cartafol personalFeeds.  - O título do cadro de diálogo
Lista de artigos amosa o nome da fonte seleccionada e o número de artigos
dispoñibles.

## Cambios para 1.0 ##
*	 Versión inicial.

[[!tag dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf-dev

[2]: http://addons.nvda-project.org/files/get.php?file=rf

