# Read Feeds #

* Авторы: Noelia Ruiz Martínez, Mesar Hameed
* NVDA compatibility: 2018.3 to 2019.2
* Загрузить [стабильную версию][1]
* Загрузить [разрабатываемую версию][2]

Это дополнение обеспечивает простой способ читать новости формата Atom или
RSS, используя NVDA.  Новостные ленты не будут обновляться автоматически.
Ниже, когда мы упоминаем новостные ленты, мы имеем в виду как RSS, так и
ATOM каналы.

## Установка или Обновление: ##

Если вы использовали предыдущую версию этого дополнения, и есть папка RSS
или personalFeeds в пользовательской папке конфигурации NVDA, при установке
текущей версии, появится диалог с запросом  обновления или
установки. Выберите обновление, чтобы сохранить ваши сохраненные ленты
новостей и продолжать использовать их в новой установленной версии
readFeeds.

## Команды: ##

### Меню Чтение Новостей ###

Вы можете получить доступ к подменю чтение новостей из меню NVDA, Сервис,
где доступны следующие пункты меню:

#### Новостные ленты... ####

Открывает диалог со следующими элементами управления:

* Фильтр по: поле редактирования для поиска ранее сохраненных новостных
  лент.
* Список сохраненных новостных лент.
* List of articles: Opens a dialog which presents the articles list from
  your current feed. Select the article you want to read and press Enter or
  Open web page of selected article button to open the corresponding page in
  your browser. Press About article button to open a dialog showing title
  and link of the selected article; from this dialog, you'll be able to copy
  this info to the clipboard.
* Открыть новостную ленту: Открывает выбранную новостную ленту в приложении
  по умолчанию.
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
* Open folder containing a backup of feeds: Opens a folder which may contain
  a backup of feeds. This can be useful to explore and delete feeds which
  shouldn't be imported when the add-on is updated.
* Закрыть: закрывает диалог новостных лент.

##### Примечания #####

* Если создан канал с именем tempFeed, пожалуйста, переименуйте его, так как
  этот файл может быть заменён, когда потребуется создать канал с  уже
  существующим именем.
* Новостная лента по умолчанию не может быть удалена. Она используется для
  сброса настроек в файле addressFile, и поэтому не может быть удалена.

####Копировать Папку новостных лент... ####

Открывает диалог для выбора папки, куда можно сохранить каталог
personalFeeds. По умолчанию выбран каталог конфигурации nvda, в котором
возможно создать каталог personalFeeds.

#### Восстановить новостные ленты... ####

Открывает диалог для выбора папки, из которой заменяются ваши новостные
ленты в папке personalFeeds. Убедитесь, что вы загружаете папку, содержащую
URL-адреса новостных лент.

### Команды клавиш ###

* Ctrl+Shift+NVDA+Пробел: Объявляет URL текущей статьи. Двойное нажатие
  откроет веб-страницу.
* Ctrl+Shift+NVDA+8: Обновляет выбранную новостную ленту и объявляет своё
  последнее название.
* Ctrl+Shift+NVDA+I: Объявляет название и ссылку текущей новостной
  ленты. Двойное нажатие скопирует название и соответствующую ссылку в буфер
  обмена.
* Ctrl+Shift+NVDA+U: Объявляет название предыдущей новостной ленты.
* Ctrl+Shift+NVDA+O: Объявляет название следующей новостной ленты.

## Оповещения: ##

* Когда название или URL были скопированы.
* Когда не удается подключить/обновить ленту, или URL-адрес не соответствует
  допустимой новостной ленте.
* NVDA отобразит сообщение об ошибке, если не удалось сделать или
  восстановить резервную копию папки personalFeeds.
* Диалог с названием списка статей отображает имя выбранной новостной ленты
  с количеством доступных элементов.

## Changes for 8.0 ##

* When the add-on is updated, feeds saved in the previous version of the
  add-on will be automatically copied to the new version, unless you prefer
  to import feeds saved in the main configuration folder of NVDA.
* When using the dialog to copy feeds, if the chosen folder is not named
  personalFeeds, a subfolder with this name will be created to prevent the
  deletion of directories containing important data, such as Documents or
  Downloads.

## Changes for 7.0 ##

* The Feeds dialog includes a button to open a folder which may contain a
  backup of feeds.
* When using the edit box to filter feeds, if no results are found, the list
  of feeds and other controls are disabled, so that NVDA doesn't report
  "unknown" in the empty list.
* If the list of articles dialog can't be shown, for example due to errors
  in the feed, NVDA will raise an error, so that the feeds dialog can be
  used without restarting NVDA.

## Changes for 6.0 ##

* When the default feed has been updated and it stops working due to server
  issues, the previous articles aren't deleted and can be read with the
  corresponding keystrokes.
* Fix regression: The default feed can be updated twice again.

## Changes for 5.0 ##

* The articles list dialog has been enhanced.
* Compatible with NVDA 2018.3 or later (required).
* If needed, you can download the [last version compatible with NVDA
  2017.3][3].

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

[1]: https://addons.nvda-project.org/files/get.php?file=rf

[2]: https://addons.nvda-project.org/files/get.php?file=rf-dev

[3]: https://addons.nvda-project.org/files/get.php?file=rf-o
