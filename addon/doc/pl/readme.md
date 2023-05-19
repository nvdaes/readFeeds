# Read Feeds #

* Autorzy: Noelia Ruiz Martínez, Mesar Hameed
* Pobierz [stabilna wersja][1] (kompatybilna z NVDA 2019.3 i nowszymi)
* Download [beta version][2] (compatible with NVDA 2019.3 and beyond)

Ten dodatek umożliwia odczytywanie przez NVDA kanałów informacyjnych w
formatach Atom lub RSS.  Kanały nie będą odświeżane automatycznie.  Mówiąc o
kanałach, mamy na myśli kanały w formatach RSS i ATOM.

## Polecenia ##

### Okno dialogowe Czytanie kanałów informacyjnych ###

Dostęp do okna dialogowego Odczyt kanałów można uzyskać z menu nvda, podmenu
Narzędzia, elementu Kanały.

Zawiera następujące kontrolki:

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
* Importowanie plików danych z pliku OPML: Otwiera okno dialogowe
  umożliwiające dodanie nowych źródeł danych z pliku OPML.
* Zapisz źródła danych w pliku OPML: Otwiera okno dialogowe, aby zapisać
  źródła dostępne w oknie dialogowym Źródła danych w pliku OPML.
* Preferencje: Otwiera okno dialogowe ustawień dla readFeeds, dostępne
  również w menu NVDA, opcje, ustawienia, kategoria readFeeds.
* Zamknij: Zamyka dialog kanały osobiste.

### Brak notatek

* Pole edycji Filtruj według można umieścić za przyciskiem Otwórz artykuł z
  menu NVDA, Preferencje, Ustawienia, Kategoria Odczyt kanałów lub
  naciskając przycisk Preferencje w oknie dialogowym Kanały.
* Ten panel ma opcję wyświetlania dat artykułów w oknie dialogowym Lista
  artykułów.


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
* NVDA wyświetli komunikat o błędzie, jeśli nie można utworzyć nowego
  kanału.
* Dialog Spisu nagłówków artykułów Wyświetla nazwę oznaczonego kanału
  osobistego i ilość dostępnych artykułów.

## Changes for 21.0

* Feeds with untitled articles can be presented in the Articles dialog, and
  opened as HTML.

## Changes for 20.0

* universalFeedParser is updated to 5.0.1, adding support for more feeds.

## Zmiany w wersji 14.0

* Naprawiono błąd, który uniemożliwiał dodanie niektórych kanałów.

## Zmiany dla wersji 13.0

* Dodatek nie może być używany na bezpiecznych ekranach.
* Kanały informacyjne są zarządzane z plików OPML.
* Ze względu na zmiany w systemie zarządzania plikami danych, w którym
  ustawiono domyślny plik danych, występują zmiany w pliku
  konfiguracyjnym. Użyj okna dialogowego Kanały, jeśli chcesz ustawić je
  ponownie.
* Stare pliki tekstowe używane w poprzednich wersjach zostaną automatycznie
  zaimportowane do nowego formatu OPML po uruchomieniu dodatku.
* Funkcja kopiowania i przywracania kanałów danych została zastąpiona
  możliwością importowania i zapisywania w plikach OPML.
* Niezbyt dobrze uformowane kanały mogą być przetwarzane przed dodaniem, aby
  były zgodne z dodatkiem.
* W panelu ustawień Odczyt kanałów nowa opcja umożliwia wyświetlanie dat
  artykułów w oknie dialogowym Lista artykułów.

## Zmiany dla wersji 12.0

* Naprawiono błąd, który powodował, że skróty do elementów menu narzędzi
  NVDA nie działały zgodnie z oczekiwaniami.

## Zmiany dla wersji 11.0

* Kompatybilny z NVDA 2021.1

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

## Zmiany dla wersji 5.0 ##

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

[1]: https://www.nvaccess.org/addonStore/legacy?file=readFeeds

[2]: https://www.nvaccess.org/addonStore/legacy?file=readFeeds-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=rf-o
