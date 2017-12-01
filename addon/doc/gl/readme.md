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

* Filtrar por: unha Caixa de edición para procurar feeds gardados
  anteriormente.
* Unha listaxe dos feeds gardados.
* Listaxe de artigos: abre un diálogo que presenta a listaxe de artigos do
  teu feed actual. Seleciona o artigo que queras ler e preme o botón Aceptar
  para abrir a páxina correspondente no teu navegador.
* Novo: abre un diálogo cunha Caixa de edición para introducir o enderezo
  dun feed novo. Se o enderezo é válido e o feed pode gardarse, o seu nome,
  baseado no título do feed, aparecerá ao fondo da listaxe dos feeds.
* Renomear: abre un diálogo cunha Caixa de edición para renomear o feed
  selecionado.
* Borrar: abre un diálogo para borrar o feed selecionado despois dunha
  confirmación.
* Configurar predeterminado: configura o feed selecionado coma o
  predeterminado, así que o seu artigo pode acederse cos xestos do NVDA.
* Pechar: pecha o diálogo Feeds.

##### Notas #####

* - Se se crea un feed chamado tempFeed, por favor renoméao, xa que este
  fichero podería reemplazarse cando sexa necesario crear un feed cun nome
  que xa exista.
* O feed configurado como o predeterminado pode borrarse. O feed addressFile
  usarase coma o predeterminado cando a configuración se reinicie, así non
  pode borrarse.

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

* Ctrl+Shift+NVDA+Espazo: anuncia a URL actual dos artigos. Premendo dúas
  veces abrirá a páxina web.
* Ctrl+Shift+NVDA+8: refresca o feed selecionado e anuncia o seu título máis
  recente.
* Ctrl+Shift+NVDA+I: anuncia o título e a liga do feed actual. Premendo dúas
  veces copiará o título e a liga relacionada ao portapapeis.
* Ctrl+Shift+NVDA+U: anuncia o título do feed anterior.
* Ctrl+Shift+NVDA+O: anuncia o título do feed seguinte.

## Notificacións: ##

* Cando o título ou a URL se copiaran.
* Cando non se pode conectar/refrescar un feed, ou a URL non se corresponde
  cun feed válido.
* NVDA amosará unha mensaxe de erro se non foi posible respaldar ou
  restaurar o cartafol personalFeeds.
* O título do diálogo da listaxe de artigos amopsa o nome do feed
  selecionado e o número de elementos dispoñibles.


## Cambios para 3.0 ##

* Elimináronse os diálogos para xestionar os ficheiros de feeds. Agora a súa
  funcionalidade inclúese no diálogo Feeds.
* Mellorouse a presentación visual dos diálogos, adheríndose á apariencia
  dos diálogos amosada no NVDA.
* O feed predeterminado gárdase na configuración do NVDA. Polo tanto, é
  posible configurar diferentes feeds predeterminados nos perfís de
  configuración.
* Requírese do NVDA 2016.4.


## Cambios para 2.0 ##

* A axuda está dispoñible no Administrador de Complementos.

## Cambios para 1.0 ##

* Versión inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rf

[2]: https://addons.nvda-project.org/files/get.php?file=rf-dev
