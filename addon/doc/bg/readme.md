# Read Feeds (Четене на източници) #

* Автори: Noelia Ruiz Martínez, Mesar Hameed
* Изтегляне [стабилна версия][2]
* Изтегляне [работна версия][1]

Тази добавка предоставя бърз и лесен начин за четене от източници в Atom или
RSS формат с NVDA.  Източниците няма да бъдат опреснявани автоматично.
Когато споменаваме думата източници, имаме предвид както RSS, така и ATOM
канали.

## Инсталиране или обновяване: ##

Ако сте използвали предишна версия на тази добавка и вече имате папка с име
RSS или personalFeeds във вашата папка с потребителски настройки за NVDA,
когато инсталирате версия 6.0 или по-нова, ще попаднете на диалог, който ще
ви попита дали искате да обновите вашата добавка или да инсталирате на
чисто.  Изберете обновяване, за да съхраните вашите запазени източници и да
продължите да ги използвате в новоинсталираната версия на readFeeds.

## Команди: ##

### Меню на Read Feeds ###

Можете да достигнете до подменюто на Read Feeds от менюто на nvda, NVDA+N,
където имате възможност да изберете някоя от следните опции:

- Article list...  Presents the article list from your current feed. Select
the article you want to read and press OK button to open the corresponding
page in your browser.  - Temporary feed address... control + NVDA + shift +
enter: Opens a dialog for typing a new URL to select another feed. The
current URL will be shown in this dialog.  - Load feed address from
file... NVDA+control+enter: Opens a dialog to select a feed from a saved
file containing a feed URL.  - Save current feed address to
file... NVDA+shift+enter: opens a dialog for selecting the file where
current feed URL will be saved.  If you save to the special file
addressFile.txt, this particular feed will be used as your default feed.  -
Refresh current feed: control+shift+NVDA+8: Refresh selected feed. The feeds
will not be updated automatically when Read Feeds addon is started.  -
Backup feeds folder...  opens a dialog to choose a folder where you can save
the personalFeeds directory of your feeds. By default the selected folder is
the NVDA's configuration directory, which will create the personalFeeds
directory.  - Restore feeds...  Opens a dialog to select a folder which
replaces your feeds in the personalFeeds folder. Make sure you load a folder
containing feeds URLs.

Note: If you want to delete a previously saved feed URL, just remove the
corresponding file.

### Клавишни команди: ###

- Ctrl+Shift+NVDA+Space: Announces current article's URL. Pressing twice
will open the web page.  - Ctrl+Shift+NVDA+8: Refreshes the selected feed
and announces its most recent title.  - Ctrl+Shift+NVDA+I: Announces current
feed title. Pressing twice will copy the title and related link to
clipboard.  - Ctrl+Shift+NVDA+U: Announces previous feed title.  -
Ctrl+Shift+NVDA+O: Announces next feed title.

## Уведомления: ##

- When the title or URL have been copied.  - When unable to connect/refresh
a feed, or the URL does not correspond to a valid feed.  - NVDA will display
an error message if it was not possible to backup the personalFeeds folder.
- The title of the article list dialog displays the selected feed name and
number of items available.

## Changes for 2.0 ##
*	 Add-on help is available from the Add-ons Manager.

## Промени във версия 1.0 ##
*	 Първоначално издание

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf-dev

[2]: http://addons.nvda-project.org/files/get.php?file=rf

