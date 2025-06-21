# Leitor de Feeds (Read Feeds) #

* Autores: Noelia Ruiz Martínez, Mesar HameedAutores: Noelia Ruiz Martínez,
  Mesar Hameed

Este complemento fornece uma maneira direta de ler feeds —
alimentadores/canais/fluxos/fontes — em formato Atom ou RSS usando o
NVDA. Os feeds não serão atualizados automaticamente. Abaixo, quando
mencionamos feeds, queremos dizer tanto feeds RSS quanto feeds ATOM.

## Comandos ##

### Caixa de diálogo Ler feeds ###

Você pode acessar a caixa de diálogo Ler feeds no menu nvda, submenu
Ferramentas, item Feeds.

Ele contém os seguintes controles:

* Filtrar por: Um campo de edição para procurar feeds anteriormente salvos.
* Uma lista dos feeds salvos, focalizada quando o diálogo é aberto.
* Lista de artigos: Abre um diálogo que apresenta a lista de artigos do seu
  feed atual. Selecione o artigo que deseja ler e pressione Enter ou o botão
  Abrir página web do artigo selecionado para abrir a página correspondente
  no seu navegador. Pressione o botão Sobre o artigo para abrir uma caixa de
  diálogo mostrando o título e o link do artigo selecionado; desta caixa de
  diálogo, você poderá copiar essa informação para a área de transferência.
* Abrir feed: Abre o feed selecionado no aplicativo padrão.
* Abrir feed como HTML: Abre o feed selecionado no navegador web
  padrão. Você poderá mostrar ou ocultar datas de publicação e botões para
  copiar informações sobre artigos para a área de transferência.
* Copiar endereço do feed: abre um diálogo para confirmar se você deseja
  copiar o endereço do feed para a área de transferência.
* Novo: Abre um diálogo com uma caixa de edição para inserir o endereço de
  um novo feed. Se o endereço for válido e o feed puder ser salvo, seu nome,
  com base no título do feed, aparecerá na parte inferior da lista de feeds.
* Renomear: Abre um diálogo com um campo de edição para renomear o feed
  selecionado.
* Excluir: Abre um diálogo para excluir o feed selecionado após confirmação.
* Definir padrão: Define o feed selecionado como padrão, para que seus
  artigos possam ser acessados com os comandos (gestos) do NVDA.
* Importar feeds de um arquivo OPML: Abre uma caixa de diálogo para
  adicionar novos feeds de um arquivo OPML.
* Salvar feeds em arquivo OPML: Abre uma caixa de diálogo para salvar os
  feeds disponíveis na caixa de diálogo Feeds em um arquivo OPML.
* Preferências: Abre o diálogo de configuração para Leitor de Feeds, também
  disponível no menu do NVDA, Preferências, configurações, categoria Leitor
  de Feeds.
* Fechar: Fecha o diálogo Feeds.

### Notas #####

* A caixa de edição Filtrar por pode ser colocada após o botão Abrir artigo
  do menu do NVDA, Preferências, Configurações, categoria Leitor de feeds,
  ou pressionando o botão Preferências do diálogo Feeds.
* Esse painel tem uma opção para mostrar as datas dos artigos na caixa de
  diálogo Lista de artigos.


### Comandos de teclado ###

* Ctrl+Shift+NVDA+Espaço: Anuncia o URL do artigo atual. Pressionar duas
  vezes abrirá a página web.
* Ctrl+Shift+NVDA+8: Atualiza o feed selecionado e anuncia seu título mais
  recente.
* Ctrl+Shift+NVDA+I: Anuncia o título e o link do feed atual. Pressionar
  duas vezes copiará o título e o link relacionado para a área de
  transferência.
* Ctrl+Shift+NVDA+U: Anuncia o título do feed anterior.
* Ctrl+Shift+NVDA+O: Anuncia o título do próximo feed.

## Notificações ##

* Quando o título ou URL foram copiados.
* Quando não é possível conectar/atualizar um feed ou o URL não corresponde
  a um feed válido.
* O NVDA exibirá uma mensagem de erro se não for possível criar um novo
  feed.
* O título do diálogo Lista de artigos mostra o nome do feed selecionado e o
  número de itens disponíveis.

## Changes for 39.0.0

* Improved notifications when title or URL are copied.

## Mudanças na 34.0.0

* Adicionado suporte para feeds rss.cbc.ca.

