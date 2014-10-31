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

- Lista de artigos... Exibe a lista de artigos do fíd atual. Selecione o
artigo que deseja ler e pressione o botão OK para abrir no navegador a
página correspondente. - Endereço de fíd temporário... Control + NVDA +
Shift + Enter: Abre um diálogo para digitar uma nova URL por forma a
selecionar outro fíd. A URL atual será mostrada nesse diálogo. - Carregar
endereço de fíd a partir de arquivo... NVDA+Control+Enter: Abre um diálogo
para selecionar um fíd a partir dum arquivo salvo que contenha uma URL de
fíd. - Salvar endereço de fíd atual para arquivo... NVDA+Shift+Enter: Abre
um diálogo para selecionar o arquivo no qual a URL do fíd atual será
salva. Caso salve no arquivo especial addressFile.txt, aquele fíd em
particular será usado como o fíd padrão. - Atualizar fíd atual:
Control+Shift+NVDA+8: Atualiza fíd selecionado. Os fíds não serão
automaticamente atualizados quando se inicia o Leitor de Fíds. - Copiar
pasta de fíds...  Abre um diálogo para escolher uma pasta na qual pode
salvar o diretório de fíds personalFeeds. Por padrão a pasta selecionada é o
diretório de opções do NVDA, que criará o diretório personalFeeds. -
Restaurar fíds...  Abre um diálogo para selecionar uma pasta que substituirá
os fíds da pasta personalFeeds. Certifique-se de carregar uma pasta que
contenha URLs de fíds.

Nota: Caso deseje apagar uma URL de feed anteriormente salva, simplesmente
remova o arquivo correspondente.

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

## Mudanças na 2.0 ##
*	 A ajuda do complemento está disponível no gestor de complementos.

## Mudanças na 1.0 ##
*	 Versão inicial.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf-dev

[2]: http://addons.nvda-project.org/files/get.php?file=rf

