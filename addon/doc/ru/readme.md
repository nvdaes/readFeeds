# Read Feeds

- Авторы: Noelia Ruiz Martínez, Mesar Hameed
- Совместимость с NVDA 2021.1
- Download [stable version][1]
- Download [development version][2]

Это дополнение обеспечивает простой способ читать новости формата Atom или
RSS, используя NVDA.
Новостные ленты не будут обновляться автоматически.
Ниже, когда мы упоминаем новостные ленты, мы имеем в виду как RSS, так и
ATOM каналы.

## Installation or Update:

If you used a previous version of this addon, and there is an RSS or personalFeeds folder in your personal NVDA configuration folder,
when installing the current version, a dialog will ask if you want to upgrade or install.
Choose update to preserve your saved feeds and to continue using them in the new installed version of readFeeds.

## Команды

### Read Feeds menu

You can access the Read Feeds submenu from the nvda menu, Tools submenu, where the following menu options are available:

#### Feeds...

Opens a dialog with the following controls:

- Фильтр по: поле редактирования для поиска ранее сохраненных новостных
  лент.
- A list of the saved feeds.
- Список статей: Открывает диалог, в котором представлен список статей из
  вашей текущей ленты. Выберите статью, которую вы хотите прочитать, и
  нажмите Enter или кнопку Открыть веб-страницу выбранной статьи, чтобы
  открыть соответствующую страницу в вашем браузере. Нажмите кнопку "О
  статье", чтобы открыть диалог с названием и ссылкой на выбранную статью;
  из этого диалога вы сможете скопировать эту информацию в буфер обмена.
- Открыть новостную ленту: Открывает выбранную новостную ленту в приложении
  по умолчанию.
- Новый: открывает диалог с полем редактирования, где можно ввести адрес
  новой ленты. Если адрес действителен и новостная лента может быть
  сохранена, её имя появится в низу списка новостных лент, исходя из
  названия новостной ленты.
- Переименовать: открывает диалог с полем редактирования для переименования
  выбранной новостной ленты.
- Удалить: открывает диалог для удаления выбранной ленты после
  подтверждения.
- Установить по умолчанию: устанавливает выбранную новостную ленту по
  умолчанию, и её статьи могут быть доступны с помощью жестов NVDA.
- Open folder containing a backup of feeds: Opens a folder which may contain a backup of feeds. This can be useful to explore and delete feeds which shouldn't be imported when the add-on is updated.
- Закрыть: закрывает диалог новостных лент.

##### Примечания

- If a feed named tempFeed is created, please rename it, as this file could be replaced when needed to create a feed whose name already exists.
- The feed set as the default can't be removed. The addressFile feed will be use as the default when the configuration is reset, so it can't be deleted.

\####Copy feeds folder... ####

Opens a dialog to choose a folder where you can save the personalFeeds directory of your feeds. By default the selected folder is the NVDA's configuration directory, which will create the personalFeeds directory.

#### Restore feeds...

Opens a dialog to select a folder which replaces your feeds in the personalFeeds folder. Make sure you load a folder containing feeds URLs.

### Клавишные команды

- Ctrl+Shift+NVDA+Пробел: Объявляет URL текущей статьи. Двойное нажатие
  откроет веб-страницу.
- Ctrl+Shift+NVDA+8: Обновляет выбранную новостную ленту и объявляет своё
  последнее название.
- Ctrl+Shift+NVDA+I: Объявляет название и ссылку текущей новостной
  ленты. Двойное нажатие скопирует название и соответствующую ссылку в буфер
  обмена.
- Ctrl+Shift+NVDA+U: Объявляет название предыдущей новостной ленты.
- Ctrl+Shift+NVDA+O: Объявляет название следующей новостной ленты.

## Оповещения

- Когда название или URL были скопированы.
- Когда не удается подключить/обновить ленту, или URL-адрес не соответствует
  допустимой новостной ленте.
- NVDA will display an error message if it was not possible to backup or restore the personalFeeds folder.
- Диалог с названием списка статей отображает имя выбранной новостной ленты
  с количеством доступных элементов.

## Изменения для 8.0

- При обновлении дополнения каналы, сохранённые в предыдущей версии
  дополнения, будут автоматически скопированы в новую версию, если только вы
  не предпочитаете импортировать каналы, сохранённые в главной папке
  конфигурации NVDA.
- При использовании диалога для копирования новостных каналов, если
  выбранная папка не имеет имени personalFeeds, будет создана подпапка с
  таким именем, чтобы предотвратить удаление каталогов, содержащих важные
  данные, такие как документы или загрузки.

## Изменения для 7.0

- В диалоге "Новостные ленты" есть кнопка для открытия папки, которая может
  содержать резервную копию каналов.
- При использовании поля редактирования для фильтрации каналов, если
  результаты не найдены, список каналов и другие элементы управления
  отключаются, чтобы NVDA не сообщала "неизвестно" в пустом списке.
- Если диалог списка статей не может быть отображён, например, из-за ошибок
  в ленте, NVDA выдаст сообщение об ошибке, так что диалог лент можно будет
  использовать без перезапуска NVDA.

## Изменения для 6.0

- Когда лента новостей по умолчанию обновляется и перестает работать из-за
  проблем с сервером, предыдущие статьи не удаляются и могут быть прочитаны
  с помощью соответствующих нажатий клавиш.
- Исправлена регрессия: лента данных по умолчанию может быть обновлена еще
  дважды.

## Изменения для 5.0

- Улучшен диалог со списком статей.
- Совместимо с NVDA 2018.3 или позднее (обязательно).
- If needed, you can download the [last version compatible with NVDA 2017.3][3].

## Изменения для 4.0

- Добавлена кнопка открытия новостной ленты в диалоге новостных лент.

## Изменения для 3.0

- Диалоги управления файлами лент были удалены. Сейчас их функциональность
  вошла в диалог новостных лент.
- Визуальное представление диалогов было модифицировано, придерживаясь
  внешнего вида диалогов, отображаемых в NVDA.
- Новостная лента по умолчанию сохраняется в конфигурации NVDA. Таким
  образом, можно установить различные новостные ленты по умолчанию в
  различных профилях конфигурации.
- Требуется NVDA 2016.4.

## Изменения для 2.0

- Справка дополнения доступна в диспетчере дополнений.

## Изменения для 1.0

- Первоначальная версия.

[1]: http://addons.nvda-project.org/files/get.php?file=rf
[2]: http://addons.nvda-project.org/files/get.php?file=rf-dev
[3]: http://addons.nvda-project.org/files/get.php?file=rf-o
