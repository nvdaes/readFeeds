# Read Feeds #

* Autorzy: Noelia Ruiz Martínez, Mesar Hameed
* Zgodność z wersjami NVDA: 2019.3 lub nowszą
* Pobierz [Wersja stabilna][1]
* Pobierz [Wersja rozwojowa][2]


Ten dodatek umożliwia odczytywanie przez NVDA kanałów informacyjnych w
formatach Atom lub RSS.  Kanały nie będą odświeżane automatycznie.  Mówiąc o
kanałach, mamy na myśli kanały w formatach RSS i ATOM.

## Instalacja lub aktualizacja ##

Jeśli używałeś poprzedniej wersji tego dodatku i w Twoim folderze
konfiguracji NVDA znajdują się katalogi RSS lub personalFeeds , podczas
instalacji wersji 6.0 lub nowszej, pojawi się okno dialogowe z pytaniem, czy
chcesz aktualizować, czy zainstalować.  Wybierz aktualizację, aby
zaktualizować osobiste kanały i kontynuować ich używanie w nowo
zainstalowanej wersji.

## Polecenia ##

### Menu Czytaj kanały ###

Możesz przejść do podmenu Czytaj kanały z menu NVDA (klawisz NVDA+N);
dostępne są tam następujące opcje:

#### Kanały ####

Otwiera dialog z następującymi kontrolkami:

* Filtruj Według: Pole edycyjne do wyszukiwania poprzednio zapisanych
  kanałów osobistych.
* Lista zapisanych kanałów informacyjnych, zostanie sfokusowana po otwarciu
  okna dialogowego.
* Lista artykułow: Otwiera dialog wyświetlający spis artykułów z teraz
  wyświetlanego kanału osobistego. Oznacz artykuł, którego chcesz
  przeczytać, a potem naciśnij przycisk OK, aby otworzyć odnoszącą się
  stronę w przeglądarce. Z tego oka dialogowego, będzie można skopiować tę
  informację do schowka.
* Otwórz kanał: otwiera wybrany kanał w domyślnej aplikacji.
* Otwórz kanał jako HTML: Otwiera wybrany kanał w domyślnej przeglądarce
  internetowej. Będziesz mógł pokazywać lub ukrywać daty publikacji i
  przyciski do kopiowania informacji o artykułach do schowka.
* Kopiuj adres kanału: Otwiera okno dialogowe z potwierdzeniem, czy chcesz
  skopiować adres kanału do schowka.
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
* Otwórz folder zawierający kopię zapasową kanałów: Otwiera folder, który
  może zawierać kopię zapasową kanałów. Może to być przydatne do
  przeglądania i usuwania kanałów, których nie należy importować po
  zaktualizowaniu dodatku.
* Preferencje: Otwiera okno dialogowe ustawień dla readFeeds, dostępne
  również w menu NVDA, opcje, ustawienia, kategoria readFeeds.
* Zamknij: Zamyka dialog kanały osobiste.

##### Uwagi #####

* Jeżeli jest stworzony kanał osobisty pod nazwą tempFeed, zmień mu nazwę,
  dla tego że ten plik może być zamieniony kiedy to jest potrzebne dla
  kanału, który już istnieje.
* Kanał ustawiony jako domyślny nie może być usunięty. Kanał osobisty
  addressFile feed będzie użyty jako domyślny, kiedy konfiguracja jest
  zresetowana, i dla tego, on nie może być usunięty.
* Pole edycji Filtruj według można umieścić za przyciskiem Otwórz artykuł z
  menu NVDA, Preferencje, Ustawienia, Kategoria Odczyt kanałów lub
  naciskając przycisk Preferencje w oknie dialogowym Kanały.

#### Kopiowanie folderu kanałów informacyjnych ####

Otwiera okno dialogowe, w którym można wybrać katalog gdzie można zapisać
katalog personalFeeds directory z waszymi katalogami osobistymi. Domyślny
katalog, to katalog konfiguracyjny NVDA, gdzie będzie stworzony katalog
personalFeeds.

#### Przywracanie plików danych ####

Otwiera okno dialogowe w którym można wybrać katalog który zamienia twoje
kanały osobiste w katalogu personalFeeds folder. Upewnij się, że wybrałeś
katalog zawierający kanały osobiste.

### Skróty klawiszowe ###

* Ctrl+Szift+NVDA+Spacja: mówi adres artykułu. Jeżeli się naciśnie dwa razy,
  otwiera stronę.
