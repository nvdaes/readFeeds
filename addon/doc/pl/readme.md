# Read Feeds / czytaj kanały osobiste #

* Autorzy: Noelia Ruiz Martínez, Mesar Hameed
* Pobierz [Wersja stabilna][1]
* Pobierz [Wersja rozwojowa][2]

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

#### Kanały osobiste... ####

Otwiera dialog z następującymi kontrolkami:

* Filtruj Według: Pole edycyjne do wyszukiwania poprzednio zapisanych
  kanałów osobistych.
* Lista zachowanych kanałów osobistych.
* Lista artykułow: Otwiera dialog wyświetlający spis arytykułów z teraz
  wyświetlanego kanału osobistego. Oznacz artykuł, którego chcesz
  przeczytać, a potem naćiśnij przycisk OK, aby otworzyć odnoszącą się
  stronę w przeglądarce www.
* Nowy: Otwiera okno dialogowe zawierające pole edycyjne, w którym można
  wpisać adres nowego kanału osobistego. Jeżeli adres jest prawidłowy a
  kanał osobisty może być zachowany, nazwa kanału, bazowana na podstawie
  tytułu kanału, będzie wyświetlana na końcu listy.
* Zmień nazwę: Otwiera okno dialogowe zawierające pole edycyjne do zmiany
  nazwy zaznaczonego kanału osobistego.
* Usuń: Otwiera okno dialogowe umożliwiające  usuwanie oznaczonego kanału
  osobistego po potwierdzeniu.
* Ustaw jako domyślny: Ustawia kanał osobisty jako domyślny, aby można było
  się dostać do artykułów za pomocą gestów NVDA.
* Zamknij: Zamyka dialog kanały osobiste.

##### Uwagi #####

* Jeżeli jest stworzony kanał osobisty pod nazwą tempFeed, zmień mu nazwę,
  dla tego że ten plik może być zamieniony kiedy to jest potrzebne dla
  kanału, który już istnieje.
* Kanał ustawiony jako domyślny nie może być usunięty. Kanał osobisty
  addressFile feed będzie użyty jako domyślny, kiedy konfiguracja jest
  zresetowana, i dla tego, on nie może być usunięty.

####Skopiuj katalog z kanałami osobistymi... ####

Otwiera okno dialogowe, w którym można wybrać katalog gdzie można zapisać
katalog personalFeeds directory z waszymi katalogami osobistymi. Domyślny
katalog, to katalog konfiguracyjny NVDA, gdzie będzie stworzony katalog
personalFeeds.

#### Zresetuj kanały osobiste... ####

Otwiera okno dialogowe w którym można wybrać katalog który zamienia twoje
kanały osobiste w katalogu personalFeeds folder. Upewnij się, że wybrałeś
katalog zawierający kanały osobiste.

### Skróty klawiszowe: ###

* Ctrl+Szift+NVDA+Spacja: mówi adres artykułu. Jeżeli się naciśnie dwa razy,
  otwiera stronę.
* Ctrl+Szift+NVDA+8: Odświeża oznaczony kanał osobisty i wymawia najnowszy
  teraźniejszy nagłówek.
* Ctrl+Szift+NVDA+I: Wymawia teraźniejszy tytuł kanału osobistego i
  link. Dwukrotne naciśnięcie spowoduje kopiowanie tytułu odnoszącego się
  linku do schowka.
* Ctrl+Szift+NVDA+U: Wymawia poprzedni tytuł kanału osobistego.
* Ctrl+Szift+NVDA+O: Wymawia następujący tytuł kanału osobistego.

## Powiadomienia: ##

* Kiedy tytuł i adres zostały skopiowane.
* Kiedy jest niemożliwe odświeżanie/łączenie z kanałem osobistym, albo adres
  się nie zgadza z prawdziwym kanałem osobistym.
* NVDA w¥świetli komunikat o błędzie, jeżeli nie jest możliwe zrobienie
  kopii zapasowej, lub przywracanie katalogu personalFeeds.
* Dialog Spisu nagłówków artykułów Wyświetla nazwę oznaczonego kanału
  osobistego i ilość dostępnych artykułów.


## Zmiany dla wersji 3.0 ##

* Dialogi do zarządzania plikami kanałami osobistymi został usunięty. Teraz
  tę funkcjonalność można znaleźć w dialogu "Kanaly osobiste".
* Wizualna prezentacja dialogów została ulepszona, aby była zgodna z
  wyświetlanymi dialogami w NVDA.
* Domyślny kanał osobisty jest zachowany w konfiguracji NVDA's. Aczkolwiek,
  można ustawić poszczególne domyślne kanały osobiste w profilach
  konfiguracyjnych.
* Wymaga NVDA 2016.4.


## Zmiany dla wersji 2.0 ##

* Pomoc dodatku jest dostępna w menedżerze dodatków.

## Zmiany dla wersji 1.0 ##

* Pierwsza wersja.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rf

[2]: https://addons.nvda-project.org/files/get.php?file=rf-dev
