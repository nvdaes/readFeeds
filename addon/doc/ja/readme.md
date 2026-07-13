# Read Feeds

- Authors: Noelia Ruiz Martínez, Mesar Hameed
- NVDA 2019.3以降が必要。
- Download [stable version][1]
- Download [development version][2]

This addon provides a straightforward  way to read feeds in Atom or RSS formats using NVDA.
The feeds will not be refreshed automatically.
Below when we mention feeds, we mean both RSS and ATOM feeds.

## Installation or Update:

If you used a previous version of this addon, and there is an RSS or personalFeeds folder in your personal NVDA configuration folder,
when installing the current version, a dialog will ask if you want to upgrade or install.
Choose update to preserve your saved feeds and to continue using them in the new installed version of readFeeds.

## コマンド

### Read Feeds ダイアログ

Read Feedsダイアログにnvdaメニュー、ツールサブメニュー、Feeds項目からアクセス出来ます。

#### Feeds...

次のコントロールを含みます:

- ～でフィルター: 以前に保存したフィードを検索するエディットボックス。
- A list of the saved feeds.
- List of articles: Opens a dialog which presents the articles list from your current feed. Select the article you want to read and press Enter or Open web page of selected article button to open the corresponding page in your browser. Press About article button to open a dialog showing title and link of the selected article; from this dialog, you'll be able to copy this info to the clipboard.
- フィードを開く: 選択したフィードを既定のアプリケーションで開きます。
- New: Opens a dialog with an edit box to enter the address of a new feed. If the address is valid and the feed can be saved, its name, based on the feed title, will appear at the bottom of the feeds list.
- 名前を変更: 選択されたフィードの名前を変更するエディットボックスのあるダイアログを開きます。
- 削除: 確認後に選択されたフィードを削除するダイアログが開きます。
- 初期状態に設定: 選択されたフィードを初期状態に設定し、NVDAのジェスチャーでその記事にアクセス出来るようにします。
- Open folder containing a backup of feeds: Opens a folder which may contain a backup of feeds. This can be useful to explore and delete feeds which shouldn't be imported when the add-on is updated.
- 閉じる: Feedsダイアログを閉じます。

##### 備考

- If a feed named tempFeed is created, please rename it, as this file could be replaced when needed to create a feed whose name already exists.
- The feed set as the default can't be removed. The addressFile feed will be use as the default when the configuration is reset, so it can't be deleted.

\####Copy feeds folder... ####

Opens a dialog to choose a folder where you can save the personalFeeds directory of your feeds. By default the selected folder is the NVDA's configuration directory, which will create the personalFeeds directory.

#### Restore feeds...

Opens a dialog to select a folder which replaces your feeds in the personalFeeds folder. Make sure you load a folder containing feeds URLs.

### キーボードコマンド

- Ctrl+Shift+NVDA+Space: 現在の記事のURLを通知。2回押してそのウェブページを開く。 Pressing twice will open the web page.
- Ctrl+Shift+NVDA+8: 選択されたフィードを再読み込みして、その最新のタイトルを通知。
- Ctrl+Shift+NVDA+I:現在のフィードのタイトルとリンクを通知。2回押してそのタイトルと関連リンクをクリップボードにコピー。 Pressing twice will copy the title and related link to clipboard.
- Ctrl+Shift+NVDA+U: 前のフィードタイトルを通知。
- Ctrl+Shift+NVDA+O: 次のフィードタイトルを通知。

## 通知

- タイトルまたはURLがコピーされた時。
- フィードに接続/再読み込み出来ない時、または、URLが有効なフィードに応答しない時。
- NVDA will display an error message if it was not possible to backup or restore the personalFeeds folder.
- 記事リストダイアログのタイトルは、選択されたフィードの名前と、利用可能な項目の数を表示します。

## 8.0の変更点

- NVDAのメインの設定フォルダに保存されたフィードをインポートするのを好む場合を除き、アドオンが更新される時、前のバージョンで保存されたフィードは、自動的に新しいバージョンにコピーされます。
- フィードをコピーするのにダイアログを使用する時、選択されたフォルダがpersonalFeedsという名前でない場合、ドキュメントやダウンロードといった、重要なデータを含むディレクトリの削除を避けるため、その名前のサブフォルダが作成されるようになりました。

## 7.0の変更点

- フィードダイアログが、フィードのバックアップを含むフォルダーを開くボタンを、含むようになりました。
- フィードをフィルターするのにエディットボックスを使用する時、結果が見つからない場合、NVDAが空のリストに「未知の物」と通知しないように、フィードのリストと他のコントロールが無効化されるようになりました。
- 例えばフィードのエラーにより、記事のリストダイアログが表示されなかった時、フィードダイアログがNVDAの再起動をしなくても使用出来るように、NVDAはエラーを表示するようになりました。

## 6.0の変更点

- 初期設定のフィードが更新され、サーバーの問題で動作が停止した時、前の記事が削除されず、対応するキーストロークで読めるようになりました。
- 再発バグの修正: 初期のフィードを2回更新可能に再びなりました。

## 5.0の変更点

- 記事リストダイアログが拡張されました。
- NVDA 2018.3以降に互換(必要)
- Compatible with NVDA 2023.1.

## 4.0の変更点

- フィードダイアログから選択されたフィードを開くボタンを追加しました。

## 3.0の変更点

- フィードファイルを管理するダイアログが除去されました。それらの機能はフィードダイアログに含まれるようになりました。 Now their functionality is included in the Feeds dialog.
- ダイアログの外観が、NVDAに表示されるダイアログの外観に従って、拡張されました。
- 初期設定のフィードはNVDAの設定に保存されます。よって、異なる初期設定のフィードは設定プロファイルに設定することが出来ます。 Therefore, it's possible to set different default feeds in configuration profiles.
- NVDA 2016.4が必要。

## 2.0の変更点

- アドオンヘルプはアドオンマネージャから利用可能になりました。

## 1.0の変更点

- 最初のバージョン。

[1]: http://addons.nvda-project.org/files/get.php?file=rf
[2]: http://addons.nvda-project.org/files/get.php?file=rf-dev
[3]: http://addons.nvda-project.org/files/get.php?file=rf-o
