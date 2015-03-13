# Read Feeds #

* 作者: Noelia Ruiz Martínez, Mesar Hameed
* ダウンロード [安定版][2]
* ダウンロード [開発版][1]

このアドオンはNVDAを使用してATOMやRSSの形式のフィードを簡単に読むためのものです。フィードは自動的に更新されることはありません。以下でフィードとはRSSとATOMの両方を形式を含んでいます。

## インストールと更新: ##

このアドオンの以前のバージョンを使用していて、個人用NVDA設定フォルダにRSSまたはpersonalFeedsフォルダがある場合は、readFeedsアドオンのバージョン6.0以上をインストールするときにアップグレードとインストールを選択するダイアログが表示されます。アップデートを選ぶと保存したフィードを残すことができ、新しいバージョンのreadFeedsで引き続き利用できます。

## コマンド: ##

### Read Feeds メニュー ###

NVDAメニュー(NVDA+N)から Reed Feeds サブメニューを使用できます。以下のオプションがあります:

-Article list...現在のフィードから記事リストを表示します。読みたい記事を選択してOKボタンを押し、ブラウザで対応するページを開きます。
-Temporary feed address...Ctrl+NVDA+Shift+Enter:
ダイアログを開いて新しいURLを入力して他のフィードを選択します。現在のURLがこのダイアログに表示されます。
-Load feed address from file...NVDA+Ctrl+Enter:
ダイアログを開いて、フィードURLが保存されたファイルからフィードを選択します。
-Save current feed address to file...NVDA+Shift+Enter:
ダイアログを開いて現在のフィードURLを保存するファイルを選択します。addressFile.txtに保存すると、このファイルに保存されたフィードが最初のフィードとして使用されます。
-Refresh current feed: Ctrl+Shift+NVDA+8: 選択されたフィードを更新します。フィードは、Read Feeds
アドオンを起動時に自動的に更新されません。
-Backup feeds
folder...ダイアログを開いて自分のフィードを保存する個人フィードディレクトリを保存するフォルダを選択します。初期設定では、NVDAの設定ディレクトリ(configuration
directory)がフォルダとして選択され、個人フィードディレクトリが作成されます。
-Restore
feeds...ダイアログを開き個人フィードフォルダ内のフィードを入れ替えるフォルダを選択します。フィードURLが保存されたフォルダを読み込むようにします。

注: 以前に保存したフィードURLを削除したい場合は、対応するファイルを削除します。

### キーボードコマンド: ###

-Ctrl+Shift+NVDA+Space: 現在の記事のURLを通知します。2回押すとそのウェブページを開きます。
-Ctrl+Shift+NVDA+8: 選択されたフィードを更新して最新のタイトルを通知します。
-Ctrl+Shift+NVDA+I: 現在のフィードのタイトルを通知します。2回押すとそのタイトルとリンクをクリップボードにコピーします。
-Ctrl+Shift+NVDA+U: 前のフィードのタイトルを通知します。
-Ctrl+Shift+NVDA+O: 次のフィードのタイトルを通知します。

## 通知: ##

-タイトルまたはURLがコピーされた時。
-フィードを接続更新できない時、またはURLが有効なフィードに対応しない時。
-個人フィードフォルダをバックアップできない時、NVDAはエラーメッセージを表示します。
-記事リストダイアログのタイトルは選択されたフィード名および使用できる項目数を表示します。

## 2.0の変更点 ##
*	 アドオン ヘルプはアドオン マネージャから利用可能になりました

## バージョン1.0 ##
*	 最初のバージョン

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf-dev

[2]: http://addons.nvda-project.org/files/get.php?file=rf

