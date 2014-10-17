# Czytaj wiadomości / Read Feeds #

* Autorzy: Noelia Ruiz Martínez, Mesar Hameed
* Pobierz [wersja stabilna][2]
* Pobierz [wersja rozwojowa][1]

Ten dodatek dostarcza prosty sposób odczytywania przez NVDA kanałów
informacyjnych w formatach Atom lub RSS.  Kanały nie będą odświeżane
automatycznie.  Mówiąc o kanałach, mamy na myśli kanały w formatach RSS i
ATOM.

## Instalacja i aktualizacja: ##

Jeśli używałeś poprzedniej wersji tego dodatku, i w twoim folderze
konfiguracji NVDA znajdują się katalogi RSS lub personalFeeds , podczas
instalacji wersji 6.0 lub nowszej, pojawi się okno dialogowe z pytaniem, czy
chcesz aktualizować, czy zainstalować.  Wybierz aktualizację, aby
zaktualizować osobiste kanały i kontynuować ich używanie w nowo
zainstalowanej wersji.

## Polecenia: ##

### Menu Czytaj kanały ###

Możesz przejść do podmenu Czytaj kanały z menu NVDA (klawisz NVDA+N);
dostępne są tam następujące opcje:

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

### Skróty klawiszowe: ###

- Ctrl+Shift+NVDA+Space: Podaje adres artykułu. Dwukrotne naciśnięcie
otworzy stronę internetową.  - Ctrl+Shift+NVDA+8: odświeża wybrany kanał i
odczytuje tytuł ostatniego artykułu.  - Ctrl+Shift+NVDA+I: odczytuje tytuł
aktualnego kanału. dwukrotne naciśnięcie skopiuje do schowka tytuł i
powiązany link.  - Ctrl+Shift+NVDA+U: odczytuje adres poprzedniego kanału.
- Ctrl+Shift+NVDA+O: odczytuje adres następnego kanału.

## Powiadomienia: ##

- Gdy tytuł lub adres zostały skopiowane.  - gdy nie można połączyć z siecią
lub odświeżyć kanału, lub adres nie jest związany z prawidłowym kanałem.  -
NVDA wyświetli komunikat błędu, gdy nie było możliwe skopiowanie folderu
personalFeeds.  - Tytuł okna listy artykułów zawiera nazwę wybranego kanału
i liczbę dostępnych elementów.

## Changes for 2.0 ##
*	 Add-on help is available from the Add-ons Manager.

## Zmiany dla wersji 1.0 ##
*	 Pierwsza wersja.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf-dev

[2]: http://addons.nvda-project.org/files/get.php?file=rf
