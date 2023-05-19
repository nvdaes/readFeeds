# Læs feeds #

* Forfattere: Noelia Ruiz Martínez, Mesar Hameed
* Download [stabil version][1] (kompatibel med NVDA 2019.3 og nyere)
* Download [beta version][2] (compatible with NVDA 2019.3 and beyond)

Dette tilføjelsesprogram giver en nem og ligetil måde at læse nyheader i
atom- eller RSS-format med NVDA. Feeds vil ikke blive opdateret
automatisk. Når vi nedenfor nævner feeds, mener vi både RSS- og atom-feeds.

## Kommandoer ##

### Dialogboksen Læs feeds ###

Du kan få adgang til undermenuen Læs Feeds fra NVDA-menuen værktøjer.

It contains the following controls:

* Filtrér efter: Et redigeringsfelt til at søge i tidligere gemte feeds.
* En liste over de gemte feeds, der automatisk får fokus, når dialogen
  åbnes.
* Liste over artikler: Åbner en dialog, der viser en liste over artikler fra
  dit nuværende feed. Vælg den artikel, du vil læse, og tryk på Enter eller
  Åbn webside for den valgte artikel for at åbne den tilsvarende side i din
  browser. Tryk på knappen "Om artiklen" for at åbne en dialog med titel og
  link for den valgte artikel; Fra denne dialog kan du kopiere denne
  information til udklipsholderen.
* Åbn feed: Åbner det valgte feed i standardprogrammet.
* Åbn feed som HTML: Åbner det valgte feed i standardwebbrowseren. Du vil
  være i stand til at vise eller skjule udgivelsesdatoer og knapper for at
  kopiere oplysninger om artikler til udklipsholderen.
* Kopier feedadresse: Åbner en dialog for at bekræfte, om du vil kopiere
  feedadressen til udklipsholderen.
* Ny: Åbner en dialogboks med et redigeringsfelt til at indtaste adressen på
  et nyt feed. Hvis adressen er gyldig og feedet kan gemmes, vises dets
  navn, baseret på feedets titel nederst på listen over feeds.
* Omdøb: Åbner en dialogboks med et redigeringsfelt til at omdøbe det valgte
  feed.
* Slet: Åbner en dialogboks for at slette det valgte feed efter bekræftelse.
* Indstil som standard: Indstiller det valgte feed som standard, så dets
  artikler kan tilgås med NVDAs inputbevægelser.
* Importér feeds fra OPML-fil: Åbner en dialogboks, så du kan tilføje nye
  feeds fra en OPML-fil.
* Gem feeds til OPML-fil: Åbner en dialog for at gemme de tilgængelige feeds
  fra feeds-dialogen i en OPML-fil.
* Indstillinger: Åbner indstillingerne for tilføjelsen. Indstillingerne kan
  også findes i NVDA-menuen>Opsætning>Indstillinger og ved at vælge
  kategorien "Læs Feeds".
* Luk: Lukker dialogen Nyhedskanaler.

### Bemærkninger #####

* Filtrer efter redigeringsfelt kan placeres efter knappen Åbn artikel fra
  NVDA's menu, Indstillinger, Indstillinger, Læs feeds-kategori eller ved at
  trykke på knappen Indstillinger i dialogboksen Feeds.
* Dette panel har en mulighed for at vise artikeldatoer i dialogboksen Liste
  over artikler.


### Tastaturkommandoer ###

* CTRL+Skift+NVDA+Mellemrum: Annoncerer URL på den aktuelle artikel. Ved at
  trykke to gange åbnes adressen i din browser.
* CTRL+NVDA+Skift+8: Opdaterer det valgte feed og oplyser den seneste titel.
* CTRL+Skift+NVDA+I: Annoncerer den aktuelle titel på det valgte feed. Ved
  to tryk kopieres titlen og det tilsvarende link til udklipsholderen.
* CTRL+Skift+NVDA+U: Annoncerer titel på det forrige feed.
* CTRL+Skift+NVDA+O: Annoncerer titel på det næste feed.

## Meddelelser ##

* Når titlen eller URL-adressen er blevet kopieret.
* Når det ikke er muligt at forbinde/opdatere et feed, eller den angivne URL
  ikke svarer til et gyldigt feed.
* NVDA vil vise en fejlmeddelelse, hvis et nyt feed ikke kan oprettes.
* Titlen på dialogen der viser listen over artikler viser navnet på det
  aktuelle feed, samt antallet af artikler til rådighed.

## Changes for 21.0

* Feeds with untitled articles can be presented in the Articles dialog, and
  opened as HTML.

## Changes for 20.0

* universalFeedParser is updated to 5.0.1, adding support for more feeds.

## Ændringer for 14.0

* Rettede en fejl, der gjorde det umuligt at tilføje nogle feeds.

## Ændringer i 13,0

* Tilføjelsen kan ikke bruges på sikre skærme.
* Feeds administreres fra OPML-filer.
* På grund af ændringer i feeds-styringssystemet er der ændringer i
  konfigurationsfilen, hvor standardfeedet er indstillet. Brug venligst
  feed-dialogen, hvis du vil indstille den igen.
* Dine gamle tekstfiler, der blev brugt i tidligere versioner, importeres
  automatisk til det nye OPML-format, når tilføjelsen startes.
* Funktionen til kopiering og gendannelse af feeds er blevet erstattet med
  muligheden for at importere fra og gemme til OPML-filer.
* Ikke velformede feeds kan behandles, før de tilføjes, for at gøre dem
  kompatible med tilføjelsen.
* I indstillingspanelet Læs feeds giver en ny mulighed mulighed for at vise
  artikeldatoer i dialogboksen Liste over artikler.

## Ændringer for 12.0

* Rettede en fejl, der gjorde, at genveje til elementer i NVDA's
  værktøjsmenu ikke fungerede som forventet.

## Ændringer for 11.0

* Kompatibel med NVDA 2021.1.

## Ændringer for 10.0 ##

* Tilføjet en knap for at åbne det valgte feed som HTML i
  standardwebbrowseren.
* Hvis et nyt feed ikke kan oprettes, vil du få besked om dette i en dialog.
* Forbedret rækkefølge og præsentation af nogle artikler.
* Potentiale for understøttelse af flere feeds.
* Når feeds-dialogen åbnes, vil listen over feeds være i fokus i stedet for
  søgefeltet.
* Du kan vælge, om søgefeltet skal placeres efter feedslisten, hvilket er
  nyttigt, når du skifter fra et andet vindue uden at lukke dialogen.
* Tilføjet en knap til at kopiere feedadressen til udklipsholderen fra
  feeds-dialogen.

## Ændringer for 9.0 ##

* Kræver NVDA 2019.3 eller nyere.

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

[1]: https://www.nvaccess.org/addonStore/legacy?file=readFeeds

[2]: https://www.nvaccess.org/addonStore/legacy?file=readFeeds-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=rf-o
