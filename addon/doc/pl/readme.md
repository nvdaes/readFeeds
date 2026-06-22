# Read Feeds

- Authors: Noelia Ruiz Martínez, Mesar Hameed
- Compatible with NVDA 2023.1.
- Download [stable version][1]
- Download [development version][2]

Ten dodatek umożliwia odczytywanie przez NVDA kanałów informacyjnych w
formatach Atom lub RSS.
Kanały nie będą odświeżane automatycznie.
Mówiąc o
kanałach, mamy na myśli kanały w formatach RSS i ATOM.

## Installation or Update:

If you used a previous version of this addon, and there is an RSS or personalFeeds folder in your personal NVDA configuration folder,
when installing the current version, a dialog will ask if you want to upgrade or install.
Choose update to preserve your saved feeds and to continue using them in the new installed version of readFeeds.

## Polecenia

### Read Feeds menu

Dostęp do okna dialogowego Odczyt kanałów można uzyskać z menu nvda, podmenu
Narzędzia, elementu Kanały.

#### Feeds...

Opens a dialog with the following controls:

- Filtruj Według: Pole edycyjne do wyszukiwania poprzednio zapisanych
  kanałów osobistych.
- A list of the saved feeds.
- Lista artykułow: Otwiera dialog wyświetlający spis artykułów z teraz
  wyświetlanego kanału osobistego. Oznacz artykuł, którego chcesz
  przeczytać, a potem naciśnij przycisk OK, aby otworzyć odnoszącą się
  stronę w przeglądarce. Z tego oka dialogowego, będzie można skopiować tę
  informację do schowka.
- Otwórz kanał: otwiera wybrany kanał w domyślnej aplikacji.
- Nowy: Otwiera okno dialogowe zawierające pole edycyjne, w którym można
  wpisać adres nowego kanału osobistego. Jeżeli adres jest prawidłowy a
  kanał osobisty może być zachowany, nazwa kanału, bazowana na podstawie
  tytułu kanału, będzie wyświetlana na końcu listy.
- Zmień nazwę: Otwiera okno dialogowe zawierające pole edycyjne do zmiany
  nazwy zaznaczonego kanału osobistego.
- Usuń: Otwiera okno dialogowe umożliwiające  usuwanie oznaczonego kanału
  osobistego po potwierdzeniu.
- Ustaw jako domyślny: Ustawia kanał osobisty jako domyślny, aby można było
  się dostać do artykułów za pomocą gestów NVDA.
- Open folder containing a backup of feeds: Opens a folder which may contain a backup of feeds. This can be useful to explore and delete feeds which shouldn't be imported when the add-on is updated.
- Zamknij: Zamyka dialog kanały osobiste.

##### Brak notatek

- If a feed named tempFeed is created, please rename it, as this file could be replaced when needed to create a feed whose name already exists.
- The feed set as the default can't be removed. The addressFile feed will be use as the default when the configuration is reset, so it can't be deleted.

\####Copy feeds folder... ####

Opens a dialog to choose a folder where you can save the personalFeeds directory of your feeds. By default the selected folder is the NVDA's configuration directory, which will create the personalFeeds directory.

#### Restore feeds...

Opens a dialog to select a folder which replaces your feeds in the personalFeeds folder. Make sure you load a folder containing feeds URLs.

### Keyboard commands:

- Ctrl+Szift+NVDA+Spacja: mówi adres artykułu. Jeżeli się naciśnie dwa razy,
  otwiera stronę.
- Ctrl+Szift+NVDA+8: Odświeża oznaczony kanał osobisty i wymawia najnowszy
  teraźniejszy nagłówek.
- Ctrl+Szift+NVDA+I: Wymawia teraźniejszy tytuł kanału osobistego i
  link. Dwukrotne naciśnięcie spowoduje kopiowanie tytułu odnoszącego się
  linku do schowka.
- Ctrl+Szift+NVDA+U: Wymawia poprzedni tytuł kanału osobistego.
- Ctrl+Szift+NVDA+O: Wymawia następujący tytuł kanału osobistego.

## Powiadomienia

- Improved notifications when title or URL are copied.
- When unable to connect/refresh a feed, or the URL does not correspond to a valid feed.
- NVDA will display an error message if it was not possible to backup or restore the personalFeeds folder.
- Dialog Spisu nagłówków artykułów Wyświetla nazwę oznaczonego kanału
  osobistego i ilość dostępnych artykułów.

## Zmiany w wersji 8.0

- Po zaktualizowaniu dodatku kanały zapisane w poprzedniej wersji dodatku
  zostaną automatycznie skopiowane do nowej wersji, chyba że wolisz
  importować kanały zapisane w głównym folderze konfiguracyjnym NVDA.
- Podczas korzystania z okna dialogowego do kopiowania kanałów
  informacyjnych, jeśli wybrany folder nie ma nazwy personalFeeds, zostanie
  utworzony podfolder o tej nazwie, aby zapobiec usunięciu katalogów
  zawierających ważne dane, takie jak Dokumenty lub Pobrane.

## Zmiany w wersji 7.0

- Okno dialogowe Kanały zawiera przycisk do otwierania folderu, który może
  zawierać kopię zapasową kanałów.
- Podczas używania pola edycji do filtrowania kanałów, jeśli nie zostaną
  znalezione żadne wyniki, lista kanałów i innych kontrolek jest wyłączona,
  dzięki czemu NVDA nie zgłasza "nieznanego" na pustej liście.
- Jeśli nie można wyświetlić okna dialogowego listy artykułów, na przykład z
  powodu błędów w kanale, NVDA spowoduje wyświetlenie błędu, dzięki czemu
  okno dialogowe kanałów może być używane bez ponownego uruchamiania NVDA.

## Zmiany w wersji 6.0

- Gdy domyślny kanał informacyjny został zaktualizowany i przestaje działać
  z powodu problemów z serwerem, poprzednie artykuły nie są usuwane i można
  je odczytać za pomocą odpowiednich naciśnięć.
- Naprawiony błąd: Domyślny kanał może być aktualizowany znowu dwa razy.

## Zmiany dla wersji 5.0

- Ulepszone okno dialogowe artykułów.
- Zgodny z NVDA 2018.3 lub nowszą (wymagane).
- If needed, you can download the [last version compatible with NVDA 2017.3][3].

## Zmiany w wersji 4.0

- Dodano przycisk służący do otwierania wybranego kanału z dialogu kanałów
  osobistych.

## Zmiany dla wersji 3.0

- Dialogi do zarządzania plikami kanałami osobistymi został usunięty. Teraz
  tę funkcjonalność można znaleźć w dialogu "Kanaly osobiste".
- Wizualna prezentacja dialogów została ulepszona, aby była zgodna z
  wyświetlanymi dialogami w NVDA.
- Domyślny kanał osobisty jest zachowany w konfiguracji NVDA's. Aczkolwiek,
  można ustawić poszczególne domyślne kanały osobiste w profilach
  konfiguracyjnych.
- Wymaga NVDA 2016.4.

## Zmiany dla wersji 2.0

- Pomoc dodatku jest dostępna w menedżerze dodatków.

## Zmiany dla wersji 1.0

- Pierwsza wersja.

[1]: http://addons.nvda-project.org/files/get.php?file=rf
[2]: http://addons.nvda-project.org/files/get.php?file=rf-dev
[3]: http://addons.nvda-project.org/files/get.php?file=rf-o
