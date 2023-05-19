# Read Feeds-NVDA-RSS阅读插件 #

* 作者: Noelia Ruiz Martínez, Mesar Hameed
* Download [stable version][1] (compatible with NVDA 2019.3 and beyond)
* Download [beta version][2] (compatible with NVDA 2019.3 and beyond)

此插件提供了一种使用NVDA以Atom或RSS格式读取订阅源的简单方法。 Feed不会自动刷新。下面我们提到feed时，我们指的是RSS和ATOM提要。

## 快捷键 ##

### Read Feeds dialog ###

You can access the Read Feeds dialog from the nvda menu, Tools submenu,
Feeds item.

It contains the following controls:

* 过滤条件：用于搜索以前保存的feed的编辑框。
* 已保存的Feeds列表，在对话框打开时集中显示。
* 文章列表：打开一个对话框，显示当前Feed中的文章列表。选择要阅读的文章，然后按Enter或打开所选文章的网页按钮，在浏览器中打开相应的页面。按关于文章按钮打开一个对话框，显示所选文章的标题和链接;在此对话框中，您将能够将此信息复制到剪贴板。
* 打开feed：在默认应用程序中打开所选feed。
* 以HTML格式打开Feed。在默认的网络浏览器中打开选定的feed。您将能够显示或隐藏出版日期和按钮来复制文章信息到剪贴板。
* 复制馈送地址。打开一个对话框，确认是否要将feed地址复制到剪贴板。
* 新建：打开带有编辑框的对话框，以输入新Feed的地址。如果地址有效且可以保存Feed，则其名称（基于Feed标题）将显示在Feed列表的底部。
* 重命名：打开一个带有编辑框的对话框，以重命名所选的源。
* 删除：打开确认后删除所选feed的对话框。
* 设置默认值：将选定的Feed设置为默认值，以便可以使用NVDA的快捷键访问其文章。
* Import feeds from OPML file: Opens a dialog to add new feeds from an OPML
  file.
* Save feeds to OPML file: Opens a dialog to save the feeds available from
  the Feeds dialog in an OPML file.
* 首选项。打开readFeeds的设置对话框，也可在NVDA的菜单 "首选项"、"设置"、"readFeeds "类别中使用。
* 关闭：关闭“源”对话框。

### Notes #####

* 通过编辑框过滤可以放在NVDA的菜单、首选项、设置、读取feeds类别的打开文章按钮之后，或者按Feeds对话框的首选项按钮。
* This panel has an option to show article dates on the List of articles
  dialog.


### 键盘快捷键 ###

* Ctrl + Shift + NVDA + Space：朗读当前文章的URL。按两次将打开网页。
* Ctrl + Shift + NVDA + 8：刷新选定的Feed并朗读其最新的标题。
* Ctrl + Shift + NVDA + I：朗读当前RSS源的标题和链接。按两次将标题和相关链接复制到剪贴板。
* Ctrl + Shift + NVDA + U：朗读当前源的上一个的标题。
* Ctrl + Shift + NVDA + O：朗读当前源的下一个标题。

## 通知 ##

* 复制标题或URL时。
* 无法连接/刷新Feed时，或者URL与有效Feed不对应。
* NVDA will display an error message if a new feed cannot be created.
* “文章列表”对话框的标题显示所选的源名称和可用项目数。

## Changes for 21.0

* Feeds with untitled articles can be presented in the Articles dialog, and
  opened as HTML.

## Changes for 20.0

* universalFeedParser is updated to 5.0.1, adding support for more feeds.

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

## 版本12.0

* 修复了导致 NVDA 工具菜单项的快捷方式无法按预期工作的错误。

## 版本11.0

* 兼容 NVDA 2021.1

## 版本10.0更新日志 ##

* 增加了一个按钮，在默认的网页浏览器中以HTML形式打开选定的feed。
* 如果不能创建新的feed，将在错误对话框中通知。
* 改进一些条款的顺序和表述方式。
* 可以支持更多的feed。
* 当打开Feeds对话框时，Feeds列表将被关注，而不是搜索编辑框。
* 您可以选择是否将搜索编辑框放在Feeds列表之后，这对于在不关闭Feeds对话框的情况下从另一个窗口切换时聚焦列表非常有用。
* 在feeds对话框中添加了将feed地址复制到剪贴板的按钮。

## 版本9.0 ##

* 需要NVDA 2019.3或更高版本。

## 版本8.0 ##

* 更新插件后，除非您更喜欢导入保存在NVDA主配置文件夹中的feed，否则将保存在以前版本的插件中的提要将自动复制到新版本。
* 使用对话框复制供稿时，如果所选文件夹未命名为personalFeeds，则将创建具有此名称的子文件夹，以防止删除包含重要数据的目录，例如“文档”或“下载”。

## 版本7.0 ##

* "源" 对话框中包含一个按钮, 用于打开可能包含源备份的文件夹。
* 使用编辑框筛选源时, 如果未找到任何结果, 则会禁用源和其他控件的列表, 以便 NVDA 不会在空列表中朗读 "未知"。
* 如果无法显示文章对话框列表 (例如, RSS的摘要有错误), 直接报错, 这样可以在不重新启动 NVDA 的情况下继续使用RSS源对话框。

## 版本6.0 ##

* 当默认RSS源已更新并且由于服务器问题而停止工作时，之前的文章不会被删除，并且可以使用相应的按键进行读取。
* 修复错误：默认RSS源可以更新两次了。

## 版本5.0 ##

* 文章列表对话框已得到增强。
* 兼容NVDA 2018.3或更高版本（必需）。
* 如果需要，您可以下载[与NVDA 2017.3兼容的最新版本] [3]。

## 版本4.0 ##

* 添加了一个按钮，可以从“源”对话框中打开所选的源。

## 版本3.0 ##

* 管理订阅源文件的对话框已被删除。现在，他们的功能包含在“源”对话框中。
* 对话框的可视化表示已得到增强，符合NVDA中显示的对话框的外观。
* 默认配置保存在NVDA的配置中。因此，可以在配置配置文件中设置不同的默认源。
* 需要NVDA 2016.4。

## 版本2.0 ##

* 插件管理器提供了插件帮助。

## 版本1.0 ##

* 发布初始版本。

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=readFeeds

[2]: https://www.nvaccess.org/addonStore/legacy?file=readFeeds-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=rf-o
