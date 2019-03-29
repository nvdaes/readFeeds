# Read Feeds #

* Forfattere: Noelia Ruiz Martínez, Mesar Hameed
* NVDA-kompatibilitet: 2018.3 til 2019.1
* Download [stabil version][1]
* download [udviklingsversion][2]

Dette tilføjelsesprogram giver en nem og ligetil måde at læse nyheader i
atom- eller RSS-format med NVDA. Nyhedskanaler vil ikke blive opdateret
automatisk. Når vi nedenfor nævner nyhedskanaler, mener vi både RSS- og
atom-kanaler.

## Installation eller opdatering: ##

Hvis du har brugt en tidligere version af dette tilføjelsesprogram, og hvis
der er en mappe med navnet RSS eller personalFeeds i mappen med dine
personlige NVDA-indstillinger, vil der, når du installerer den aktuelle
version, komme en dialog, som spørger, om du vil opgradere eller
installere. Vælg opdater for at bevare dine gemte nyhedskanaler og fortsætte
med at bruge dem i den nyinstallerede version af ReadFeeds.

## Kommandoer: ##

### Menuen Læs feeds ###

Du kan få adgang til undermenuen Read Feeds fra NVDA-menuen værktøjer, hvor
de følgende menupunkter er tilgængelige:

#### Nyhedskanaler... ####

Åbner en dialogboks med følgende kontrolelementer:

* Filtrér efter: Et redigeringsfelt til at søge i tidligere gemte
  nyhedskanaler.
* En liste over de gemte nyhedskanaler.
* Liste over artikler: Åbner en dialog, der præsenterer artikellisten fra
  din nuværende kanal. Vælg den artikel, du vil læse, og tryk på Enter eller
  Åbn webside for den valgte artikelknap for at åbne den tilsvarende side i
  din browser. Tryk på Om artiklen knap for at åbne en dialog med titel og
  link for den valgte artikel; Fra denne dialog kan du kopiere denne
  information til udklipsholderen.
* Åbn nyhedskanal: Åbner den markerede kanal i standardprogrammet.
* Ny: Åbner en dialogboks med et redigeringsfelt til at indtaste adressen på
  en ny nyhedskanal. Hvis adressen er gyldig og kanalen kan gemmes, vises
  dens navn, baseret på nyhedskanalens titel nederst på listen over kanaler.
* Omdøb: Åbner en dialogboks med et redigeringsfelt til at omdøbe den valgte
  nyhedskanal.
* Slet: Åbner en dialogboks for at slette den valgte kanal efter
  bekræftelse.
* Sæt som standard: Indstiller den valgte nyhedskanal som standard, så dens
  artikler kan tilgås med NVDAs inputbevægelser.
* Open folder containing a backup of feeds: Opens a folder which may contain
  a backup of feeds. This can be useful to explore and delete feeds which
  shouldn't be imported when the add-on is updated.
* Luk: Lukker dialogen Nyhedskanaler.

##### Noter #####

* Hvis et nyhedskanal ved navn tempFeed er oprettet, skal du omdøbe denne
  kanal, eftersom denne fil kunne erstattes, når det er nødvendigt at
  oprette en kanal med et navn der allerede eksisterer.
* Kanalen der er angivet som standard kan ikke fjernes. AddressFile-kanalen
  vil blive brugt som standard, når konfigurationen er nulstillet. Den kan
  ikke fjernes.

####Mappe til kopiering af nyhedskanaler... ####

Åbner en dialogboks for at vælge en mappe, hvor du kan gemme mappen
personalFeeds der indeholder dine nyhedskanaler. Den valgte mappe er som
standard NVDAs konfigurationsmappen. Tilføjelsespakken vil oprette mappen
personalFeeds.

#### Gendan kanaler ####

Åbner en dialogboks for at vælge en mappe, som erstatter dine nyhedskanaler
i mappen personalFeeds. Sørg for, at du indlæser en mappe der indeholder
URL-adresser på nyhedskanaler.

### Tastaturkommandoer: ###

* CTRL+Skift+NVDA+Mellemrum: Annoncerer URL på den aktuelle artikel. Ved at
  trykke to gange åbnes adressen i din browser.
* CTRL+NVDA+Skift+8: Opdaterer den valgte nyhedskanal og oplyser den seneste
  titel.
* CTRL+Skift+NVDA+I: Annoncerer den aktuelle titel på den valgte
  nyhedskanal. Ved to tryk kopieres titlen og det tilsvarende link til
  udklipsholderen.
* CTRL+Skift+NVDA+U: Annoncerer titel på den forrige nyhedskanal.
* CTRL+Skift+NVDA+O: Annoncerer titel på den næste nyhedskanal.

## Meddelelser: ##

* Når titlen eller URL-adressen er blevet kopieret.
* Når det ikke er muligt at forbinde/opdatere en kanal, eller den angivne
  URL ikke svarer til en gyldig nyhedskanal.
* NVDA vil vise en fejlmeddelelse, hvis det ikke var muligt at
  sikkerhedskopiere eller gendanne mappen personalFeeds.
* Titlen på dialogen der viser listen over artikler viser navnet på den
  aktuelle kanal, samt antallet af artikler til rådighed.

## Changes for 7.0 ##

* The Feeds dialog includes a button to open a folder which may contain a
  backup of feeds.
* When using the edit box to filter feeds, if no results are found, the list
  of feeds and other controls are disabled, so that NVDA doesn't report
  "unknown" in the empty list.
* If the list of articles dialog can't be shown, for example due to errors
  in the feed, NVDA will raise an error, so that the feeds dialog can be
  used without restarting NVDA.

## Ændringer i 6.0 ##

* Når standardkanalen er opdateret, og det ophører med at fungere på grund
  af serverproblemer, fjernes de tidligere artikler ikke og kan læses med de
  tilsvarende tastetryk.
* Rettede regression: Standardkanalen kan opdateres to gange igen.

## Ændringer i 5.0 ##

* Dialogen med listen over artikler er blevet forbedret.
* Kompatibel med NVDA 2018.3 eller nyere (påkrævet).
* Hvis nødvendigt, kan du hente [den sidste version kompatibel med NVDA
  2017.3][3].

## Ændringer i4.0  ##

* Tilføjet en knap for at åbne den valgte nyhedskanal fra dialogen Kanaler.

## Ændringer i 3.0 ##

* Dialoger til at administrere kanalernes filer er blevet fjernet. Nu er
  deres funktionalitet medtaget i dialogen Kanaler.
* Dialogens visuelle præsentation er blevet forbedret og overholder
  udseendet af de dialoger, der vises i NVDA.
* Standardkanalen er gemt i NVDA-konfigurationen. Derfor er det muligt at
  indstille forskellige standardkanaler i konfigurationsprofilerne.
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
