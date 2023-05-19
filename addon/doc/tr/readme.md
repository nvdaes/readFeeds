# RSS Akışlarını Oku #

* Yazarlar: Noelia Ruiz Martínez, Mesar Hameed
* Download [stable version][1] (compatible with NVDA 2019.3 and beyond)
* Download [beta version][2] (compatible with NVDA 2019.3 and beyond)

Bu eklenti NVDA kullanarak Atom veya RSS formatında beslemeleri okumak için
basit bir yol sunar. Beslemeler otomatik olarak yenilenmez. Aşağıda besleme
derken hem RSS hem de ATOM beslemelerini kastediyoruz.

## Komutlar ##

### Akışları Oku iletişim kutusu ###

Akışları Oku iletişim kutusuna nvda menüsü, Araçlar alt menüsü, akış listesi
öğesinden erişebilirsiniz.

Aşağıdaki kontrolleri içerir:

* Filtreleme kriteri: Önceden kaydedilmiş beslemeleri aramak için bir
  düzenleme kutusu.
* İletişim kutusu açıldığında odaklanılan kayıtlı akışların listesi.
* Makale listesi: Mevcut beslemenizdeki makalelerin listesini sunan bir
  iletişim kutusu açar. Okumak istediğiniz makaleyi seçin ve ilgili sayfayı
  tarayıcınızda açmak için Enter veya Seçilen makalenin web sayfasını aç
  düğmesine basın. Seçilen makalenin başlığını ve bağlantısını gösteren bir
  iletişim kutusu açmak için Makale hakkında düğmesine basın; bu iletişim
  kutusundan, bu bilgiyi panoya kopyalayabilirsiniz.
* Akışı aç: Seçili akışı varsayılan uygulamada açar.
* Akışı HTML olarak aç: Seçili akışı varsayılan web tarayıcısında
  açar. Makaleler hakkındaki bilgileri panoya kopyalamak için yayın
  tarihlerini ve düğmeleri gösterip gizleyebileceksiniz.
* Akış adresini kopyala: Akış adresini panoya kopyalamak isteyip
  istemediğinizi onaylamak için bir iletişim kutusu açar.
* Yeni: Yeni bir beslemenin adresini girmek için bir düzenleme kutusu içeren
  bir iletişim kutusu açar. Adres geçerliyse ve yayın kaydedilebilirse,
  yayın başlığına göre adı, yayın listesinin içinde görünecektir.
* Yeniden Adlandır: Seçili akışı yeniden adlandırmak için bir düzenleme
  kutusu içeren bir iletişim kutusu açar.
* Sil: Onaydan sonra seçilen akışın silinmesi için bir iletişim kutusu açar.
* Varsayılan olarak ayarla: Seçilen beslemeyi varsayılan olarak ayarlar,
  böylece makalelerine ilgili NVDA girdi hareketleriyle erişilebilir.
* OPML dosyasından akışları içe aktar: Bir OPML dosyasından yeni akışlar
  eklemek için bir iletişim kutusu açar.
* Akışları OPML dosyasına kaydet: Akışlar iletişim kutusunda bulunan
  beslemeleri bir OPML dosyasına kaydetmek için bir iletişim kutusu açar.
* Tercihler: NVDA menüsünde Tercihler, ayarlar, Akışları oku kategorisinde
  de bulunan akışları oku için ayarlar diyalog penceresini açar.
* Kapat: Akışlar iletişim kutusunu kapatır.

### Notlar #####

* Filtreye göre düzenleme kutusu NVDA menüsünden Tercihler, Ayarlar,
  Akışları oku kategorisinden veya akışlar iletişim kutusundaki Tercihler
  düğmesine basarak Makaleyi aç düğmesinden sonra yerleştirilebilir.
* Bu panel, Makalelerin listesi iletişim kutusunda makale tarihlerini
  gösterme seçeneğine sahiptir.


### Klavye komutları ###

* Ctrl+Shift+NVDA+Space: Mevcut makalenin URL'sini duyurur. İki kez basmak
  web sayfasını açacaktır.
* Ctrl+Shift+NVDA+8: Seçili akışı yeniler ve en son başlığı duyurur.
* Ctrl+Shift+NVDA+I: Mevcut akış başlığını ve bağlantısını duyurur. İki kez
  basmak, başlığı ve ilgili bağlantıyı panoya kopyalayacaktır.
* Ctrl+Shift+NVDA+U: Önceki akış başlığını duyurur.
* Ctrl+Shift+NVDA+O: Sonraki akış başlığını duyurur.

## Bildirimler ##

* Başlık veya URL kopyalandığında.
* Bir akışa bağlanılamadığında/yenileme yapılamadığında veya URL, geçerli
  bir akışa karşılık gelmediğinde.
* Yeni bir akış oluşturulamıyorsa NVDA bir hata mesajı görüntüler.
* Makale listesi iletişim kutusunun başlığı, seçilen akış adını ve mevcut
  öğelerin sayısını gösterir.

## Changes for 21.0

* Feeds with untitled articles can be presented in the Articles dialog, and
  opened as HTML.

## Changes for 20.0

* universalFeedParser is updated to 5.0.1, adding support for more feeds.

## Changes for 14.0

* Fixed a bug that made impossible to add some feeds.

## 13.0 için  Değişiklikler

