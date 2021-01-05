# Leitor de Feeds (Read Feeds) #

* Autores: Noelia Ruiz Martínez, Mesar Hameed
* Compatibilidade com NVDA: 2019.3 ou posterior
* Baixe a [versão estável][1]
* Baixe a [versão em desenvolvimento][2]


Esse complemento fornece uma maneira direta de ler feeds
(alimentadores/canais/fluxos/fontes) em formato Atom ou RSS usando o
NVDA. Os feeds não serão atualizados automaticamente. Ao mencionarmos feeds
abaixo, referimo-nos tanto a feeds RSS como ATOM.

## Installation or Update ##

Se você usou uma versão anterior deste complemento, e há uma pasta RSS ou
personalFeeds na sua pasta pessoal de configuração do NVDA, ao instalar a
versão atual, uma caixa de diálogo perguntará se você deseja atualizar ou
instalar. Escolha atualizar para preservar seus feeds salvos e continuar
usando-os na nova versão instalada do Leitor de Feeds.

## Commands ##

### Menu Leitor de Feeds ###

Você pode acessar o submenu do Leitor de Feeds a partir do menu do NVDA,
submenu Ferramentas, onde estão disponíveis as opções de menu a seguir:

#### Feeds ####

Abre um diálogo com os seguintes controles:

* Filtrar por: Um campo de edição para procurar feeds anteriormente salvos.
* A list of the saved feeds, focused when the dialog is opened.
* Lista de artigos: Abre uma caixa de diálogo que apresenta a lista de
  artigos do seu feed atual. Selecione o artigo que deseja ler e pressione
  Enter ou o botão Abrir página da web do artigo selecionado para abrir a
  página correspondente no seu navegador. Pressione o botão Sobre o artigo
  para abrir uma caixa de diálogo mostrando o título e o link do artigo
  selecionado; desta caixa de diálogo, você poderá copiar essa informação
  para a área de transferência.
* Abrir feed: Abre o feed selecionado no aplicativo padrão.
* Open feed as HTML: Opens the selected feed in the default web browser. You
  will be able to show or hide publication dates and buttons to copy
  information about articles to clipboard.
* Copy feed address: Opens a dialog to confirm if you want to copy the feed
  address to clipboard.
* Novo: Abre uma caixa de diálogo com uma caixa de edição para inserir o
  endereço de um novo feed. Se o endereço for válido e o feed puder ser
  salvo, seu nome, com base no título do feed, aparecerá na parte inferior
  da lista de feeds.
* Renomear: Abre um diálogo com um campo de edição para renomear o feed
  selecionado.
* Excluir: Abre um diálogo para excluir o feed selecionado após confirmação.
* Definir padrão: Define o feed selecionado como padrão, para que seus
  artigos possam ser acessados com os comandos (gestos) do NVDA.
* Abrir pasta que contém cópia dos feeds: Abre uma pasta que pode conter uma
  cópia dos feeds. Isso pode ser útil para explorar e apagar feeds que não
  devem ser importados quando o complemento é atualizado.
* Preferences: Opens the settings dialog for readFeeds, also available in
  NVDA's menu, Preferences, settings, readFeeds category.
* Fechar: Fecha o diálogo feeds.

##### Notas #####

* Se um feed chamado tempFeed for criado, renomeie-o, pois esse arquivo pode
  ser substituído quando necessário para criar um feed cujo nome já exista.
* O feed definido como padrão não pode ser removido. O endereço do arquivo
  (addressFile) do feed será usado como padrão quando a configuração for
  redefinida, por isso não pode ser excluída.
* The Filter by edit box can be placed after the Open article button from
  NVDA's menu, Preferences, Settings, Read feeds category, or pressing the
  Preferences button of the Feeds dialog.

#### Copy feeds folder ####

Abre uma caixa de diálogo para escolher uma pasta onde você pode salvar o
diretório personalFeeds dos seus feeds. Por padrão, a pasta selecionada é o
diretório de configuração do NVDA, em que criará o diretório personalFeeds.

#### Restore feeds ####

Abre uma caixa de diálogo para selecionar uma pasta que sobrescreve seus
feeds na pasta personalFeeds. Certifique-se de carregar uma pasta contendo
URLs de feeds.

### Keyboard commands ###

