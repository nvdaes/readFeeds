# Læs feeds #

* Forfattere: Noelia Ruiz Martínez, Mesar Hameed
* NVDA-kompatibilitet: 2018.3 til 2019.2
* Download [stabil version][1]
* download [udviklingsversion][2]

Dette tilføjelsesprogram giver en nem og ligetil måde at læse nyheader i
atom- eller RSS-format med NVDA. Feeds vil ikke blive opdateret
automatisk. Når vi nedenfor nævner feeds, mener vi både RSS- og atom-feeds.

## Installation eller opdatering: ##

Hvis du har brugt en tidligere version af dette tilføjelsesprogram, og hvis
der er en mappe med navnet RSS eller personalFeeds i mappen med dine
personlige NVDA-indstillinger, vil der, når du installerer den aktuelle
version fremkomme en dialog, som spørger, om du vil opgradere eller
installere. Vælg opdater for at bevare dine gemte feeds og fortsætte med at
bruge dem i den nyinstallerede version af Læs Feeds.

## Kommandoer: ##

### Menuen Læs feeds ###

Du kan få adgang til undermenuen Læs Feeds fra NVDA-menuen værktøjer, hvor
de følgende menupunkter er tilgængelige:

#### Feeds... ####

Åbner en dialogboks med følgende kontrolelementer:

* Filtrér efter: Et redigeringsfelt til at søge i tidligere gemte feeds.
* En liste over de gemte feeds.
* Liste over artikler: Åbner en dialog, der viser en liste over artikler fra
  dit nuværende feed. Vælg den artikel, du vil læse, og tryk på Enter eller
  Åbn webside for den valgte artikel for at åbne den tilsvarende side i din
  browser. Tryk på knappen "Om artiklen" for at åbne en dialog med titel og
  link for den valgte artikel; Fra denne dialog kan du kopiere denne
  information til udklipsholderen.
* Åbn feed: Åbner det valgte feed i standardprogrammet.
* Ny: Åbner en dialogboks med et redigeringsfelt til at indtaste adressen på
  et nyt feed. Hvis adressen er gyldig og feedet kan gemmes, vises dets
  navn, baseret på feedets titel nederst på listen over feeds.
* Omdøb: Åbner en dialogboks med et redigeringsfelt til at omdøbe det valgte
  feed.
* Slet: Åbner en dialogboks for at slette det valgte feed efter bekræftelse.
* Indstil som standard: Indstiller det valgte feed som standard, så dets
  artikler kan tilgås med NVDAs inputbevægelser.
* Åbn mappen med sikkerhedskopierne for dine feeds: Åbner en mappe, der
  indeholder sikkerhedskopier af dine feeds. Dette kan være nyttigt, hvis du
  evt. vil slette feeds der ikke skal importeres, når tilføjelsen opdateres.
* Luk: Lukker dialogen Nyhedskanaler.

##### Bemærkninger #####

* Hvis et feed ved navn tempFeed er oprettet, skal du omdøbe dette feed,
  eftersom denne fil kunne erstattes, når det er nødvendigt at oprette et
  feed med et navn der allerede eksisterer.
* Det feed der er angivet som standard kan ikke fjernes. AddressFile-feedet
  vil blive brugt som standard, når konfigurationen er nulstillet. Den kan
  ikke fjernes.

####Mappe til kopiering af feeds... ####

Åbner en dialogboks for at vælge en mappe, hvor du kan gemme mappen
personalFeeds der indeholder dine feeds. Den valgte mappe er som standard
NVDAs konfigurationsmappe. Tilføjelsespakken vil oprette mappen
personalFeeds.

#### Gendan feeds... ####

Åbner en dialogboks for at vælge en mappe, som erstatter dine feeds i mappen
personalFeeds. Sørg for, at du indlæser en mappe der indeholder URL-adresser
på feeds.

### Tastaturkommandoer: ###

