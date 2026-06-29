# Read Feeds

- Authors: Noelia Ruiz Martínez, Mesar Hameed
- Kompatibel mit NVDA 2021.1
- Download [stable version][1]
- Download [development version][2]

Diese Erweiterung bietet eine einfache Möglichkeit, RSS-Feeds in den
Formaten Atom oder RSS mit NVDA zu lesen.
Die Feeds werden nicht automatisch
aktualisiert.
Wenn wir weiter unten  von Feeds sprechen, dann meinen wir
sowohl RSS- als auch  ATOM-Feeds.

## Installation or Update:

If you used a previous version of this addon, and there is an RSS or personalFeeds folder in your personal NVDA configuration folder,
when installing the current version, a dialog will ask if you want to upgrade or install.
Choose update to preserve your saved feeds and to continue using them in the new installed version of readFeeds.

## Befehle

### Read Feeds menu

Sie können das Dialogfeld von Read Feedsüber das NVDA-Menü, und dort
Werkzeuge und dann Feeds aufrufen.

#### Feeds...

Opens a dialog with the following controls:

- Filtern nach: Ein Eingabefeld, um zuvor gespeicherte Feeds zu durchsuchen.
- A list of the saved feeds.
- Liste der Artikel: Öffnet einen Dialog, der die Artikelliste aus Ihrem
  aktuellen Feed anzeigt. Wählen Sie den Artikel, den Sie lesen möchten, und
  drücken Sie die Eingabetaste oder die Schaltfläche Webseite des
  ausgewählten Artikels öffnen, um die entsprechende Seite in Ihrem Browser
  zu öffnen. Klicken Sie auf die Schaltfläche Info-Artikel, um einen Dialog
  mit Titel und Link des ausgewählten Artikels zu öffnen; von diesem Dialog
  aus können Sie diese Informationen in die Zwischenablage kopieren.
- Feed öffnen: Öffnet den ausgewählten Feed in der Standardanwendung.
- Neu: Öffnet einen Dialog mit einem Eingabefeld zur Eingabe der Adresse
  eines neuen RSS-Feeds. Wenn die Adresse gültig ist und der Feed
  gespeichert werden kann, erscheint sein Name, basierend auf dem
  Feed-Titel, am Ende der Liste der RSS-Feeds.
- Umbenennen: Öffnet einen Dialog mit einem Eingabefeld zum Umbenennen des
  ausgewählten Feeds.
- Löschen: Öffnet einen Dialog zum Löschen des ausgewählten Feeds.
- Als standard festlegen: Legt den ausgewählten RSS-Feed als Standard fest,
  so dass auf seine Artikel mit den Tastenkürzel von NVDA zugegriffen werden
  kann.
- Open folder containing a backup of feeds: Opens a folder which may contain a backup of feeds. This can be useful to explore and delete feeds which shouldn't be imported when the add-on is updated.
- Schließen: Schließt den Dialog.

##### Hinweise

- If a feed named tempFeed is created, please rename it, as this file could be replaced when needed to create a feed whose name already exists.
- The feed set as the default can't be removed. The addressFile feed will be use as the default when the configuration is reset, so it can't be deleted.

\####Copy feeds folder... ####

Opens a dialog to choose a folder where you can save the personalFeeds directory of your feeds. By default the selected folder is the NVDA's configuration directory, which will create the personalFeeds directory.

#### Restore feeds...

Opens a dialog to select a folder which replaces your feeds in the personalFeeds folder. Make sure you load a folder containing feeds URLs.

### Tastaturbefehle

- STRG+Umschalt+NVDA+Leertaste: Sagt die aktuelle Adresse des Artikels
  an. Zweimaliges Drücken öffnet die Webseite des Artikels.
- STRG+Umschalt+NVDA+8: Der ausgewählte RSS-Feed wird neu geladen und der
  aktuellste Titel wird angesagt.
- Strg+Umschalt+NVDA+I: Sagt den aktuellen Feed-Titel und -Link an. Durch
  zweimaliges Drücken wird der Titel und der zugehörige Link in die
  Zwischenablage kopiert.