* Eklenti, güvenli ekranlarda kullanılamaz.
* Yayınlar, OPML dosyalarından yönetilir.
* Akış yönetim sistemindeki değişiklikler nedeniyle, varsayılan akışın
  ayarlandığı yapılandırma dosyasında değişiklikler vardır. Tekrar ayarlamak
  istiyorsanız lütfen akışlar iletişim kutusunu kullanın.
* Önceki sürümlerde kullanılan eski metin dosyalarınız, eklenti
  başlatıldığında otomatik olarak yeni OPML biçimine aktarılacaktır.
* Akışları kopyala ve geri yükle özelliği, OPML dosyalarından içe aktarma ve
  kaydetme özelliğiyle değiştirildi.
* İyi biçimlendirilmemiş akış adresleri  , eklentiyle uyumlu hale
  getirilmeleri için eklenmeden önce işlenebilir.
* Akışları oku ayarları panelinde yeni bir seçenek, makale tarihlerinin
  Makale listesi iletişim kutusunda gösterilmesine olanak tanır.

## 12.0 için Değişiklikler

* NVDA'nın araçlar menüsündeki öğeler için kısayolların beklendiği gibi
  çalışmamasına neden olan bir hata düzeltildi.

## 11.0 için değişiklikler

* NVDA 2021.1 ile uyumlu

## 10.0 için Değişiklikler ##

* Varsayılan web tarayıcısında seçilen akışı HTML olarak açmak için bir
  düğme eklendi.
* Yeni bir akış oluşturulamıyorsa, bu durum bir hata iletişim kutusunda
  bildirilecektir.
* Bazı makalelerin düzeni ve sunumunda iyileştirme.
* Daha fazla akış desteklenebilir.
* Akışlar iletişim kutusu açıldığında, arama düzenleme kutusu yerine
  yayınların listesine odaklanılacaktır.
* Arama düzenleme kutusunun akış listesinden sonra yerleştirilip
  yerleştirilmeyeceğini seçebilirsiniz; bu, akışlar iletişim kutusunu
  kapatmadan başka bir pencereden geçiş yaparken bile listeye odaklanmak
  için yararlı olabilir.
* Akış iletişim kutusundan akış adresini panoya kopyalamak için bir düğme
  eklendi.

## 9.0 için Değişiklikler ##

* NVDA 2019.3 veya sonraki bir sürümünü gerektirir.

## 8.0 için Değişiklikler ##

* Eklenti güncellendiğinde, NVDA'nın ana yapılandırma klasörüne kaydedilen
  beslemeleri içe aktarmayı tercih etmediğiniz sürece, eklentinin önceki
  sürümünde kaydedilen beslemeler otomatik olarak yeni sürüme
  kopyalanacaktır.
* Akışları kopyalamak için iletişim kutusunu kullanırken, seçilen klasörün
  adı personalFeeds değilse, Belgeler veya İndirilenler gibi önemli verileri
  içeren dizinlerin silinmesini önlemek için bu ada sahip bir alt klasör
  oluşturulacaktır.

## 7.0 için Değişiklikler ##

* Akışlar iletişim kutusu, akışların yedeğini içerebilecek bir klasörü açmak
  için bir düğme içerir.
* Yayınları filtrelemek için düzenleme kutusunu kullanırken, hiçbir sonuç
  bulunmazsa, yayınların listesi ve diğer kontroller devre dışı bırakılır,
  böylece NVDA boş listede "bilinmeyen" demez.
* Makaleler listesi iletişim kutusu, örneğin beslemedeki hatalar nedeniyle
  gösterilemiyorsa, NVDA bir hata oluşturur, böylece beslemeler iletişim
  kutusu NVDA'yı yeniden başlatmadan kullanılabilir.

## 6.0 için Değişiklikler ##

* Varsayılan besleme güncellendiğinde ve sunucu sorunları nedeniyle
  çalışmayı durdurduğunda, önceki makaleler silinmez ve ilgili tuşlarla
  okunabilir.
* Gerileme düzeltmesi: Varsayılan besleme iki kez tekrar güncellenebilir.

## 5.0 için Değişiklikler ##

* Makaleler listesi iletişim kutusu geliştirildi.
* NVDA 2018.3 veya üstü ile uyumlu (gerekli).
* Gerekirse [NVDA 2017.3 ile uyumlu son sürüm][3]ü indirebilirsiniz.

## 4.0 için Değişiklikler ##

* Akışlar iletişim kutusundan seçilen akışı açmak için bir düğme eklendi.

## 3.0 için Değişiklikler ##

* Akış dosyalarını yönetmek için kullanılan iletişim kutuları
  kaldırıldı. Artık işlevleri akışlar iletişim kutusuna dahil edildi.
* NVDA'da gösterilen iletişim kutularının görünümüne bağlı kalınarak
  iletişim kutularının görsel sunumu geliştirildi.
* Varsayılan akış, NVDA'nın yapılandırmasına kaydedilir. Dolayısıyla,
  yapılandırma profillerinde farklı varsayılan akışlar ayarlamak mümkündür.
* NVDA 2016.4 gerektirir.

## 2.0 için Değişiklikler ##

* Eklenti yardımına, Eklenti Yöneticisi'nden ulaşılabilir.

## 1.0 Değişiklikler ##

* İlk sürüm.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=readFeeds

[2]: https://www.nvaccess.org/addonStore/legacy?file=readFeeds-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=rf-o
