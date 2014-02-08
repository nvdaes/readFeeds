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

*	 Lista artykułów... przedstawia listę artykułów aktualnego kanału. Wybierz
   artykuł, który chcesz przeczytać i naciśnij przycisk OK, aby otworzyć
   powiązaną stronę w przeglądarce internetowej.
*	 Tymczasowy adres kanału... control + NVDA + shift + enter: otwiera okno
   dialogowe pozwalające wpisać adres innego kanału. Aktualny adres zostanie
   wyświetlony w tym oknie.
*	 Wczytaj adres kanału z pliku... NVDA+control+enter: otwiera okno wyboru
   kanału, którego adres jest zapisany w pliku.
*	 Zapisz aktualny adres kanału do pliku... NVDA+shift+enter: otwiera okno
   wyboru pliku, w którym zostanie zapisany aktualny adres kanału. jeśli
   zapiszesz do specjalnego pliku addressFile.txt, adres ten zostanie użyty
   jako domyślny.
*	 Odśwież aktualny kanał: control+shift+NVDA+8: odświeża wybrany
   kanał. Kanały nie są automatycznie aktualizowane po uruchomieniu tego
   dodatku.
*	 Zapisz kopię folderu kanałów... otwiera okno wyboru folderu, w którym
   zostanie zapisany katalog twoich kanałów personalFeeds. Domyślnie,
   wybranym folderem jest folder konfiguracyjny NVDA, gdzie zostanie
   utworzony katalog personalFeeds .
*	 Przywróć kanały... otwiera okno wyboru folderu z kanałami, który zastąpi
   twój katalog personalFeeds. Upewnij się, że wczytujesz folder zawierający
   adresy kanałów.

### Skróty klawiszowe: ###

*	 Ctrl+Shift+NVDA+Space: ogłasza adres aktualnego artykułu. Podwójne
   naciśnięcie otworzy stronę internetową.
*	 Ctrl+Shift+NVDA+8: odświeża aktualny kanał i ogłasza najnowszy tytuł.
*	 Ctrl+Shift+NVDA+I: ogłasza tytuł aktualnego kanału. podwójne naciśnięcie
   skopiuje tytuł i adres do schowka.
*	 Ctrl+Shift+NVDA+U: oznajmia poprzedni tytuł kanału.
*	 Ctrl+Shift+NVDA+O: oznajmia następny tytuł kanału.

## Powiadomienia: ##

*	 Gdy tytuł lub adres zostały skopiowane.
*	 Gdy nie można pobrać lub zaktualizować kanału, albo adres nie wskazuje na
   prawidłowy kanał.
*	 NVDA wyświetli komunikat o błędzie, jeśli nie było możliwe skopiowanie
   katalogu personalFeeds.
*	 Tytuł okna listy artykułów zawiera nazwę wybranego kanału i ilość
   dostępnych elementów.

## Zmiany dla wersji 1.0 ##
*	 Pierwsza wersja.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf-dev

[2]: http://addons.nvda-project.org/files/get.php?file=rf

