# Read Feeds #

* مطورو الإضافة: Noelia Ruiz Martínez, Mesar Hameed
* تحميل [الإصدار النهائي][2]
* تحميل [الإصدار التجريبي][1]

تعمل هذه الإضافة على تزويدنا بطريقة سهلة وبسيطة لقراءة التلقيمات بصيغة آتوم
أو آرإسإس باستخدام NVDA. لم يتم تنشيط التلقيمات آليا. في كل مرة نذكر فيها
كلمة تلقيمات, فإننا نعني بها التلقيمات بكل من الصغيتين آرإسإس وآتوم.

## تثبيت أو تحديث: ##

إذا كنت تستخدم إصدار أقدم من هذه الإضافة, ويوجد بملف إعدادات NVDA الخاص بك
مجلد للتلقيمات الشخصية أو تلقيمات آرإسإس, فعند تثبيت الإصدار 6.0 من هذه
الإضافة وما بعده, ستظهر محاورة تسألك عما إذا كنت تريد الترقية أو
التثبيت. اختر الأمر تحديث كي تحتفظ بالتلقيمات التي قمت بحفظها من قبل وكي
تستطيع الاستمرار في استخدامها بعد تثبيت الإصدار الجديد.

## الاختصارات: ##

### قائمة Read Feeds ###

يمكنك الوصول إلى القائمة الفرعية Read Feeds من قائمة NVDA الرئيسية, NVDA+N,
وتوجد بها الخيارات التالية:

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

### مفاتيح الاختصار: ###

- Ctrl+Shift+NVDA+Space: الإعلان عن رابط المقال الحالي. بالضغط عليه مرتين
سيفتح الصفحة المنشور بها المقال.  - Ctrl+Shift+NVDA+8: تنشيط التلقيم المحدد
والإعلان عن أحدث عنوان له.  - Ctrl+Shift+NVDA+I: الإعلان عن عنوان التلقيم
الحالي. بالضغط عليه مرتين سينسخ العنوان ورابط التلقيم للحافظة.  -
Ctrl+Shift+NVDA+U: الإعلان عن عنوان التلقيم السابق.  - Ctrl+Shift+NVDA+O:
الإعلان عن عنوان التلقيم التالي. 

## إشعارات: ##

عند نسخ العنوان أو الرابط.  - عند تعذر الاتصال ب/تنشيط تلقيم, أو الرابط غير
متعلق بتلقيم صحيح.  - سيقوم NVDA بعرض رسالة خطأ إذا تعذر أخذ نسخة احطياطية
من مجلد التلقيمات الشخصية.  - ستقوم محاورة عنوان قائمة المقالات بعرض اسم
التلقيم المحدد وعدد العناصر المتاحة.

## Changes for 2.0 ##
*	 Add-on help is available from the Add-ons Manager.

## تعديلات الإصدار 1.0 ##
*	 إصدار أولي

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf-dev

[2]: http://addons.nvda-project.org/files/get.php?file=rf