* Ctrl+Szift+NVDA+8: Odświeża oznaczony kanał osobisty i wymawia najnowszy
  teraźniejszy nagłówek.
* Ctrl+Szift+NVDA+I: Wymawia teraźniejszy tytuł kanału osobistego i
  link. Dwukrotne naciśnięcie spowoduje kopiowanie tytułu odnoszącego się
  linku do schowka.
* Ctrl+Szift+NVDA+U: Wymawia poprzedni tytuł kanału osobistego.
* Ctrl+Szift+NVDA+O: Wymawia następujący tytuł kanału osobistego.

## Powiadomienia ##

* Kiedy tytuł i adres zostały skopiowane.
* Kiedy jest niemożliwe odświeżanie/łączenie z kanałem osobistym, albo adres
  się nie zgadza z prawdziwym kanałem osobistym.
* NVDA wyświetli komunikat o błędzie, jeśli nie można było wykonać kopii
  zapasowej lub przywrócić folderu personalFeeds i jeśli nie można utworzyć
  nowego kanału informacyjnego.
* Dialog Spisu nagłówków artykułów Wyświetla nazwę oznaczonego kanału
  osobistego i ilość dostępnych artykułów.

## Changes for 12.0

* Fixed a bug which made shortcuts for items of NVDA's tools menu don't work
  as expected.

## Changes for 11.0

* Compatible with NVDA 2021.1

## Zmiany dla wersji 10.0 ##

* Dodano przycisk do otwierania wybranego kanału informacyjnego jako HTML w
  domyślnej przeglądarce internetowej.
* Jeśli nie można utworzyć nowego pliku danych, zostanie to wyświetlone w
  oknie dialogowym błędu.
* Poprawiono kolejność i prezentację niektórych artykułów.
* Może być obsługiwane więcej kanałów.
* Po otwarciu okna dialogowego kanały informacyjne zostanie wyświetlona
  zamiast pola edycji wyszukiwania.
* Możesz wybrać, czy pole edycji wyszukiwania ma być umieszczone po liście
  kanałów, co jest przydatne do skupienia listy nawet podczas przełączania z
  innego okna bez zamykania okna dialogowego Źródła.
* Dodano przycisk do kopiowania adresu kanału do schowka z okna dialogowego
  kanałów.

## Zmiany w wersji 9.0 ##

* Wymaga NVDA 2019.3 lub nowszą.

## Zmiany w wersji 8.0 ##

* Po zaktualizowaniu dodatku kanały zapisane w poprzedniej wersji dodatku
  zostaną automatycznie skopiowane do nowej wersji, chyba że wolisz
  importować kanały zapisane w głównym folderze konfiguracyjnym NVDA.
* Podczas korzystania z okna dialogowego do kopiowania kanałów
  informacyjnych, jeśli wybrany folder nie ma nazwy personalFeeds, zostanie
  utworzony podfolder o tej nazwie, aby zapobiec usunięciu katalogów
  zawierających ważne dane, takie jak Dokumenty lub Pobrane.

## Zmiany w wersji 7.0 ##

* Okno dialogowe Kanały zawiera przycisk do otwierania folderu, który może
  zawierać kopię zapasową kanałów.
* Podczas używania pola edycji do filtrowania kanałów, jeśli nie zostaną
  znalezione żadne wyniki, lista kanałów i innych kontrolek jest wyłączona,
  dzięki czemu NVDA nie zgłasza "nieznanego" na pustej liście.
* Jeśli nie można wyświetlić okna dialogowego listy artykułów, na przykład z
  powodu błędów w kanale, NVDA spowoduje wyświetlenie błędu, dzięki czemu
  okno dialogowe kanałów może być używane bez ponownego uruchamiania NVDA.

## Zmiany w wersji 6.0 ##

* Gdy domyślny kanał informacyjny został zaktualizowany i przestaje działać
  z powodu problemów z serwerem, poprzednie artykuły nie są usuwane i można
  je odczytać za pomocą odpowiednich naciśnięć.
* Naprawiony błąd: Domyślny kanał może być aktualizowany znowu dwa razy.

## zmiany w wersji 5.0 ##

* Ulepszone okno dialogowe artykułów.
* Zgodny z NVDA 2018.3 lub nowszą (wymagane).
* Jeżeli to potrzebne, można pobrać [ostatnią wersję zgodną z NVDA
  2017.3][3].

## Zmiany w wersji 4.0 ##

* Dodano przycisk służący do otwierania wybranego kanału z dialogu kanałów
  osobistych.

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

[3]: https://addons.nvda-project.org/files/get.php?file=rf-o
