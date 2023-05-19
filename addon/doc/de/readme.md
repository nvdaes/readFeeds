# RSS-Feeds lesen #

* Autoren: Noelia Ruiz Martínez, Mesar Hameed
* [Stabile Version herunterladen][1] (kompatibel mit NVDA 2019.3 und neuer)
* [Beta-Version herunterladen][2] (kompatibel mit NVDA 2019.3 und neuer)

Diese Erweiterung bietet eine einfache Möglichkeit, RSS-Feeds in den
Formaten Atom oder RSS mit NVDA zu lesen. Die Feeds werden nicht automatisch
aktualisiert. Wenn wir weiter unten  von Feeds sprechen, dann meinen wir
sowohl RSS- als auch  ATOM-Feeds.

## Befehle ##

### Dialogfeld für RSS-Feeds lesen ###

Sie können das Dialogfeld von Read Feedsüber das NVDA-Menü, und dort
Werkzeuge und dann Feeds aufrufen.

Sie enthält die folgenden Steuerelemente:

* Filtern nach: Ein Eingabefeld, um zuvor gespeicherte Feeds zu durchsuchen.
* Eine Liste der gespeicherten RSS-Feeds, die beim Öffnen des Dialogfelds
  hervorgehoben werden.
* Liste der Artikel: Öffnet einen Dialog, der die Artikelliste aus Ihrem
  aktuellen Feed anzeigt. Wählen Sie den Artikel, den Sie lesen möchten, und
  drücken Sie die Eingabetaste oder die Schaltfläche Webseite des
  ausgewählten Artikels öffnen, um die entsprechende Seite in Ihrem Browser
  zu öffnen. Klicken Sie auf die Schaltfläche Info-Artikel, um einen Dialog
  mit Titel und Link des ausgewählten Artikels zu öffnen; von diesem Dialog
  aus können Sie diese Informationen in die Zwischenablage kopieren.
* Feed öffnen: Öffnet den ausgewählten Feed in der Standardanwendung.
* RSS-Feed als HTML öffnen: Öffnet den ausgewählten RSS-Feed im
  Standard-Webbrowser. Sie können Veröffentlichungsdaten und Schaltflächen
  ein- oder ausblenden, um Informationen zu Artikeln in die Zwischenablage
  zu kopieren.
* Adresse des RSS-Feed kopieren: Öffnet ein Dialogfeld, in dem bestätigt
  wird, ob die Feed-Adresse in die Zwischenablage kopiert werden soll.
* Neu: Öffnet einen Dialog mit einem Eingabefeld zur Eingabe der Adresse
  eines neuen RSS-Feeds. Wenn die Adresse gültig ist und der Feed
  gespeichert werden kann, erscheint sein Name, basierend auf dem
  Feed-Titel, am Ende der Liste der RSS-Feeds.
* Umbenennen: Öffnet einen Dialog mit einem Eingabefeld zum Umbenennen des
  ausgewählten Feeds.
* Löschen: Öffnet einen Dialog zum Löschen des ausgewählten Feeds.
* Als standard festlegen: Legt den ausgewählten RSS-Feed als Standard fest,
  so dass auf seine Artikel mit den Tastenkürzel von NVDA zugegriffen werden
  kann.
* RSS-Feeds aus OPML-Datei importieren: Öffnet einen Dialogfeld zum
  Hinzufügen neuer RSS-Feeds aus einer OPML-Datei.
* RSS-Feeds in OPML-Datei speichern: Öffnet ein Dialogfeld zum Speichern der
  im Dialogfeld für die RSS-Feeds verfügbaren Feeds in einer OPML-Datei.
* Einstellungen: Öffnet das Dialogfeld mit den Einstellungen der
  erweiterung, der auch im NVDA-Menü "Einstellungen", "Einstellungen" und
  "RSS-Feeds lesen" verfügbar ist.
* Schließen: Schließt den Dialog.

### Hinweise #####

