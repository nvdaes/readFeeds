# Leitor de fíds #

* Autores: Noelia Ruiz Martínez, Mesar Hameed
* Baixe a [versão estável][1]
* Baixe a [versão em desenvolvimento][2]

Este complemento fornece uma maneira direta de ler fíds em formato Atom ou
RSS usando o NVDA. Os fíds não são atualizados automaticamente.  Ao
mencionarmos fíds abaixo, referimo-nos tanto a fíds RSS como ATOM.

## Instalar ou atualizar: ##

If you used a previous version of this addon, and there is an RSS or
personalFeeds folder in your personal NVDA configuration folder, when
installing the current version, a dialog will ask if you want to upgrade or
install.  Choose update to preserve your saved feeds and to continue using
them in the new installed version of readFeeds.

## Comandos: ##

### Menu Leitor de Fíds ###

Você pode acessar o submenu do Leitor de Fíds a partir do menu do NVDA,
submenu Ferramentas, onde são disponíveis as opções de menu a seguir:

#### Fíds... ####

Abre um diálogo com os seguintes controles:

* Filtrar por: Um campo de edição para procurar fíds anteriormente salvos.
* Uma lista com os fíds salvos.
* List of articles: Opens a dialog which presents the articles list from
  your current feed. Select the article you want to read and press OK button
  to open the corresponding page in your browser.
* Open feed: Opens the selected feed in the default application.
* New: Opens a dialog with an edit box to enter the address of a new
  feed. If the address is valid and the feed can be saved, its name, based
  on the feed title, will appear at the bottom of the feeds list.
* Renomear: Abre um diálogo com um campo de edição para renomear o fíd
  selecionado.
* Excluir: Abre um diálogo para excluir o fíd selecionado após confirmação.
* Set default: Sets the selected feed as the default, so that its articles
  can be accessed with NVDA's gestures.
* Fechar: Fecha o diálogo fíds.

##### Notas #####

* If a feed named tempFeed is created, please rename it, as this file could
  be replaced when needed to create a feed whose name already exists.
* The feed set as the default can't be removed. The addressFile feed will be
  use as the default when the configuration is reset, so it can't be
  deleted.

####Copy feeds folder... ####

Opens a dialog to choose a folder where you can save the personalFeeds
directory of your feeds. By default the selected folder is the NVDA's
configuration directory, which will create the personalFeeds directory.

#### Restaurar fíds... ####

Opens a dialog to select a folder which replaces your feeds in the
personalFeeds folder. Make sure you load a folder containing feeds URLs.

### Comandos de teclado: ###

* Ctrl+Shift+NVDA+Space: Announces current article's URL. Pressing twice
  will open the web page.
* Ctrl+Shift+NVDA+8: Refreshes the selected feed and announces its most
  recent title.
* Ctrl+Shift+NVDA+I: Announces current feed title and link. Pressing twice
  will copy the title and related link to clipboard.
* Ctrl+Shift+NVDA+U: Announces previous feed title.
* Ctrl+Shift+NVDA+O: Announces next feed title.

## Notificações: ##

* When the title or URL have been copied.
* When unable to connect/refresh a feed, or the URL does not correspond to a
  valid feed.
* O NVDA mostrará uma mensagem de erro se não tiver sido possível fazer uma
  cópia ou restaurar a pasta personalFeeds.
* O título do diálogo Lista de artigos mostra o nome do fíd selecionado e o
  número de itens disponíveis.



## Changes for 4.0 ##

* Added a button to open the selected feed from the Feeds dialog.

## Mudanças na 3.0 ##

* Os diálogos para gerir arquivos de fíds foram removidos. Agora a
  funcionalidade dos mesmos está inclusa no diálogo fíds.
* A apresentação visual dos diálogos foi aprimorada, aderindo à aparência
  dos diálogos exibidos pelo NVDA.
* O fíd padrão é salvo nas configurações do NVDA. Assim, é possível
  especificar diferentes fíds padrão em perfis de configurações.
* Requer NVDA 2016.4.


## Mudanças na 2.0 ##

* A ajuda do complemento está disponível no gestor de complementos.

## Mudanças na 1.0 ##

* Versão inicial.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf

[2]: http://addons.nvda-project.org/files/get.php?file=rf-dev