* CTRL+Skift+NVDA+Mellemrum: Annoncerer URL på den aktuelle artikel. Ved at
  trykke to gange åbnes adressen i din browser.
* CTRL+NVDA+Skift+8: Opdaterer det valgte feed og oplyser den seneste titel.
* CTRL+Skift+NVDA+I: Annoncerer den aktuelle titel på det valgte feed. Ved
  to tryk kopieres titlen og det tilsvarende link til udklipsholderen.
* CTRL+Skift+NVDA+U: Annoncerer titel på det forrige feed.
* CTRL+Skift+NVDA+O: Annoncerer titel på det næste feed.

## Meddelelser: ##

* Når titlen eller URL-adressen er blevet kopieret.
* Når det ikke er muligt at forbinde/opdatere et feed, eller den angivne URL
  ikke svarer til et gyldigt feed.
* NVDA vil vise en fejlmeddelelse, hvis det ikke var muligt at
  sikkerhedskopiere eller gendanne mappen personalFeeds.
* Titlen på dialogen der viser listen over artikler viser navnet på det
  aktuelle feed, samt antallet af artikler til rådighed.

## Ændringer i 8.0 ##

* Når tilføjelsesprogrammet opdateres, bliver feeds, der er gemt i den
  tidligere version af tilføjelsesprogrammet automatisk kopieret til den nye
  version, medmindre du foretrækker at importere feeds, der er gemt i den
  primære konfigurations mappe i NVDA.
* Når du bruger dialogen til at kopiere feeds, hvis den valgte mappe ikke er
  navngivet personalFeeds, vil en undermappe med dette navn blive oprettet
  for at forhindre sletning af mapper, der indeholder vigtige data, såsom
  dokumenter eller overførsler.

## Ændringer i7.0 ##

* Dialogboksen "Feeds" indeholder en knap for at åbne en mappe, der
  indeholder en sikkerhedskopi af feeds.
* Når du bruger redigeringsboksen til at filtrere feeds, og hvis der ikke
  findes nogen resultater, er listen over feeds og andre kontroller
  deaktiveret, så NVDA ikke rapporterer "ukendt" i den tomme liste.
* Hvis dialogen "Liste over artikler" ikke kan vises, for eksempel på grund
  af fejl med feedet, vil NVDA fejle, så dialogen kan bruges uden at
  genstarte NVDA.

## Ændringer i 6.0 ##

* Når standardfeedet er opdateret, og det ophører med at fungere på grund af
  serverproblemer, fjernes de tidligere artikler ikke og kan læses med de
  tilsvarende tastetryk.
* Rettede regression: Standardfeedet kan opdateres to gange igen.

## Ændringer i 5.0 ##

* Dialogen med listen over artikler er blevet forbedret.
* Kompatibel med NVDA 2018.3 eller nyere (påkrævet).
* Hvis nødvendigt, kan du hente [den sidste version kompatibel med NVDA
  2017.3][3].

## Ændringer i4.0  ##

* Tilføjet en knap for at åbne det valgte feed fra dialogen "Feeds".

## Ændringer i 3.0 ##

* Dialoger til at administrere filer til feeds er blevet fjernet. Nu er
  deres funktionalitet medtaget i dialogen "Feeds".
* Dialogens visuelle præsentation er blevet forbedret og overholder
  udseendet af de dialoger, der vises i NVDA.
* Standardfeed er gemt i NVDA-konfigurationen. Derfor er det muligt at
  indstille forskellige standardfeeds i konfigurationsprofilerne.
* Kræver NVDA 2016.4.


## Ændringer i 2.0 ##

* Hjælp til tilføjelsesprogrammet er til rådighed fra styring af
  tilføjelsesprogrammer.

## Ændringer i 1.0 ##

* Første version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rf

[2]: https://addons.nvda-project.org/files/get.php?file=rf-dev

[3]: https://addons.nvda-project.org/files/get.php?file=rf-o
