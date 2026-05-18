# Read Feeds dialog

- Authors: Noelia Ruiz Martínez, Mesar Hameed
- 兼容 NVDA 2021.1
- Download [stable version][1]
- Download [development version][2]

此插件提供了一种使用NVDA以Atom或RSS格式读取订阅源的简单方法。 Feed不会自动刷新。下面我们提到feed时，我们指的是RSS和ATOM提要。
The feeds will not be refreshed automatically.
Below when we mention feeds, we mean both RSS and ATOM feeds.

## Installation or Update:

If you used a previous version of this addon, and there is an RSS or personalFeeds folder in your personal NVDA configuration folder,
when installing the current version, a dialog will ask if you want to upgrade or install.
Choose update to preserve your saved feeds and to continue using them in the new installed version of readFeeds.

## Commands:

### Read Feeds-NVDA-RSS阅读插件

You can access the Read Feeds dialog from the nvda menu, Tools submenu,
Feeds item.

#### Feeds...

Opens a dialog with the following controls:

- 过滤条件：用于搜索以前保存的feed的编辑框。
- A list of the saved feeds.
- List of articles: Opens a dialog which presents the articles list from your current feed. Select the article you want to read and press Enter or Open web page of selected article button to open the corresponding page in your browser. Press About article button to open a dialog showing title and link of the selected article; from this dialog, you'll be able to copy this info to the clipboard.
- 打开feed：在默认应用程序中打开所选feed。
- New: Opens a dialog with an edit box to enter the address of a new feed. If the address is valid and the feed can be saved, its name, based on the feed title, will appear at the bottom of the feeds list.
- 重命名：打开一个带有编辑框的对话框，以重命名所选的源。
- Delete: Opens a dialog to delete the selected feed after confirmation.
- 设置默认值：将选定的Feed设置为默认值，以便可以使用NVDA的快捷键访问其文章。
- Open folder containing a backup of feeds: Opens a folder which may contain a backup of feeds. This can be useful to explore and delete feeds which shouldn't be imported when the add-on is updated.
- 关闭：关闭“源”对话框。

##### Notes

- If a feed named tempFeed is created, please rename it, as this file could be replaced when needed to create a feed whose name already exists.
- The feed set as the default can't be removed. The addressFile feed will be use as the default when the configuration is reset, so it can't be deleted.

\####Copy feeds folder... ####

Opens a dialog to choose a folder where you can save the personalFeeds directory of your feeds. By default the selected folder is the NVDA's configuration directory, which will create the personalFeeds directory.

#### Restore feeds...

Opens a dialog to select a folder which replaces your feeds in the personalFeeds folder. Make sure you load a folder containing feeds URLs.

### Keyboard commands:

- Ctrl + Shift + NVDA + Space：朗读当前文章的URL。按两次将打开网页。 Pressing twice will open the web page.
- Ctrl + Shift + NVDA + 8：刷新选定的Feed并朗读其最新的标题。
- Ctrl + Shift + NVDA + I：朗读当前RSS源的标题和链接。按两次将标题和相关链接复制到剪贴板。 Pressing twice will copy the title and related link to clipboard.
- Ctrl + Shift + NVDA + U：朗读当前源的上一个的标题。
- Ctrl + Shift + NVDA + O：朗读当前源的下一个标题。

## 通知

- 复制标题或URL时。
- 无法连接/刷新Feed时，或者URL与有效Feed不对应。
- NVDA will display an error message if a new feed cannot be created.
- “文章列表”对话框的标题显示所选的源名称和可用项目数。

## 版本8.0

- 更新插件后，除非您更喜欢导入保存在NVDA主配置文件夹中的feed，否则将保存在以前版本的插件中的提要将自动复制到新版本。
- 使用对话框复制供稿时，如果所选文件夹未命名为personalFeeds，则将创建具有此名称的子文件夹，以防止删除包含重要数据的目录，例如“文档”或“下载”。

## 版本7.0

- "源" 对话框中包含一个按钮, 用于打开可能包含源备份的文件夹。
- 使用编辑框筛选源时, 如果未找到任何结果, 则会禁用源和其他控件的列表, 以便 NVDA 不会在空列表中朗读 "未知"。
- 如果无法显示文章对话框列表 (例如, RSS的摘要有错误), 直接报错, 这样可以在不重新启动 NVDA 的情况下继续使用RSS源对话框。

## 版本6.0

- 当默认RSS源已更新并且由于服务器问题而停止工作时，之前的文章不会被删除，并且可以使用相应的按键进行读取。
- Fix regression: The default feed can be updated twice again.

## Changes for 15.0

- 文章列表对话框已得到增强。
- 兼容NVDA 2018.3或更高版本（必需）。
- If needed, you can download the [last version compatible with NVDA 2017.3][3].

## Changes for 14.0

- 添加了一个按钮，可以从“源”对话框中打开所选的源。

## Changes for 13.0

- The dialogs to manage feed files have been removed. Now their functionality is included in the Feeds dialog.
- 对话框的可视化表示已得到增强，符合NVDA中显示的对话框的外观。
- 默认配置保存在NVDA的配置中。因此，可以在配置配置文件中设置不同的默认源。 Therefore, it's possible to set different default feeds in configuration profiles.
- 需要NVDA 2016.4。

## Changes for 21.0

- 插件管理器提供了插件帮助。

## 版本1.0

- 发布初始版本。

[1]: http://addons.nvda-project.org/files/get.php?file=rf
[2]: http://addons.nvda-project.org/files/get.php?file=rf-dev
[3]: http://addons.nvda-project.org/files/get.php?file=rf-o
