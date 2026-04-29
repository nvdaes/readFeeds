# Leitor de RSS

- Authors: Noelia Ruiz Martínez, Mesar Hameed
- Compatible with NVDA 2021.1
- Download [stable version][1]
- Download [development version][2]

Este extra fornece uma maneira directa de ler feeds em formatos Atom ou RSS
usando o NVDA.
Os feeds não serão actualizados automaticamente.
quando
falamos de feeds, queremos dizer feeds RSS e ATOM.

## Installation or Update:

If you used a previous version of this addon, and there is an RSS or personalFeeds folder in your personal NVDA configuration folder,
when installing the current version, a dialog will ask if you want to upgrade or install.
Choose update to preserve your saved feeds and to continue using them in the new installed version of readFeeds.

## Comandos:

### Read Feeds dialog

You can access the Read Feeds dialog from the nvda menu, Tools submenu,
Feeds item.

#### Feeds...

Opens a dialog with the following controls:

- Filtrar por: Uma caixa de edição para procurar feeds guardados
  anteriormente.
- A list of the saved feeds.
- Lista de artigos: abre uma caixa de diálogo que apresenta a lista de
  artigos do seu feed actual. Seleccione o artigo que deseja ler e pressione
  Enter ou o botão Abrir página da web do artigo seleccionado para abrir a
  página correspondente no seu navegador. Pressione o botão Sobre o artigo
  para abrir uma caixa de diálogo que mostra o título e o link do artigo
  seleccionado; nesta caixa de diálogo, poderá copiar essa informação para a
  área de transferência.
- Abrir RSS: abre o feed seleccionado na aplicação padrão.
- Novo: abre uma caixa de diálogo com uma caixa de edição para inserir o
  endereço de um novo feed. Se o endereço for válido e o feed puder ser
  guardado, o seu nome, com base no título do feed, aparecerá na parte
  inferior da lista de RSS.
- Renomear: Abre uma caixa de diálogo com uma caixa de edição para renomear
  o feed seleccionado.
- Apagar: abre uma caixa de diálogo para excluir o feed seleccionado, após a
  confirmação.
- Definir por defeito: define o feed seleccionado como padrão, para que os
  seus artigos possam ser acedidos ​​com os comandos do NVDA.
- Open folder containing a backup of feeds: Opens a folder which may contain a backup of feeds. This can be useful to explore and delete feeds which shouldn't be imported when the add-on is updated.
- Fechar: fecha o diálogo de RSS;

##### Notes

- If a feed named tempFeed is created, please rename it, as this file could be replaced when needed to create a feed whose name already exists.
- The feed set as the default can't be removed. The addressFile feed will be use as the default when the configuration is reset, so it can't be deleted.

\####Copy feeds folder... ####

Opens a dialog to choose a folder where you can save the personalFeeds directory of your feeds. By default the selected folder is the NVDA's configuration directory, which will create the personalFeeds directory.

#### Restore feeds...

Opens a dialog to select a folder which replaces your feeds in the personalFeeds folder. Make sure you load a folder containing feeds URLs.

### Comandos de teclado:

- Ctrl+Shift+NVDA+Espaço: anuncia o URL do artigo atual. Ao pressionar duas
  vezes, a página da Web será aberta.
- Ctrl+Shift+NVDA+8: Actualiza o feed seleccionado e anuncia o seu título
  mais recente.
- Ctrl+Shift+NVDA+I: anuncia o título e o link do feed actual. Pressionando
  duas vezes, copiará o título e o link relacionado para a área de
  transferência.
- Ctrl+Shift+NVDA+U: anuncia o título do feed anterior.
- Ctrl+Shift+NVDA+O: anuncia o título do próximo feed.

## Notificações

- Quando o título ou o URL foram copiados.
- Quando não é possível conectar / actualizar um feed, ou o URL não
  corresponde a um feed válido.
- NVDA will display an error message if a new feed cannot be created.
- O título da caixa de diálogo da lista de artigos mostra o nome do feed
  selecionado e o número de itens disponíveis.

## Alterações para 8.0:

- Quando o extra é actualizado, os feeds guardados na versão anterior do
  extra serão automaticamente copiados para a nova versão, a menos que
  prefira que os feeds sejam guardados na pasta de configuração principal do
  NVDA.
- Ao usar o diálogo para copiar feeds, se a pasta escolhida não tiver o nome
  personalFeeds, uma subpasta com este nome será criada para evitar a
  exclusão de directórios que contenham dados importantes, tais como
  documentos ou downloads.

## Alterações para 7.0:

- A caixa de diálogo Feeds inclui um botão para abrir uma pasta que pode
  conter um backup de feeds.
- Ao usar a caixa de edição para filtrar os feeds, se não for encontrado
  qualquer resultado, a lista de feeds e outros controlos será desactivada,
  para que o NVDA não diga "desconhecido", na lista vazia.
- Se o diálogo de lista de artigos não puder ser mostrado, por exemplo,
  devido a erros no feed, o NVDA irá gerar um erro, para que o diálogo de
  feeds possa ser usado sem reiniciar o NVDA.

## Alterações para 6.0:

- Quando o feed padrão é actualizado e para de funcionar devido a problemas
  do servidor, os artigos anteriores não são excluídos e podem ser lidos,
  pelo uso das teclas correspondentes.
- Corrigida regressão: o feed padrão pode ser atualizado duas vezes,
  novamente.

## Alterações para 5.0:

- A caixa de diálogo da lista de artigos foi melhorada.
- Compatível com o NVDA 2018.3 ou posterior (requerido).
- If needed, you can download the [last version compatible with NVDA 2017.3][3].

## Alterações para 4.0:

- Adicionado um botão para abrir o feed seleccionado a partir da  caixa de
  diálogo de feeds.

## Alterações para 3.0:

- As caixas de diálogo para gerir ficheiros de feeds foram removidas. Agora,
  a sua funcionalidade está incluída no diálogo Feeds.
- A apresentação visual dos diálogos foi aprimorada, assemelhando-se à
  aparência dos diálogos mostrados no NVDA.
- O feed definido por defeito é guardado na configuração do NVDA. Portanto,
  é possível definir diferentes feeds padrão nos diferentes perfis de
  configuração.
- Requer NVDA 2016.4.

## Alterações para 2.0:

- A ajuda do extra está disponível a partir do gestor de extras.

## Alterações para 1.0:

- Versão inicial.

[1]: http://addons.nvda-project.org/files/get.php?file=rf
[2]: http://addons.nvda-project.org/files/get.php?file=rf-dev
[3]: http://addons.nvda-project.org/files/get.php?file=rf-o