## Mudanças na 21.0

* Os feeds com artigos sem título podem ser apresentados na caixa de diálogo
  Artigos e abertos como HTML.

## Mudanças na 20.0

* o universalFeedParser foi atualizado para a versão 5.0.1, adicionando
  suporte a mais feeds.

## Changes for 15.0

* Compatible with NVDA 2023.1.

## Mudanças na 14.0

* Correção de um erro que impossibilitava a adição de alguns feeds.

## Mudanças na 13.0

* O add-on não pode ser usado em telas seguras.
* Os feeds são gerenciados a partir de arquivos OPML.
* Devido a alterações no sistema de gerenciamento de feeds, há alterações no
  arquivo de configuração em que o feed padrão é definido. Use a caixa de
  diálogo Feeds se quiser defini-lo novamente.
* Seus arquivos de texto antigos usados em versões anteriores serão
  importados automaticamente para o novo formato OPML quando o complemento
  for iniciado.
* O recurso de cópia e restauração de feeds foi substituído pela capacidade
  de importar e salvar em arquivos OPML.
* Os feeds não bem formados podem ser processados antes de serem adicionados
  para torná-los compatíveis com o complemento.
* No painel de configurações do Read Feeds, uma nova opção permite mostrar
  as datas dos artigos na caixa de diálogo Lista de artigos.

## Mudanças na 12.0

* Correção de um bug que fazia com que os atalhos para itens do menu de
  ferramentas do NVDA não funcionassem como esperado.

## Mudanças na 11.0

* Compatível com o NVDA 2021.1

## Mudanças na 10.0 ##

* Adicionado um botão para abrir o feed selecionado como HTML no navegador
  web padrão.
* Se um novo feed não puder ser criado, isso será notificado num diálogo de
  erro.
* Melhoria da ordem e apresentação de alguns artigos.
* Mais feeds podem ser suportados.
* Quando o diálogo de feeds for aberto, a lista de feeds terá o foco em vez
  da caixa de edição de pesquisa.
* Você pode escolher se a caixa de edição de pesquisa será colocada após a
  lista de feeds, útil para focalizar a lista mesmo quando mudar de outra
  janela sem fechar o diálogo Feeds.
* Adicionado um botão para copiar o endereço do feed para a área de
  transferência no diálogo de feeds.

## Mudanças na 9.0 ##

* Requer NVDA 2019.3 ou posterior.

## Mudanças na 8.0 ##

* Quando o complemento for atualizado, feeds salvos da versão anterior do
  complemento serão automaticamente copiados para a nova versão, a não ser
  que você prefira importar os feeds salvos na pasta principal de
  configurações do NVDA.
* Ao usar o diálogo de copiar feeds, caso a pasta escolhida não seja nomeada
  personalFeeds, será criada uma subpasta com esse nome para prevenir a
  exclusão de diretórios que contenham dados importantes, tais como
  Documentos ou Downloads.

## Mudanças na 7.0 ##

* O diálogo de feeds inclui um botão para abrir uma pasta que pode conter
  uma cópia de segurança — backup — dos feeds.
* Ao usar a caixa de edição para filtrar os feeds, se nenhum resultado for
  encontrado, a lista de feeds e outros controles serão desabilitados, para
  que o NVDA não anuncie "desconhecido" na lista vazia.
* Se o diálogo de lista de Artigos não puder ser mostrado, por exemplo
  devido a erros no feed, o NVDA disparará um erro, de modo que o diálogo de
  feeds possa ser usado sem reiniciar o NVDA.

## Mudanças na 6.0 ##

* Quando o feed padrão é atualizado e para de funcionar devido a problemas
  no servidor, os artigos anteriores não são excluídos e podem ser lidos com
  os pressionamentos de teclas correspondentes.
* Correção de regressão: o feed padrão pode ser atualizado duas vezes
  novamente.

## Mudanças na 5.0 ##

* O diálogo da lista de artigos foi aprimorado.
* Compatível com o NVDA 2018.3 ou posterior (requerido).

## Mudanças na 4.0 ##

* Adicionado um botão para abrir o feed selecionado no diálogo Feeds.

## Mudanças na 3.0 ##

* Os diálogos para gerir arquivos de feeds foram removidos. Agora a
  funcionalidade dos mesmos está inclusa na caixa de diálogo Feeds.
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

