# Read Feeds #

* Авторы: Noelia Ruiz Martínez, Mesar Hameed

Это дополнение обеспечивает простой способ читать новости формата Atom или
RSS, используя NVDA.  Новостные ленты не будут обновляться автоматически.
Ниже, когда мы упоминаем новостные ленты, мы имеем в виду как RSS, так и
ATOM каналы.

## Команды ##

### Диалог Чтение Новостей ###

You can access the Read Feeds dialog from the nvda menu, Tools submenu,
Feeds item.

Он содержит следующие элементы управления:

* Фильтр по: поле редактирования для поиска ранее сохраненных новостных
  лент.
* A list of the saved feeds, focused when the dialog is opened.
* List of articles: Opens a dialog which presents the articles list from
  your current feed. Select the article you want to read and press Enter or
  Open web page of selected article button to open the corresponding page in
  your browser. Press About article button to open a dialog showing title
  and link of the selected article; from this dialog, you'll be able to copy
  this info to the clipboard.
* Открыть новостную ленту: Открывает выбранную новостную ленту в приложении
  по умолчанию.
* Open feed as HTML: Opens the selected feed in the default web browser. You
  will be able to show or hide publication dates and buttons to copy
  information about articles to clipboard.
* Copy feed address: Opens a dialog to confirm if you want to copy the feed
  address to clipboard.
* Новый: открывает диалог с полем редактирования, где можно ввести адрес
  новой ленты. Если адрес действителен и новостная лента может быть
  сохранена, её имя появится в низу списка новостных лент, исходя из
  названия новостной ленты.
* Переименовать: открывает диалог с полем редактирования для переименования
  выбранной новостной ленты.
* Удалить: открывает диалог для удаления выбранной ленты после
  подтверждения.
* Установить по умолчанию: устанавливает выбранную новостную ленту по
  умолчанию, и её статьи могут быть доступны с помощью жестов NVDA.
* Import feeds from OPML file: Opens a dialog to add new feeds from an OPML
  file.
* Save feeds to OPML file: Opens a dialog to save the feeds available from
  the Feeds dialog in an OPML file.
* Preferences: Opens the settings dialog for readFeeds, also available in
  NVDA's menu, Preferences, settings, readFeeds category.
* Закрыть: закрывает диалог новостных лент.

### Примечания #####

* The Filter by edit box can be placed after the Open article button from
  NVDA's menu, Preferences, Settings, Read feeds category, or pressing the
  Preferences button of the Feeds dialog.
* This panel has an option to show article dates on the List of articles
  dialog.


### Клавишные команды ###

* Ctrl+Shift+NVDA+Пробел: Объявляет URL текущей статьи. Двойное нажатие
  откроет веб-страницу.
* Ctrl+Shift+NVDA+8: Обновляет выбранную новостную ленту и объявляет своё
  последнее название.
* Ctrl+Shift+NVDA+I: Объявляет название и ссылку текущей новостной
  ленты. Двойное нажатие скопирует название и соответствующую ссылку в буфер
  обмена.
* Ctrl+Shift+NVDA+U: Объявляет название предыдущей новостной ленты.
* Ctrl+Shift+NVDA+O: Объявляет название следующей новостной ленты.

## Оповещения ##

* Когда название или URL были скопированы.
* Когда не удается подключить/обновить ленту, или URL-адрес не соответствует
  допустимой новостной ленте.
* NVDA отобразит сообщение об ошибке, если новый канал не может быть создан.
* Диалог с названием списка статей отображает имя выбранной новостной ленты
  с количеством доступных элементов.

## Изменения для 21.0

* Feeds with untitled articles can be presented in the Articles dialog, and
  opened as HTML.

## Изменения для 20.0

* universalFeedParser обновлен до версии 5.0.1, добавлена поддержка большего
  количества каналов.

## Изменения для 14.0

* Исправлена ошибка, из-за которой было невозможно добавлять некоторые
  каналы.

## Изменения для 13.0

* Дополнение нельзя использовать на защищённых экранах.
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

## Изменения для 12.0

* Исправлена ошибка, из-за которой ярлыки для элементов меню сервисов NVDA
  работали не так, как ожидалось.

## Изменения для 11.0

* Совместимость с NVDA 2021.1

## Изменения для 10.0 ##

* Добавлена кнопка для открытия выбранной ленты в формате HTML в
  веб-браузере по умолчанию.
* If a new feed cannot be created, this will be notified in an error dialog.
* Улучшен порядок и представление некоторых статей.
* More feeds may be supported.
* When the feeds dialog is opened, the list of feeds will be focused instead
  of the search edit box.
* You can choose if the search edit box is placed after the list of feeds,
  useful to focus the list even when switching from another window without
  closing the Feeds dialog.
* Добавлена кнопка для копирования адреса канала в буфер обмена из
  диалогового окна "Каналы".

## Изменения для 9.0 ##

* Требуется NVDA 2019.3 или позже.

## Изменения для 8.0 ##

* When the add-on is updated, feeds saved in the previous version of the
  add-on will be automatically copied to the new version, unless you prefer
  to import feeds saved in the main configuration folder of NVDA.
* When using the dialog to copy feeds, if the chosen folder is not named
  personalFeeds, a subfolder with this name will be created to prevent the
  deletion of directories containing important data, such as Documents or
  Downloads.

## Изменения для 7.0 ##

* The Feeds dialog includes a button to open a folder which may contain a
  backup of feeds.
* When using the edit box to filter feeds, if no results are found, the list
  of feeds and other controls are disabled, so that NVDA doesn't report
  "unknown" in the empty list.
* If the list of articles dialog can't be shown, for example due to errors
  in the feed, NVDA will raise an error, so that the feeds dialog can be
  used without restarting NVDA.

## Изменения для 6.0 ##

* When the default feed has been updated and it stops working due to server
  issues, the previous articles aren't deleted and can be read with the
  corresponding keystrokes.
* Fix regression: The default feed can be updated twice again.

## Изменения для 5.0 ##

* Улучшен диалог со списком статей.
* Совместимо с NVDA 2018.3 или позднее (обязательно).
* При необходимости вы можете загрузить [последнюю версию, совместимую с
  NVDA 2017.3][3].

## Изменения для 4.0 ##

* Добавлена кнопка открытия новостной ленты в диалоге новостных лент.

## Изменения для 3.0 ##

* Диалоги управления файлами лент были удалены. Сейчас их функциональность
  вошла в диалог новостных лент.
* Визуальное представление диалогов было модифицировано, придерживаясь
  внешнего вида диалогов, отображаемых в NVDA.
* Новостная лента по умолчанию сохраняется в конфигурации NVDA. Таким
  образом, можно установить различные новостные ленты по умолчанию в
  различных профилях конфигурации.
* Требуется NVDA 2016.4.

## Изменения для 2.0 ##

* Справка дополнения доступна в диспетчере дополнений.

## Изменения для 1.0 ##

* Первоначальная версия.

[[!tag dev stable]]

[3]: https://www.nvaccess.org/addonStore/legacy?file=rf-o
