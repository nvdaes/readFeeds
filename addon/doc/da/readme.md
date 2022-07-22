# Læs feeds #

* Forfattere: Noelia Ruiz Martínez, Mesar Hameed
* Download [stable version][1] (compatible with NVDA 2019.3 and beyond)
* Download [development version][2] (compatible with NVDA 2019.3 and beyond)

Dette tilføjelsesprogram giver en nem og ligetil måde at læse nyheader i
atom- eller RSS-format med NVDA. Feeds vil ikke blive opdateret
automatisk. Når vi nedenfor nævner feeds, mener vi både RSS- og atom-feeds.

## Kommandoer ##

### Read Feeds dialog ###

You can access the Read Feeds dialog from the nvda menu, Tools submenu,
Feeds item.

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
* Import feeds from OPML file: Opens a dialog to add new feeds from an OPML
  file.
* Save feeds to OPML file: Opens a dialog to save the feeds available from
  the Feeds dialog in an OPML file.
* Indstillinger: Åbner indstillingerne for tilføjelsen. Indstillingerne kan
  også findes i NVDA-menuen>Opsætning>Indstillinger og ved at vælge
  kategorien "Læs Feeds".
* Luk: Lukker dialogen Nyhedskanaler.

### Notes #####

* Filtrer efter redigeringsfelt kan placeres efter knappen Åbn artikel fra
  NVDA's menu, Indstillinger, Indstillinger, Læs feeds-kategori eller ved at
  trykke på knappen Indstillinger i dialogboksen Feeds.
* This panel has an option to show article dates on the List of articles
  dialog.


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
* NVDA will display an error message if a new feed cannot be created.
* Titlen på dialogen der viser listen over artikler viser navnet på det
  aktuelle feed, samt antallet af artikler til rådighed.

## Changes for 14.0

* Fixed a bug that made impossible to add some feeds.

## Changes for 13.0

* The add-on cannot be used on secure screens.
* Feeds are managed from OPML files.
* Due to changes in the feeds management system, there are changes in the
  configuration file where the default feed is set. Please, use the Feeds
  dialog if you want to set it again.
* Your old text files used in previous versions will be automatically
  imported into the new OPML format when the add-on is started.
* The copy and restore feeds feature has been replaced with the ability to
  import from and save to OPML files.
* Non well-formed feeds can be processed before being added to make them
  compatible with the add-on.
* In the Read Feeds settings panel, a new option allows to show article
  dates on the List of articles dialog.

## Changes for 12.0

* Fixed a bug which made shortcuts for items of NVDA's tools menu don't work
  as expected.

## Changes for 11.0

* Compatible with NVDA 2021.1

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

[1]: https://addons.nvda-project.org/files/get.php?file=rf

[2]: https://addons.nvda-project.org/files/get.php?file=rf-dev

[3]: https://addons.nvda-project.org/files/get.php?file=rf-o
