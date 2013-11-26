# Czytaj wiadomości / Read Feeds #

* Autorzy: Noelia Ruiz Martínez, Mesar Hameed
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

- Lista artykułów...  prezentuje listę artykułów aktualnego kanału. Wybierz
artykół, który chcesz czytać i naciśnij OK, aby otworzyć powiązaną stronę w
przeglądarce internetowej.  - Tymczasowy adres kanału... control + NVDA +
shift + enter: otwiera okno dialogowe wpisywania nowego adresu, by wybrać
inny kanał. Obecny adres będzie wyświetlony w tym oknie.  - Wczytaj adres
kanału z pliku... NVDA+control+enter: pozwala wybrać adres kanału zapisany w
pliku.  - Zapisz adres aktualnego kanału w pliku... NVDA+shift+enter:
otwiera okno wyboru pliku, w którym zostanie zapisany adres aktualnego
kanału.  Jeśli zapiszesz pod specjalną nazwą addressFile.txt, ten konkretny
kanał będzie używany jako kanał domyślny.  - Odśwież aktualny kanał:
control+shift+NVDA+8: Odświeża wybrany kanał. Kanały nie będą aktualizowane
automatycznie po starcie dodatku.  - Kopiuj folder kanałów...  otwiera okno
wyboru miejsca, w którym zostanie zapisany folder personalFeeds. Domyślnie,
wybranym folderem jest folder konfiguracyjny NVDA, co spowoduje utworzenie
katalogu personalFeeds.  - Przywróć kanały...  otwiera okno wyboru folderu
który zastąpi kanały w katalogu personalFeeds. Upewnij się, że wczytujesz
folder zawierający adresy kanałów.

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

## Zmiany dla wersji 1.0 ##
*	 Pierwsza wersja.

[[!tag dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf-dev

[2]: http://addons.nvda-project.org/files/get.php?file=rf

