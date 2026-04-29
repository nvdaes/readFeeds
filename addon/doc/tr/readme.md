# Akışları Oku

- Yazarlar: Noelia Ruiz Martínez, Mesar Hameed
- NVDA 2023.1 ile uyumlu.
- Download [stable version][1]
- Download [development version][2]

Bu eklenti NVDA kullanarak Atom veya RSS formatında beslemeleri okumak için
basit bir yol sunar.
Beslemeler otomatik olarak yenilenmez.
Aşağıda besleme
derken hem RSS hem de ATOM beslemelerini kastediyoruz.

## Installation or Update:

If you used a previous version of this addon, and there is an RSS or personalFeeds folder in your personal NVDA configuration folder,
when installing the current version, a dialog will ask if you want to upgrade or install.
Choose update to preserve your saved feeds and to continue using them in the new installed version of readFeeds.

## Commands:

### Read Feeds menu

Akışları Oku iletişim kutusuna nvda menüsü, Araçlar alt menüsü, akış listesi
öğesinden erişebilirsiniz.

#### Feeds...

Opens a dialog with the following controls:

- Filtreleme kriteri: Önceden kaydedilmiş beslemeleri aramak için bir
  düzenleme kutusu.
- A list of the saved feeds.
- Makale listesi: Mevcut beslemenizdeki makalelerin listesini sunan bir
  iletişim kutusu açar. Okumak istediğiniz makaleyi seçin ve ilgili sayfayı
  tarayıcınızda açmak için Enter veya Seçilen makalenin web sayfasını aç
  düğmesine basın. Seçilen makalenin başlığını ve bağlantısını gösteren bir
  iletişim kutusu açmak için Makale hakkında düğmesine basın; bu iletişim
  kutusundan, bu bilgiyi panoya kopyalayabilirsiniz.
- Akışı aç: Seçili akışı varsayılan uygulamada açar.
- Yeni: Yeni bir beslemenin adresini girmek için bir düzenleme kutusu içeren
  bir iletişim kutusu açar. Adres geçerliyse ve yayın kaydedilebilirse,
  yayın başlığına göre adı, yayın listesinin içinde görünecektir.
- Yeniden Adlandır: Seçili akışı yeniden adlandırmak için bir düzenleme
  kutusu içeren bir iletişim kutusu açar.
- Sil: Onaydan sonra seçilen akışın silinmesi için bir iletişim kutusu açar.
- Varsayılan olarak ayarla: Seçilen beslemeyi varsayılan olarak ayarlar,
  böylece makalelerine ilgili NVDA girdi hareketleriyle erişilebilir.
- Open folder containing a backup of feeds: Opens a folder which may contain a backup of feeds. This can be useful to explore and delete feeds which shouldn't be imported when the add-on is updated.
- Kapat: Akışlar iletişim kutusunu kapatır.

##### Notlar

- If a feed named tempFeed is created, please rename it, as this file could be replaced when needed to create a feed whose name already exists.
- The feed set as the default can't be removed. The addressFile feed will be use as the default when the configuration is reset, so it can't be deleted.

\####Copy feeds folder... ####

Opens a dialog to choose a folder where you can save the personalFeeds directory of your feeds. By default the selected folder is the NVDA's configuration directory, which will create the personalFeeds directory.

#### Restore feeds...

Opens a dialog to select a folder which replaces your feeds in the personalFeeds folder. Make sure you load a folder containing feeds URLs.

### Klavye komutları

- Ctrl+Shift+NVDA+Space: Mevcut makalenin URL'sini duyurur. İki kez basmak
  web sayfasını açacaktır.
- Ctrl+Shift+NVDA+8: Seçili akışı yeniler ve en son başlığı duyurur.
- Ctrl+Shift+NVDA+I: Mevcut akış başlığını ve bağlantısını duyurur. İki kez
  basmak, başlığı ve ilgili bağlantıyı panoya kopyalayacaktır.
- Ctrl+Shift+NVDA+U: Önceki akış başlığını duyurur.
- Ctrl+Shift+NVDA+O: Sonraki akış başlığını duyurur.

## Notifications:

- Başlık veya URL kopyalandığında.
- Bir akışa bağlanılamadığında/yenileme yapılamadığında veya URL, geçerli
  bir akışa karşılık gelmediğinde.
- NVDA will display an error message if it was not possible to backup or restore the personalFeeds folder.
- Makale listesi iletişim kutusunun başlığı, seçilen akış adını ve mevcut
  öğelerin sayısını gösterir.

## 8.0 İçin değişiklikler

- Eklenti güncellendiğinde, NVDA'nın ana yapılandırma klasörüne kaydedilen
  beslemeleri içe aktarmayı tercih etmediğiniz sürece, eklentinin önceki
  sürümünde kaydedilen beslemeler otomatik olarak yeni sürüme
  kopyalanacaktır.
- Akışları kopyalamak için iletişim kutusunu kullanırken, seçilen klasörün
  adı personalFeeds değilse, Belgeler veya İndirilenler gibi önemli verileri
  içeren dizinlerin silinmesini önlemek için bu ada sahip bir alt klasör
  oluşturulacaktır.

## 7.0 İçin değişiklikler

- Akışlar iletişim kutusu, akışların yedeğini içerebilecek bir klasörü açmak
  için bir düğme içerir.
- Yayınları filtrelemek için düzenleme kutusunu kullanırken, hiçbir sonuç
  bulunmazsa, yayınların listesi ve diğer kontroller devre dışı bırakılır,
  böylece NVDA boş listede "bilinmeyen" demez.
- Makaleler listesi iletişim kutusu, örneğin beslemedeki hatalar nedeniyle
  gösterilemiyorsa, NVDA bir hata oluşturur, böylece beslemeler iletişim
  kutusu NVDA'yı yeniden başlatmadan kullanılabilir.

## 6.0 İçin değişiklikler

- Varsayılan besleme güncellendiğinde ve sunucu sorunları nedeniyle
  çalışmayı durdurduğunda, önceki makaleler silinmez ve ilgili tuşlarla
  okunabilir.
- Gerileme düzeltmesi: Varsayılan besleme iki kez tekrar güncellenebilir.

## 5.0 İçin değişiklikler

- Makaleler listesi iletişim kutusu geliştirildi.
- NVDA 2018.3 veya üstü ile uyumlu (gerekli).
- If needed, you can download the [last version compatible with NVDA 2017.3][3].

## 4.0 İçin değişiklikler

- Akışlar iletişim kutusundan seçilen akışı açmak için bir düğme eklendi.

## 3.0 İçin değişiklikler

- Akış dosyalarını yönetmek için kullanılan iletişim kutuları
  kaldırıldı. Artık işlevleri akışlar iletişim kutusuna dahil edildi.
- NVDA'da gösterilen iletişim kutularının görünümüne bağlı kalınarak
  iletişim kutularının görsel sunumu geliştirildi.
- Varsayılan akış, NVDA'nın yapılandırmasına kaydedilir. Dolayısıyla,
  yapılandırma profillerinde farklı varsayılan akışlar ayarlamak mümkündür.
- NVDA 2016.4 gerektirir.

## 2.0 için Değişiklikler

- Eklenti yardımına, Eklenti Yöneticisi'nden ulaşılabilir.

## 1.0 İçin değişiklikler

- İlk sürüm.

[1]: http://addons.nvda-project.org/files/get.php?file=rf
[2]: http://addons.nvda-project.org/files/get.php?file=rf-dev
[3]: http://addons.nvda-project.org/files/get.php?file=rf-o