* Das Bearbeitungsfeld Filtern nach kann nach der Schaltfläche Artikel
  öffnen im NVDA-Menü, Einstellungen, Einstellungen, Feeds lesen oder durch
  Klicken auf die Schaltfläche Einstellungen im Dialogfeld Feeds platziert
  werden.
* Dieses Panel verfügt über eine Option zur Anzeige von Artikeldaten im
  Dialogfeld für die Liste der Artikel.


### Tastaturbefehle ###

* STRG+Umschalt+NVDA+Leertaste: Sagt die aktuelle Adresse des Artikels
  an. Zweimaliges Drücken öffnet die Webseite des Artikels.
* STRG+Umschalt+NVDA+8: Der ausgewählte RSS-Feed wird neu geladen und der
  aktuellste Titel wird angesagt.
* Strg+Umschalt+NVDA+I: Sagt den aktuellen Feed-Titel und -Link an. Durch
  zweimaliges Drücken wird der Titel und der zugehörige Link in die
  Zwischenablage kopiert.
* STRG+Umschalt+NVDA+U: Sagt den Titel des vorherigen RSS-Feeds an.
* STRG+Umschalt+NVDA+O: Sagt den Titel des nächsten RSS-Feeds an.

## Benachrichtigungen ##

* Wenn der Titel oder die URL kopiert wurden.
* Wenn die Verbindung / das Neuladen eines RSS-Feeds fehlgeschlagen ist,
  oder wenn die URL nicht mit einem gültigen Feed übereinstimmt.
* NVDA zeigt eine Fehlermeldung an, wenn ein neuer Feed nicht erstellt
  werden konnte.
* Im Titel des Dialogs für die Artikellisten werden der Name des
  ausgewählten Feeds und die Anzahl der verfügbaren Artikel angezeigt.

## Änderungen in 21.0

* RSS-Feeds mit unbetitelten Artikeln können im Dialogfeld der Artikel
  angezeigt und als HTML geöffnet werden.

## Änderungen in 20.0

* Der Universal Feed Parser wurde auf 5.0.1 aktualisiert und unterstützt nun
  mehr RSS-Feeds.

## Änderungen in 14.0

* Es wurde ein Fehler behoben, der das Hinzufügen einiger Feeds unmöglich
  machte.

## Änderungen in 13.0

* Diese Erweiterung ist nicht länger verwendbar mehr im geschützten Modus.
* RSS-Feeds werden über OPML-Dateien verwaltet.
* Auf Grund von Änderungen in der Verwaltung der RSS-Feeds gibt es
  Änderungen in der Konfigurationsdatei, in der der Standard-Feed
  eingestellt ist. Bitte verwenden Sie den Dialogfeld für die RSS-Feeds,
  wenn Sie es wieder einstellen möchten.
* Die noch im alten Format gespeicherten Textdateien, werden automatisch in
  das neue OPML-Format umgewandelt, sobald die neue Version der Erweiterung
  zum ersten Mal gestartet wird.
* Die Funktion zum Kopieren und Wiederherstellen von RSS-Feeds wurde durch
  die neuen Dateien im OPML-Format ersetzt.
* Inkompatible RSS-Feeds können vor dem Hinzufügen verarbeitet werden, um
  sie mit der Erweiterung kompatibel zu machen.
* Im Einstellungsfenster für Read Feeds gibt es eine neue Option, mit der
  das Datum des Artikels in der Liste der Artikel angezeigt werden kann.

## Änderungen in 12.0

* Es wurde ein Fehler behoben, der dazu führte, dass Verknüpfungen für
  Elemente im NVDA-Menüs unter "Werkzeuge" nicht wie erwartet
  funktionierten.

## Änderungen in 11.0

* Kompatibel mit NVDA 2021.1

## Änderungen in 10.0 ##

* Es wurde eine Schaltfläche hinzugefügt, um den ausgewählten RSS-Feed als
  HTML im Standard-Webbrowser zu öffnen.
* Wenn kein neuer RSS-Feed erstellt werden konnte, wird dies in einem
  Fehlerdialog angezeigt.
