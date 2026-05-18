# Leitor de Feeds (Read Feeds)

- Autores: Noelia Ruiz Martínez, Mesar HameedAutores: Noelia Ruiz Martínez,
  Mesar Hameed
- Compatible with NVDA 2023.1.
- Download [stable version][1]
- Download [development version][2]

Este complemento fornece uma maneira direta de ler feeds —
alimentadores/canais/fluxos/fontes — em formato Atom ou RSS usando o
NVDA.
Os feeds não serão atualizados automaticamente.
Abaixo, quando
mencionamos feeds, queremos dizer tanto feeds RSS quanto feeds ATOM.

## Installation or Update:

If you used a previous version of this addon, and there is an RSS or personalFeeds folder in your personal NVDA configuration folder,
when installing the current version, a dialog will ask if you want to upgrade or install.
Choose update to preserve your saved feeds and to continue using them in the new installed version of readFeeds.

## Comandos

### Read Feeds menu

Você pode acessar a caixa de diálogo Ler feeds no menu nvda, submenu
Ferramentas, item Feeds.

#### Feeds...

Opens a dialog with the following controls:

- Filtrar por: Um campo de edição para procurar feeds anteriormente salvos.
- A list of the saved feeds.
- Lista de artigos: Abre um diálogo que apresenta a lista de artigos do seu
  feed atual. Selecione o artigo que deseja ler e pressione Enter ou o botão
  Abrir página web do artigo selecionado para abrir a página correspondente
  no seu navegador. Pressione o botão Sobre o artigo para abrir uma caixa de
  diálogo mostrando o título e o link do artigo selecionado; desta caixa de
  diálogo, você poderá copiar essa informação para a área de transferência.
- Abrir feed: Abre o feed selecionado no aplicativo padrão.
- Novo: Abre um diálogo com uma caixa de edição para inserir o endereço de
  um novo feed. Se o endereço for válido e o feed puder ser salvo, seu nome,
  com base no título do feed, aparecerá na parte inferior da lista de feeds.
- Renomear: Abre um diálogo com um campo de edição para renomear o feed
  selecionado.
- Excluir: Abre um diálogo para excluir o feed selecionado após confirmação.
- Definir padrão: Define o feed selecionado como padrão, para que seus
  artigos possam ser acessados com os comandos (gestos) do NVDA.
- Open folder containing a backup of feeds: Opens a folder which may contain a backup of feeds. This can be useful to explore and delete feeds which shouldn't be imported when the add-on is updated.
- Fechar: Fecha o diálogo Feeds.

##### Notas

- If a feed named tempFeed is created, please rename it, as this file could be replaced when needed to create a feed whose name already exists.
- The feed set as the default can't be removed. The addressFile feed will be use as the default when the configuration is reset, so it can't be deleted.

\####Copy feeds folder... ####

Opens a dialog to choose a folder where you can save the personalFeeds directory of your feeds. By default the selected folder is the NVDA's configuration directory, which will create the personalFeeds directory.

#### Restore feeds...

Opens a dialog to select a folder which replaces your feeds in the personalFeeds folder. Make sure you load a folder containing feeds URLs.

### Comandos de teclado

- Ctrl+Shift+NVDA+Espaço: Anuncia o URL do artigo atual. Pressionar duas
  vezes abrirá a página web.
- Ctrl+Shift+NVDA+8: Atualiza o feed selecionado e anuncia seu título mais
  recente.
- Ctrl+Shift+NVDA+I: Anuncia o título e o link do feed atual. Pressionar
  duas vezes copiará o título e o link relacionado para a área de
  transferência.
- Ctrl+Shift+NVDA+U: Anuncia o título do feed anterior.
- Ctrl+Shift+NVDA+O: Anuncia o título do próximo feed.

## Notificações

- Quando o título ou URL foram copiados.
- Quando não é possível conectar/atualizar um feed ou o URL não corresponde
  a um feed válido.
- O NVDA exibirá uma mensagem de erro se não for possível criar um novo
  feed.
- O título do diálogo Lista de artigos mostra o nome do feed selecionado e o
  número de itens disponíveis.

## Mudanças na 8.0

- Quando o complemento for atualizado, feeds salvos da versão anterior do
  complemento serão automaticamente copiados para a nova versão, a não ser
  que você prefira importar os feeds salvos na pasta principal de
  configurações do NVDA.
- Ao usar o diálogo de copiar feeds, caso a pasta escolhida não seja nomeada
  personalFeeds, será criada uma subpasta com esse nome para prevenir a
  exclusão de diretórios que contenham dados importantes, tais como
  Documentos ou Downloads.

## Mudanças na 7.0

- O diálogo de feeds inclui um botão para abrir uma pasta que pode conter
  uma cópia de segurança — backup — dos feeds.
- Ao usar a caixa de edição para filtrar os feeds, se nenhum resultado for
  encontrado, a lista de feeds e outros controles serão desabilitados, para
  que o NVDA não anuncie "desconhecido" na lista vazia.
- Se o diálogo de lista de Artigos não puder ser mostrado, por exemplo
  devido a erros no feed, o NVDA disparará um erro, de modo que o diálogo de
  feeds possa ser usado sem reiniciar o NVDA.

## Mudanças na 6.0

- Quando o feed padrão é atualizado e para de funcionar devido a problemas
  no servidor, os artigos anteriores não são excluídos e podem ser lidos com
  os pressionamentos de teclas correspondentes.
- Correção de regressão: o feed padrão pode ser atualizado duas vezes
  novamente.

## Mudanças na 5.0

- O diálogo da lista de artigos foi aprimorado.
- Compatível com o NVDA 2018.3 ou posterior (requerido).
- If needed, you can download the [last version compatible with NVDA 2017.3][3].

## Mudanças na 4.0

- Adicionado um botão para abrir o feed selecionado no diálogo Feeds.

## Mudanças na 3.0

- Os diálogos para gerir arquivos de feeds foram removidos. Agora a
  funcionalidade dos mesmos está inclusa na caixa de diálogo Feeds.
- A apresentação visual dos diálogos foi aprimorada, aderindo à aparência
  dos diálogos exibidos pelo NVDA.
- O feed padrão é salvo nas configurações do NVDA. Assim, é possível
  especificar diferentes feeds padrão em perfis de configurações.
- Requer NVDA 2016.4.

## Mudanças na 2.0

- A ajuda do complemento está disponível no gestor de complementos.

## Mudanças na 1.0

- Versão inicial.

[1]: http://addons.nvda-project.org/files/get.php?file=rf
[2]: http://addons.nvda-project.org/files/get.php?file=rf-dev
[3]: http://addons.nvda-project.org/files/get.php?file=rf-o
