# Leitor de fíds #

* Autores: Noelia Ruiz Martínez, Mesar Hameed
* Baixe a [versão estável][2]
* Baixe a [versão de desenvolvimento][1]

Este complemento fornece uma maneira direta de ler fíds em formato Atom ou
RSS usando o NVDA. Os fíds não são atualizados automaticamente.  Ao
mencionarmos fíds abaixo, referimo-nos tanto a fíds RSS como ATOM.

## Instalar ou atualizar: ##

Caso já tenha usado uma versão anterior deste complemento e houver uma pasta
RSS ou personalFeeds na pasta pessoal de opções do NVDA, ao instalar a
versão 6.0 ou superior, um diálogo vai perguntar se você quer atualizar ou
instalar.  Escolha atualizar para preservar os fíds salvos e continuá-los
usando na nova versão instalada do Leitor de Fíds.

## Comandos: ##

### Menu Leitor de Fíds ###

Você pode acessar o submenu do Leitor de Fíds a partir do menu do NVDA,
NVDA+N, onde são disponíveis as opções de menu a seguir:

- Article list...  Presents the article list from your current feed. Select
the article you want to read and press OK button to open the corresponding
page in your browser.  - Temporary feed address... control + NVDA + shift +
enter: Opens a dialog for typing a new URL to select another feed. The
current URL will be shown in this dialog.  - Load feed address from
file... NVDA+control+enter: Opens a dialog to select a feed from a saved
file containing a feed URL.  - Save current feed address to
file... NVDA+shift+enter: opens a dialog for selecting the file where
current feed URL will be saved.  If you save to the special file
addressFile.txt, this particular feed will be used as your default feed.  -
Refresh current feed: control+shift+NVDA+8: Refresh selected feed. The feeds
will not be updated automatically when Read Feeds addon is started.  -
Backup feeds folder...  opens a dialog to choose a folder where you can save
the personalFeeds directory of your feeds. By default the selected folder is
the NVDA's configuration directory, which will create the personalFeeds
directory.  - Restore feeds...  Opens a dialog to select a folder which
replaces your feeds in the personalFeeds folder. Make sure you load a folder
containing feeds URLs.

Note: If you want to delete a previously saved feed URL, just remove the
corresponding file.

### Comandos de teclado: ###

- Ctrl+Shift+NVDA+Espaço: Anuncia a URL do artigo atual. Pressionar duas
vezes abre a página web.  - Ctrl+Shift+NVDA+8: Atualiza o fíd selecionado e
anuncia o título mais recente.  - Ctrl+Shift+NVDA+I: Anuncia o título do fíd
atual. Pressionar duas vezes copia o título e o linque relacionado para a
área de transferência.  - Ctrl+Shift+NVDA+U: Anuncia o título do fíd
anterior.  - Ctrl+Shift+NVDA+O: Anuncia o título do próximo fíd.

## Notificações: ##

Quando o título ou a URL houver sido copiado.  - Quando não é possível
conectar/atualizar um fíd, ou a URL não corresponde a um fíd válido.  - O
NVDA mostrará uma mensagem de erro se não for possível copiar a pasta
personalFeeds.  - O título do diálogo de lista de artigos mostra o nome do
fíd selecionado e o número de itens disponíveis.

## Changes for 2.0 ##
*	 Add-on help is available from the Add-ons Manager.

## Mudanças na 1.0 ##
*	 Versão inicial.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf-dev

[2]: http://addons.nvda-project.org/files/get.php?file=rf