* Verbesserte Reihenfolge und Präsentation einiger Artikel.
* Weitere Feeds werden möglicherweise unterstützt.
* Wenn das Dialogfeld "Feeds" geöffnet wird, wird die Liste der Feeds
  anstelle des Bearbeitungsfelds "Suche" hervorgehoben.
* Sie können auswählen, ob das Suchfeld für die Suche hinter der Liste der
  Feeds platziert werden soll. Dies ist nützlich, um die Liste auch dann zu
  fokussieren, wenn Sie aus einem anderen Fenster wechseln, ohne das
  Dialogfeld "Feeds" zu schließen.
* Es wurde eine Schaltfläche hinzugefügt, um die Adresse des RSS-Feed aus
  dem Dialogfeld der Feeds in die Zwischenablage zu kopieren.

## Änderungen für 9.0 ##

* Erfordert NVDA 2019.3 oder höher.

## Änderungen in 8.0 ##

* Bei der Aktualisierung dieser Erweiterung werden die in der vorherigen
  Version gespeicherten Feeds automatisch in die neue Version kopiert, es
  sei denn, Sie möchten ausdrücklich, dass Feeds aus dem
  Hauptkonfigurationsordner von NVDA importiert werden.
* Wenn Sie den Dialog zum Kopieren von Feeds verwenden und der ausgewählte
  Ordner nicht "personalFeeds" heißt, wird ein Unterordner mit diesem Namen
  erstellt, um das Löschen von Verzeichnissen mit wichtigen Daten wie
  Dokumente oder Downloads zu verhindern.

## Änderungen bis 7.0 ##

* Der RSS Feeds Dialog wird mit einen Schalter erweitert, um einen
  Backup-Ordner zu öffnen, der die Sicherungsdateien der Feeds enthalten
  kann.
* Wenn die Eingabe in der Filterfunktion keine Ergebnisse liefert, werden
  die Liste der Feeds und andere Dialogelemente nicht mehr angezeigt. Somit
  meldet NVDA nicht mehr "unbekannt" in der leeren Liste.
* Wenn die Liste der Artikel nicht angezeigt werden kann, beispielsweise
  wegen Fehlern beim Rss Feed, wird NVDA einen Fehler auslösen. Dadurch
  können Sie den RSS Feed Dialog nutzen, ohne NVDA neu starten zu müssen.

## Änderungen bis 6.0 ##

* Wenn der Standardfeed aktualisiert wurde und er aufgrund von
  Serverproblemen nicht mehr funktioniert, werden die vorherigen Artikel
  nicht gelöscht und können mit den entsprechenden Tastenkombinationen
  gelesen werden.
* Fehler behoben: Der Standardfeed kann noch zweimal aktualisiert werden.

## Änderungen für 5.0 ##

* Der Dialog der Artikelliste wurde erweitert.
* Kompatibel mit NVDA 2018.3 oder neuer (erforderlich).
* Bei Bedarf können Sie die [letzte Version][3], die mit NVDA 2017.3
  kompatibel ist herunterladen.

## Änderungen in 4.0 ##

* Schaltfläche zum Öffnen des ausgewählten Feeds über den Feed-Dialog
  hinzugefügt.

## Änderungen in 3.0 ##

* Die Dialoge zur Verwaltung von RSS-Feed-Dateien wurden entfernt. Jetzt ist
  ihre Funktionalität im RSS-Feeds-Dialog enthalten.
* Die visuelle Darstellung der Dialoge wurde verbessert und entspricht dem
  Erscheinungsbild der Dialoge in NVDA.
* Der Standard-Feed wird in der NVDA-Konfiguration gespeichert. Daher ist es
  möglich, verschiedene Standard-Feeds in Konfigurationsprofilen
  einzustellen.
* NVDA 2016.4 oder höher ist erforderlich.

## Änderungen in 2.0 ##

* Hilfe zur Erweiterung ist über den Dialog "Erweiterungen verwalten"
  verfügbar.

## Änderungen in 1.0 ##

* Ehrstveröffentlichung.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=readFeeds

[2]: https://www.nvaccess.org/addonStore/legacy?file=readFeeds-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=rf-o
