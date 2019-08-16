# Leitor de RSS #

* Autores: Noelia Ruiz Martínez, Mesar Hameed
* NVDA compatibility: 2018.3 to 2019.2
* Baixar [versão estável][1]
* Baixar [versão de desenvolvimento][2]

Este extra fornece uma maneira directa de ler feeds em formatos Atom ou RSS
usando o NVDA. Os feeds não serão actualizados automaticamente. quando
falamos de feeds, queremos dizer feeds RSS e ATOM.

## Instalação ou actualização: ##

Se usou uma versão anterior deste addon e existe uma pasta RSS ou
pessoalFeeds na sua pasta pessoal de configuração do NVDA, ao instalar a
versão actual, uma caixa de diálogo perguntará se deseja actualizar ou
instalar. Escolha a actualização para preservar os seus feeds guardados e
continuar a usá-los na nova versão instalada do readFeeds.

## Comandos: ##

### Menu do leitor de RSS: ###

Pode aceder ao submenu leitor de RSS no menu do nvda, submenu Ferramentas,
onde estão disponíveis as seguintes opções de menu:

#### RSS... ####

Abre um diálogo com os seguintes controlos:

* Filtrar por: Uma caixa de edição para procurar feeds guardados
  anteriormente.
* Uma lista dos feeds guardados;
* Lista de artigos: abre uma caixa de diálogo que apresenta a lista de
  artigos do seu feed actual. Seleccione o artigo que deseja ler e pressione
  Enter ou o botão Abrir página da web do artigo seleccionado para abrir a
  página correspondente no seu navegador. Pressione o botão Sobre o artigo
  para abrir uma caixa de diálogo que mostra o título e o link do artigo
  seleccionado; nesta caixa de diálogo, poderá copiar essa informação para a
  área de transferência.
* Abrir RSS: abre o feed seleccionado na aplicação padrão.
* Novo: abre uma caixa de diálogo com uma caixa de edição para inserir o
  endereço de um novo feed. Se o endereço for válido e o feed puder ser
  guardado, o seu nome, com base no título do feed, aparecerá na parte
  inferior da lista de RSS.
* Renomear: Abre uma caixa de diálogo com uma caixa de edição para renomear
  o feed seleccionado.
* Apagar: abre uma caixa de diálogo para excluir o feed seleccionado, após a
  confirmação.
* Definir por defeito: define o feed seleccionado como padrão, para que os
  seus artigos possam ser acedidos ​​com os comandos do NVDA.
* Abrir pasta que contenha um backup de feeds: Abre uma pasta que pode
  conter um backup de feeds. Isto pode ser útil para explorar e excluir
  feeds que não devam ser importados quando o extra é actualizado.
* Fechar: fecha o diálogo de RSS;

##### Notas: #####

* Se um feed chamado tempFeed for criado, mude-lhe o nome, pois esse
  ficheiro pode ser substituído quando necessário para criar um feed cujo
  nome já existe.
* O feed definido por defeito não pode ser removido. O ficheiro de endereço
  do feed será usado como padrão quando a configuração for reiniciada,
  portanto não pode ser excluído.

#### Copiar pasta de RSS... ####

Abre uma caixa de diálogo para escolher uma pasta onde pode guardar o seu
directório pessoal de RSS . Por padrão, a pasta seleccionada é o diretório
de configuração do NVDA, que criará o diretório de feeds pessoais.

#### Restaurar feeds... ####

Abre uma caixa de diálogo para seleccionar uma pasta que substitui os seus
feeds na pasta personalFeeds. Certifique-se de carregar uma pasta contendo
URLs de feeds.

### Comandos de teclado: ###

* Ctrl+Shift+NVDA+Espaço: anuncia o URL do artigo atual. Ao pressionar duas
  vezes, a página da Web será aberta.
* Ctrl+Shift+NVDA+8: Actualiza o feed seleccionado e anuncia o seu título
  mais recente.
* Ctrl+Shift+NVDA+I: anuncia o título e o link do feed actual. Pressionando
  duas vezes, copiará o título e o link relacionado para a área de
  transferência.
* Ctrl+Shift+NVDA+U: anuncia o título do feed anterior.
* Ctrl+Shift+NVDA+O: anuncia o título do próximo feed.

## Notificações: ##

* Quando o título ou o URL foram copiados.
* Quando não é possível conectar / actualizar um feed, ou o URL não
  corresponde a um feed válido.
* O NVDA mostrará uma mensagem de erro se não for possível fazer backup ou
  restaurar a pasta pessoalFeeds.
* O título da caixa de diálogo da lista de artigos mostra o nome do feed
  selecionado e o número de itens disponíveis.

## Changes for 8.0 ##

* When the add-on is updated, feeds saved in the previous version of the
  add-on will be automatically copied to the new version, unless you prefer
  to import feeds saved in the main configuration folder of NVDA.
* When using the dialog to copy feeds, if the chosen folder is not named
  personalFeeds, a subfolder with this name will be created to prevent the
  deletion of directories containing important data, such as Documents or
  Downloads.

## Alterações para 7.0: ##

* A caixa de diálogo Feeds inclui um botão para abrir uma pasta que pode
  conter um backup de feeds.
* Ao usar a caixa de edição para filtrar os feeds, se não for encontrado
  qualquer resultado, a lista de feeds e outros controlos será desactivada,
  para que o NVDA não diga "desconhecido", na lista vazia.
* Se o diálogo de lista de artigos não puder ser mostrado, por exemplo,
  devido a erros no feed, o NVDA irá gerar um erro, para que o diálogo de
  feeds possa ser usado sem reiniciar o NVDA.

## Alterações para 6.0: ##

* Quando o feed padrão é actualizado e para de funcionar devido a problemas
  do servidor, os artigos anteriores não são excluídos e podem ser lidos,
  pelo uso das teclas correspondentes.
* Corrigida regressão: o feed padrão pode ser atualizado duas vezes,
  novamente.

## Alterações para 5.0: ##

* A caixa de diálogo da lista de artigos foi melhorada.
* Compatível com o NVDA 2018.3 ou posterior (requerido).
* Se necessário, pode fazer o download da [última versão compatível com o
  NVDA 2017.3] [3].

## Alterações para 4.0: ##

* Adicionado um botão para abrir o feed seleccionado a partir da  caixa de
  diálogo de feeds.

## Alterações para 3.0: ##

* As caixas de diálogo para gerir ficheiros de feeds foram removidas. Agora,
  a sua funcionalidade está incluída no diálogo Feeds.
* A apresentação visual dos diálogos foi aprimorada, assemelhando-se à
  aparência dos diálogos mostrados no NVDA.
* O feed definido por defeito é guardado na configuração do NVDA. Portanto,
  é possível definir diferentes feeds padrão nos diferentes perfis de
  configuração.
* Requer NVDA 2016.4.


## Alterações para 2.0: ##

* A ajuda do extra está disponível a partir do gestor de extras.

## Alterações para 1.0: ##

* Versão inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rf

[2]: https://addons.nvda-project.org/files/get.php?file=rf-dev

[3]: https://addons.nvda-project.org/files/get.php?file=rf-o
