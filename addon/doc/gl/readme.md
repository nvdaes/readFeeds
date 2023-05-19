# Read Feeds #

* Autores: Noelia Ruiz Martínez, Mesar Hameed
* [descargar versión estable][1] (compatible con NVDA 2019.3 en diante)
* Download [beta version][2] (compatible with NVDA 2019.3 and beyond)

Este complemento proporciona unha maneira sinxela de ler fontes en formatos
de RSS ou Atom utilizando NVDA.  Os feeds non se actualizarán
automáticamente.  No futuro cando mencionemos feeds, referirémonos ós feeds
RSS e ATOM.

## Ordes ##

### Diálogo Read Feeds ###

Podes acceder ó diálogo Read Feeds dende o menú nvda, submenú Ferramentas,
elemento Feeds.

Contén os seguintes controis:

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
* Importar fontes dende arquivo OPML: Abre un diálogo para engadir novas
  fontes dende un arquivo OPML.
* Gardar fontes en arquivo OPML: Abre un diálogo para gardar as fontes
  dispoñibles dende o diálogo de fontes nun arquivo OPML.
* Preferencias: Abre o diálogo de opcións para ReadFeeds, tamén dispoñible
  no menú NVDA, Preferencias, Opcións, categoría ReadFeeds.
* Pechar: pecha o diálogo Feeds.

### Notas #####

* A caixa de edición filtrar por pódese poñer despois do botón Abrir artigo
  dende o menú NVDA, Preferencias, Opcións, categoría Read Feeds, ou
  premendo o botón Preferencias do diálogo de fontes.
* Este panel ten unha opción para amosar as datas dos artigos no diálogo de
  lista de artigos.


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
* NVDA amosará unha mensaxe de erro se non se pode crear unha nova fonte.
* O título do diálogo da listaxe de artigos amopsa o nome do feed
  selecionado e o número de elementos dispoñibles.

## Changes for 21.0

* Feeds with untitled articles can be presented in the Articles dialog, and
  opened as HTML.

## Changes for 20.0

* universalFeedParser is updated to 5.0.1, adding support for more feeds.

## Cambios para 14.0

* Arranxado un erro que facía imposible engadir certas fontes.

## Cambios para 13.0

* O complemento non se pode utilizar en pantallas seguras.
* As fontes xestiónanse mediante arquivos OPML.
* Por mor de cambios no sistema de xestión de fontes, hai cambios no arquivo
  de configuración onde se establece a fonte por defecto. Por favor, utiliza
  o diálogo Fontes se desexas configurala de novo.
* Os teus antigos arquivos de texto utilizados en versións anteriores
  importaranse automaticamente no novo formato OPML cando se inicie o
  complemento.
* A característica de copiar e restaurar fontes reemprazouse pola
  posibilidade de importar dende e gardar en arquivos OPML.
* Pódense procesar fontes malformadas antes de engadirse para facelas
  compatibles co complemento.
* No panel de opcións de Read Feeds, unha nova opción permite amosar as
  datas dos artigos no diálogo de Lista de artigos.

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

[1]: https://addons.nvda-project.org/files/get.php?file=readFeeds

[2]: https://www.nvaccess.org/addonStore/legacy?file=readFeeds-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=rf-o
