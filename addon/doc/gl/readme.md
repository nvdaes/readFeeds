# Read Feeds #

* Autores: Noelia Ruiz Martínez, Mesar Hameed
* Download [stable version][1] (compatible with NVDA 2019.3 and beyond)
* Download [development version][2] (compatible with NVDA 2019.3 and beyond)

Este complemento proporciona unha maneira sinxela de ler fontes en formatos
de RSS ou Atom utilizando NVDA.  Os feeds non se actualizarán
automáticamente.  No futuro cando mencionemos feeds, referirémonos ós feeds
RSS e ATOM.

## Ordes ##

### Read Feeds dialog ###

You can access the Read Feeds dialog from the nvda menu, Tools submenu,
Feeds item.

It contains the following controls:

* Filtrar por: unha Caixa de edición para procurar feeds gardados
  anteriormente.
* Unha lista das fontes gardadas, enfocada ao abrirse o diálogo.
* Listaxe de artigos: abre un diálogo que amosa a listaxe de artigos do teu
  feed actual. Seleciona o artigo que desexes ler e preme Intro ou o botón
  Abrir páxina web do artigo selecionado para abrir a páxina correspondente
  no teu navegador. Preme o botón Acerca do artigo para abrir un diálogo que
  amose o título e a liga do artigo selecionado; dende este diálogo, poderás
  copiar esta información ao portapapeis.
* Abrir feed: abre o feed selecionado na aplicación predeterminada.
* Abrir fonte como HTML: Abre a fonte seleccionada no navegador web por
  defecto. Poderás ocultar datas de publicación e botóns para copiar
  información sobre os artigos ao portapapeis.
* Copiar enderezo da fonte: Abre un diálogo para confirmar se queres copiar
  o enderezo da fonte ó portapapeis.
* Novo: abre un diálogo cunha Caixa de edición para introducir o enderezo
  dun feed novo. Se o enderezo é válido e o feed pode gardarse, o seu nome,
  baseado no título do feed, aparecerá ao fondo da listaxe dos feeds.
* Renomear: abre un diálogo cunha Caixa de edición para renomear o feed
  selecionado.
* Borrar: abre un diálogo para borrar o feed selecionado despois dunha
  confirmación.
* Configurar predeterminado: configura o feed selecionado coma o
  predeterminado, así que o seu artigo pode acederse cos xestos do NVDA.
* Import feeds from OPML file: Opens a dialog to add new feeds from an OPML
  file.
* Save feeds to OPML file: Opens a dialog to save the feeds available from
  the Feeds dialog in an OPML file.
* Preferencias: Abre o diálogo de opcións para ReadFeeds, tamén dispoñible
  no menú NVDA, Preferencias, Opcións, categoría ReadFeeds.
* Pechar: pecha o diálogo Feeds.

### Notes #####

* A caixa de edición filtrar por pódese poñer despois do botón Abrir artigo
  dende o menú NVDA, Preferencias, Opcións, categoría Read Feeds, ou
  premendo o botón Preferencias do diálogo de fontes.
* This panel has an option to show article dates on the List of articles
  dialog.


### Ordes de teclado ###

* Ctrl+Shift+NVDA+Espazo: anuncia a URL actual dos artigos. Premendo dúas
  veces abrirá a páxina web.
* Ctrl+Shift+NVDA+8: refresca o feed selecionado e anuncia o seu título máis
  recente.
* Ctrl+Shift+NVDA+I: anuncia o título e a liga do feed actual. Premendo dúas
  veces copiará o título e a liga relacionada ao portapapeis.
* Ctrl+Shift+NVDA+U: anuncia o título do feed anterior.
* Ctrl+Shift+NVDA+O: anuncia o título do feed seguinte.

## Notificacións ##

* Cando o título ou a URL se copiaran.
* Cando non se pode conectar/refrescar un feed, ou a URL non se corresponde
  cun feed válido.
* NVDA will display an error message if a new feed cannot be created.
* O título do diálogo da listaxe de artigos amopsa o nome do feed
  selecionado e o número de elementos dispoñibles.

## Changes for 14.0

* Fixed a bug that made impossible to add some feeds.

## Changes for 13.0

* The add-on cannot be used on secure screens.
* Feeds are managed from OPML files.
* Due to changes in the feeds management system, there are changes in the
  configuration file where the default feed is set. Please, use the Feeds
  dialog if you want to set it again.
* Your old text files used in previous versions will be automatically
  imported into the new OPML format when the add-on is started.
* The copy and restore feeds feature has been replaced with the ability to
  import from and save to OPML files.
* Non well-formed feeds can be processed before being added to make them
  compatible with the add-on.
* In the Read Feeds settings panel, a new option allows to show article
  dates on the List of articles dialog.

## Cambios para 12.0

* Arranxado un erro polo que os atallos do menú ferramentas de NVDA non
  funcionaban como se agardaba.

## Cambios para 11.0

* Compatible con NVDA 2021.1

## Cambios para 10.0 ##

* Engadido un botón para abrir o feed selecionado como HTML no navegador web
  predeterminado.
* Se non se pode crear unha nova fonte, notificarase nun diálogo de erro.
* Mellorada a orde e a presentación dalgúns artigos.
* Poderíanse soportar máis fontes.
* Cando se abre o diálogo de fontes, enfocarase a lista de fontes no canto
  da caixa de edición de busca.
* Podes escoller se a caixa de edición de busca se sitúa despois da lista de
  fontes, útil para enfocar a lista aínda despois de moverse dende outra
  xanela sen pechar o diálogo de fontes.
* Engadido un botón para copiar o enderezo da fonte ao portapapeis dende o
  diálogo de fontes.

## Cambios para 9.0 ##

* Require NVDA 2019.3 ou posterior.

## Cambios para 8.0 ##

* Cando o complemento se actualice, os feeds gardados na versión anterior do
  complemento copiaranse automaticamente á nova versión, a menos que
  prefiras importar os feeds gardados no cartafol principal de configuración
  de NVDA.
* Ao utilizar o diálogo para copiar feeds, se o cartafol escollido non se
  chama personalFeeds, crearase un subcartafol con ese nome para previr a
  eliminación de directorios que conteñan datos importantes, como Documentos
  ou Descargas.

## Cambios para 7.0 ##

* O diálogo Fontes contén un botón para abrir un cartafol que podería conter
  unha copia de seguridade das fontes.
* Ao usar a caixa de edición para filtrar fontes, se non se atopan
  resultados, amosaranse a lista de feeds e outros controis, de tal modo que
  NVDA non anuncie "Descoñecido" na lista baleira.
* Se o diálogo lista de artículos non se pode amosar, debido a erros no
  feed, por exemplo, NVDA disparará un erro, de modo que o diálogo de fontes
  se poida usar sen reiniciar NVDA.

## Cambios para 6.0 ##

* Cando se refresca o feed por omisión e deixa de funcionar por problemas no
  servidor, os artigos anteriores non se borran e poden lerse coas ordes
  correspondentes.
* Solucionada regresión: O feed por defecto pódese actualizar dúas veces
  novamente.

## Cambios para 5.0 ##

* Mellorouse o diálogo listaxe de artigos.
* Compatible co NVDA 2018.3 ou posterior (requerido).
* Se fora necesario, podes descargar a [última versión compatible co NVDA
  2017.3][3].

## Cambios para 4.0 ##

* Engadido un botón para abrir o feed selecionado dende o diálogo Feeds.

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

[3]: https://addons.nvda-project.org/files/get.php?file=rf-o