- STRG+Umschalt+NVDA+U: Sagt den Titel des vorherigen RSS-Feeds an.
- STRG+Umschalt+NVDA+O: Sagt den Titel des nächsten RSS-Feeds an.

## Benachrichtigungen

- Wenn der Titel oder die URL kopiert wurden.
- Wenn die Verbindung / das Neuladen eines RSS-Feeds fehlgeschlagen ist,
  oder wenn die URL nicht mit einem gültigen Feed übereinstimmt.
- NVDA will display an error message if it was not possible to backup or restore the personalFeeds folder.
- Im Titel des Dialogs für die Artikellisten werden der Name des
  ausgewählten Feeds und die Anzahl der verfügbaren Artikel angezeigt.

## Änderungen in 8.0

- Bei der Aktualisierung dieser Erweiterung werden die in der vorherigen
  Version gespeicherten Feeds automatisch in die neue Version kopiert, es
  sei denn, Sie möchten ausdrücklich, dass Feeds aus dem
  Hauptkonfigurationsordner von NVDA importiert werden.
- Wenn Sie den Dialog zum Kopieren von Feeds verwenden und der ausgewählte
  Ordner nicht "personalFeeds" heißt, wird ein Unterordner mit diesem Namen
  erstellt, um das Löschen von Verzeichnissen mit wichtigen Daten wie
  Dokumente oder Downloads zu verhindern.

## Änderungen bis 7.0

- Der RSS Feeds Dialog wird mit einen Schalter erweitert, um einen
  Backup-Ordner zu öffnen, der die Sicherungsdateien der Feeds enthalten
  kann.
- Wenn die Eingabe in der Filterfunktion keine Ergebnisse liefert, werden
  die Liste der Feeds und andere Dialogelemente nicht mehr angezeigt. Somit
  meldet NVDA nicht mehr "unbekannt" in der leeren Liste.
- Wenn die Liste der Artikel nicht angezeigt werden kann, beispielsweise
  wegen Fehlern beim Rss Feed, wird NVDA einen Fehler auslösen. Dadurch
  können Sie den RSS Feed Dialog nutzen, ohne NVDA neu starten zu müssen.

## Änderungen bis 6.0

- Wenn der Standardfeed aktualisiert wurde und er aufgrund von
  Serverproblemen nicht mehr funktioniert, werden die vorherigen Artikel
  nicht gelöscht und können mit den entsprechenden Tastenkombinationen
  gelesen werden.
- Fehler behoben: Der Standardfeed kann noch zweimal aktualisiert werden.

## Änderungen für 5.0

- Der Dialog der Artikelliste wurde erweitert.
- Kompatibel mit NVDA 2018.3 oder neuer (erforderlich).
- If needed, you can download the [last version compatible with NVDA 2017.3][3].

## Änderungen in 4.0

- Schaltfläche zum Öffnen des ausgewählten Feeds über den Feed-Dialog
  hinzugefügt.

## Änderungen in 3.0

- Die Dialoge zur Verwaltung von RSS-Feed-Dateien wurden entfernt. Jetzt ist
  ihre Funktionalität im RSS-Feeds-Dialog enthalten.
- Die visuelle Darstellung der Dialoge wurde verbessert und entspricht dem
  Erscheinungsbild der Dialoge in NVDA.
- Der Standard-Feed wird in der NVDA-Konfiguration gespeichert. Daher ist es
  möglich, verschiedene Standard-Feeds in Konfigurationsprofilen
  einzustellen.
- NVDA 2016.4 oder höher ist erforderlich.

## Änderungen in 2.0

- Hilfe zur Erweiterung ist über den Dialog "Erweiterungen verwalten"
  verfügbar.

## Änderungen in 1.0

- Initial version.

[1]: http://addons.nvda-project.org/files/get.php?file=rf
[2]: http://addons.nvda-project.org/files/get.php?file=rf-dev
[3]: http://addons.nvda-project.org/files/get.php?file=rf-o
