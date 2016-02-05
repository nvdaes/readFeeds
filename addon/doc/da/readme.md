# Read Feeds #

* Forfattere: Noelia Ruiz Martínez, Mesar Hameed
* Download [stabil version][2]
* download [testversion][1]

Dette tilføjelsesprogram giver en nem og ligetil måde at læse feeds i atom-
eller RSS-format med NVDA. Feeds vil ikke blive opdateret automatisk. Når vi
nedenfor nævner feeds, mener vi både RSS- og atom-feeds.

## Installation eller opdatering: ##

Hvis du har brugt en tidligere version af dette tilføjelsesprogram, og hvis
der er en mappe med navnet RSS eller personalFeeds i mappen med dine
personlige NVDA-indstillinger, vil der, når du installerer version 6.0 eller
senere, komme en dialog, som spørger, om du vil opgradere eller
installere. Vælg opdater for at bevare dine gemte feeds og fortsætte med at
bruge dem i den nyinstallerede version af ReadFeeds.

## Kommandoer: ##

### Menuen Læs feeds ###

Du kan gå ind i undermenuen ReadFeeds fra NVDA-menuen, NVDA+n. Her finder du
følgende muligheder:

- Artikelliste...: Viser listen over artikler fra det aktuelle feed. Vælg
den artikel, du vil læse, og tryk OK for at åbne den i din browser.
- Midlertidig feed-adresse... control + NVDA + shift + enter: Åbner en
dialog, hvor du kan indtaste en ny adresse og vælge et nyt feed. Den
aktuelle adresse vil blive vist i denne dialog.
- Hent feed-adresse fra fil... (NVDA+Ctrl+Enter. Åbner en dialog, hvor du
kan vælge et feed fra en gemt fil, som indeholder en feed-URL.
Gem aktuelle feed-adresse i fil... NVDA+Shift+Enter: Åbner en dialog, hvor
du kan vælge den fil, som den aktuelle feed-adresse skal gemmes i. hvis du
gemmer i den specielle fil med navnet addressFile.txt, vil dette feed blive
brugt som standard-feed.
- Opdater aktuelle feed control+shift+NVDA+8: Feeds bliver ikke automatisk
opdateret, når tilføjelsesprogrammet ReadFeeds startes.
- Sikkerhedskopier mappe med feeds: Åbner en dialog, hvor du kan vælge en
mappe til at gemme oversigten over dine personlige feeds. Som standard er
den valgte mappe NVDAs mappe med indstillinger, så dette vil oprette
oversigten over personlige feeds.
- Gendan feeds...: Åbner en dialog, hvor du kan vælge en mappe med feeds som
skal erstatte mappen med dine personlige feeds. Sørg for at indlæse en
mappe, som indeholder feed-adresser.

Bemærk: Hvis du vil slette en feed-adresse, som du tidligere har gemt, så
bare slet den tilsvarende fil.

### Tastaturkommandoer: ###

- Ctrl+Shift+NVDA+Space: Annoncerer adressen på den aktuele artikel. Tryk to
gange for at åbne web-siden.
- Ctrl+Shift+NVDA+8: Opdaterer det aktuelle feed og annoncerer dets seneste
titel.
- Ctrl+Shift+NVDA+I: Annoncerer aktuelle feed-titel. Tryk to gange for at
kopiere titlen og det sammenhørende link til udklipsholderen.
- Ctrl+Shift+NVDA+U: Annoncerer forrige feed-titel.
- Ctrl+Shift+NVDA+O: Annoncerer næste feed-titel.

## Meddelelser: ##

- Når titlen eller adressen er blevet kopieret.
- Når programmet ikke kan forbinde til eller opdatere et feed, eller hvis
adressen ikke svarer til et gyldigt feed.
- NVDA viser en fejlmeddelelse, hvis det ikke var muligt at
sikkerhedskopiere mappen med personlige feeds.
- Titlen på dialogen med listen over artikler viser navnet på det valgte
feed og antallet af emner til rådighed.

## Ændringer i 2.0 ##
*	 Hjælp til tilføjelsesprogrammet er til rådighed fra styring af
   tilføjelsesprogrammer.

## Ændringer i 1.0 ##
*	 Første version.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf-dev

[2]: http://addons.nvda-project.org/files/get.php?file=rf