* Ctrl+Shift+NVDA+Espaço: Anuncia o URL do artigo atual. Pressionar duas
  vezes abrirá a página web.
* Ctrl+Shift+NVDA+8: Atualiza o feed selecionado e anuncia seu título mais
  recente.
* Ctrl+Shift+NVDA+I: Anuncia o título e o link do feed atual. Pressionar
  duas vezes copiará o título e o link relacionado para a área de
  transferência.
* Ctrl+Shift+NVDA+U: Anuncia o título do feed anterior.
* Ctrl+Shift+NVDA+O: Anuncia o próximo título do feed.

## Notifications ##

* Quando o título ou URL foram copiados.
* Quando não é possível conectar/atualizar um feed ou o URL não corresponde
  a um feed válido.
* NVDA will display an error message if it was not possible to backup or
  restore the personalFeeds folder, and if a new feed cannot be created.
* O título do diálogo Lista de artigos mostra o nome do feed selecionado e o
  número de itens disponíveis.

## Changes for 10.0 ##

* Added a button to open the selected feed as HTML in the default web
  browser.
* If a new feed cannot be created, this will be notified in an error dialog.
* Improved order and presentation of some articles.
* More feeds may be supported.
* When the feeds dialog is opened, the list of feeds will be focused instead
  of the search edit box.
* You can choose if the search edit box is placed after the list of feeds,
  useful to focus the list even when switching from another window without
  closing the Feeds dialog.
* Added a button to copy the feed address to clipboard from the feeds
  dialog.

## Mudanças na 9.0 ##

* Requer NVDA 2019.3 ou posterior.

## Mudanças na 8.0 ##

* Quando o complemento for atualizado, feeds salvos da versão anterior do
  complemento serão automaticamente copiados para a nova versão, a não ser
  que você prefira importar os feeds salvos na pasta principal de
  configurações do NVDA.
* Ao usar o diálogo de copiar feeds, caso a pasta escolhida não seja nomeada
  personalFeeds, será criada uma subpasta com esse nome para prevenir o
  apagamento de diretórios que contenham dados importantes, tais como
  Documentos ou Downloads.

## Mudanças na 7.0 ##

* O diálogo de feeds inclui um botão para abrir uma pasta que pode conter
  uma cópia dos feeds.
* Ao usar a caixa de edição para filtrar os feeds, se nenhum resultado for
  encontrado, a lista de feeds e outros controles serão desabilitados, para
  que o NVDA não anuncie "desconhecido" na lista vazia.
* Se o diálogo de lista de Artigos não puder ser mostrado, por exemplo
  devido a erros no feed, o NVDA disparará um erro, de modo que o diálogo de
  feeds possa ser usado sem reiniciar o NVDA.

## Mudanças na 6.0 ##

* Quando o feed padrão é atualizado e ele para de funcionar devido a
  problemas do servidor, os artigos anteriores não são excluídos e podem ser
  lidos com os pressionamentos de teclas correspondentes.
* Correção de regressão: o feed padrão pode ser atualizado duas vezes
  novamente.

## Mudanças na 5.0 ##

* A caixa de diálogo da lista de artigos foi aprimorada.
* Compatível com o NVDA 2018.3 ou posterior (requerido).
* Se necessário, você pode fazer o download da [última versão compatível com
  o NVDA 2017.3][3].

## Mudanças na 4.0 ##

* Adicionado um botão para abrir o feed selecionado na caixa de diálogo
  Feeds.

## Mudanças na 3.0 ##

* Os diálogos para gerir arquivos de feeds foram removidos. Agora a
  funcionalidade dos mesmos está inclusa no diálogo feeds.
* A apresentação visual dos diálogos foi aprimorada, aderindo à aparência
  dos diálogos exibidos pelo NVDA.
* O feed padrão é salvo nas configurações do NVDA. Assim, é possível
  especificar diferentes feeds padrão em perfis de configurações.
* Requer NVDA 2016.4.

## Mudanças na 2.0 ##

* A ajuda do complemento está disponível no gestor de complementos.

## Mudanças na 1.0 ##

* Versão inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rf

[2]: https://addons.nvda-project.org/files/get.php?file=rf-dev

[3]: https://addons.nvda-project.org/files/get.php?file=rf-o
