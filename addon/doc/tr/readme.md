# RSS Akışlarını Oku #

* Yazarlar: Noelia Ruiz Martínez, Mesar Hameed
* İndir [kararlı sürüm][2]
* İndir [geliştirme sürümü][1]

Bu eklenti NVDA kullanarak Atom veya RSS formatında beslemeleri okumak için
basit bir yol sunar. Beslemeler otomatik olarak yenilenmez. Aşağıda besleme
derken hem RSS hem de ATOM beslemelerini kastediyoruz.

## Kurulum veya Güncelleme: ##

Bu eklentinin önceki bir sürümünü kullanıyorsanız ve kişisel NVDA
konfigürasyon klasöründe bir RSS veya personalFeeds adlı klasör varsa,
eklentinin 6.0 sürümünden itibaren güncellemek mi yoksa kurmak mı
istediğiniz sorulacaktır. Önceki RSS akışlarınızı kullanmaya devam etmek
istiyorsanız Güncelle seçeneğiyle devam edin.

## Komutlar: ##

### RSS Okuma menüsü ###

RSS Okuma alt menüsüne NVDA+N ile açılan nvda menüsünden ulaşabilir,  bu
menüde aşağıdaki menü seçeneklerini bulabilirsiniz:

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

### Klavye komutları: ###

- Ctrl+Shift+NVDA+Aralık: Mevcut haberin adresini seslendirir. İki kez
basılırsa haberle ilgili web sayfası açılır.  - Ctrl+Shift+NVDA+8: Seçilen
akış güncellenir ve en son girilen haber başlığı okunur.  -
Ctrl+Shift+NVDA+I: Geçerli haber başlığını okur. İki kez basılırsa başlık ve
adres panoya kopyalanır.  - Ctrl+Shift+NVDA+U: Önceki haber başlığını okur.
- Ctrl+Shift+NVDA+O: Sonraki haber başlığını okur.

## Bildirimler: ##

- Başlık ya da adres kopyalandığında.  - Akışa bağlanalamıyor ya da
güncellenemiyorsa ve geçerli bir adres değilse.  - Nvda, kişisel akış
klasörü yedeklenemediğinde hata verir.  - Haber listesi iletişim kutusunun
başlığında geçerli akışın adı ve geçerli haber sayısı bulunur.

## Changes for 2.0 ##
*	 Add-on help is available from the Add-ons Manager.

## 1.0 Değişiklikler ##
*	 İlk sürüm.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf-dev

[2]: http://addons.nvda-project.org/files/get.php?file=rf

