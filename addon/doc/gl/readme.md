# Read Feeds #

* Autores: Noelia Ruiz Martínez, Mesar Hameed
* Descargar [versión estable][1]
* Descargar [versión de desenvolvemento][2]

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

Podes acceder ó submenú Read Feeds dende o menú NVDA, submenú Ferramentas,
onde están dispoñibles as seguintes opcións:

#### Feeds... ####

Abre un diálogo cos seguintes controis:

- Filtrar por: una Caixa de edición para procurar feeds anteriormente
procurados.  - Unha lista dos feeds gardados.  - Lista de artigos: abre un
diálogo que presenta a lista de artigos do teu feed actual. Seleciona o
artigo que queras ler e preme o botón Aceptar para abrir la páxina
correspondente no teu navegador.  - Novo: abre un diálogo cunha Caixa  de
edición para introducir o enderezo dun feed novo. Se o enderezo é válido e o
feed pódese gardar, o seu nome, baseado no título do feed, aparecerá na
parte inferior da lista dos feeds.  - Renomear: abre un diálogo cunha Caixa
de edición para renomear o feed selecionado.  - Borrar: abre un diálogo para
borrar o feed selecionado despois da confirmación.  - Configurar
predeterminado: configura o feed selecionado coma o predeterminado, tal que
pode acederse aos seus artigos con xestos do NVDA.  - Pechar: pecha o
diálogo Feeds.

##### Notas #####
- Se se crea un feed chamado tempFeed, por favor renoméao, xa que este
fichero podería reemplazarse cando sexa necesario crear un feed cun nome que
xa exista.  - O feed configurado como o predeterminado pode borrarse. O feed
addressFile usarase coma o predeterminado cando a configuración se reinicie,
así non pode borrarse.

####Copiar cartafol feeds... ####

Abre un diálogo para escoller un catafol onde podes gardar o directorio
personalFeeds dos teus feeds. Por defecto a carpeta selecionada é o
directorio de configuración do NVDA, o que creará o directorio
personalFeeds.

#### Restaurar feeds... ####

Abre un diálogo para seleccionar un cartafol que reemplaza os teus feeds no
cartafol personalFeeds. Asegúrate de cargar un cartafol contendo URLs de
feeds.

### Ordes de teclado: ###

- Ctrl+Shift+NVDA+Espazo: Anuncia o enderezo web do presente
artigo. preméndoa dúas veces abrirase a páxina web.  - Ctrl+Shift+NVDA+8:
Refresca o feed seleccionado e anuncia o seu título máis recente.  -
Ctrl+Shift+NVDA+I: Anuncia o título do feed actual e a liga. preméndoo dúas
veces copiará o título e a liga relacionada ó portapapeis.  -
Ctrl+Shift+NVDA+U: Anuncia o título do feed anterior.  - Ctrl+Shift+NVDA+O:
Anuncia o título do seguinte feed.

## Notificacións: ##

- Cando o título ou o enderezo web se copiaran.  - Cando non se poida
conectar/actualizar un feed, ou o enderezo web non se corresponda cun feed
válido.  - NVDA amosará unha mesaxe de erro se non fora posible facer copias
de seguridade do cartafol personalFeeds.  - O título do cadro de diálogo
Lista de artigos amosa o nome do feed seleccionado e o número de elementos
dispoñibles.


## Cambios para 3.0 ##
- Os diálogos para xestionar ficheiros de feed borráronse. Agora a súa
funcionalidade inclúese no diálogo Feeds.  - A presentación visual dos
diálogos mellorouse, adheríndose á apariencia dos diálogos amosados no
NVDA.  - O feed predeterminado gárdase na configuración do NVDA. Polo tanto,
é posible configurar diferentes feeds predeterminados nos perfís de
configuración.  - Requírese NVDA 2016.4.


## Cambios para 2.0 ##
- A axuda está dispoñible no Administrador de Complementos.

## Cambios para 1.0 ##
- Versión inicial.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf

[2]: http://addons.nvda-project.org/files/get.php?file=rf-dev
