# RSS Akışlarını Oku #

* Yazarlar: Noelia Ruiz Martínez, Mesar Hameed
* NVDA uyumluluğu: 2019.3 veya üstü
* [Kararlı sürümü][1] indir
* [geliştirme sürümü][2]nü indir


Bu eklenti NVDA kullanarak Atom veya RSS formatında beslemeleri okumak için
basit bir yol sunar. Beslemeler otomatik olarak yenilenmez. Aşağıda besleme
derken hem RSS hem de ATOM beslemelerini kastediyoruz.

## Kurulum veya Güncelleme ##

Bu eklentinin önceki bir sürümünü kullanıyorsanız ve kişisel NVDA
konfigürasyon klasöründe bir RSS veya personalFeeds adlı klasör varsa,
eklentiyi güncellemek mi yoksa kurmak mı istediğiniz sorulacaktır. Önceki
RSS akışlarınızı kullanmaya devam etmek istiyorsanız Güncelle seçeneğiyle
devam edin.

## Komutlar ##

### RSS Okuma menüsü ###

RSS akışlarını Oku menüsüne NVDA+N ile açılan nvda menüsü altındaki araçlar
alt menüsünden ulaşabilir,  bu menüde aşağıdaki menüde seçeneklerini
bulabilirsiniz:

#### Akışlar ####

Aşağıdaki kontrolleri içeren bir iletişim kutusu açar:

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
* Akışların yedeğini içeren klasörü aç: Akışların yedeğini içerebilecek bir
  klasör açar. Bu, eklenti güncellendiğinde içe aktarılmaması gereken
  yayınları keşfetmek ve silmek için yararlı olabilir.
* Tercihler: NVDA menüsünde Tercihler, ayarlar, Akışları oku kategorisinde
  de bulunan akışları oku için ayarlar diyalog penceresini açar.
* Kapat: Akışlar iletişim kutusunu kapatır.

##### Notlar #####

* tempFeed adlı bir yayın oluşturulursa, adı zaten mevcut olan bir yayın
  oluşturmak için gerektiğinde bu dosya değiştirilebileceğinden lütfen
  yeniden adlandırın.
* Varsayılan olarak ayarlanan akış kaldırılamaz. Adres dosyasındaki akış
  adresi, yapılandırma sıfırlandığında varsayılan olarak kullanılacaktır, bu
  nedenle silinemez.
* Filtreye göre düzenleme kutusu NVDA menüsünden Tercihler, Ayarlar,
  Akışları oku kategorisinden veya akışlar iletişim kutusundaki Tercihler
  düğmesine basarak Makaleyi aç düğmesinden sonra yerleştirilebilir.

#### Akışlar klasörünü kopyala ####

Akışlarınızı personalFeeds dizinini kaydedebileceğiniz bir klasör seçmek
için bir iletişim kutusu açar. Varsayılan olarak, seçilen klasör,
personalFeeds dizinini oluşturacak olan NVDA'nın yapılandırma dizinidir.

#### Akışları geri yükle ####

PersonalFeeds klasöründeki akışlarınızın yerini alacak bir klasör seçmek
için bir iletişim kutusu açar. Yayın URL'lerini içeren bir klasör
yüklediğinizden emin olun.

### Klavye komutları ###

* Ctrl+Shift+NVDA+Space: Mevcut makalenin URL'sini duyurur. İki kez basmak
  web sayfasını açacaktır.
* Ctrl+Shift+NVDA+8: Seçili akışı yeniler ve en son başlığı duyurur.
* Ctrl+Shift+NVDA+I: Mevcut akış başlığını ve bağlantısını duyurur. İki kez
  basmak, başlığı ve ilgili bağlantıyı panoya kopyalayacaktır.
* Ctrl+Shift+NVDA+U: Önceki akış başlığını duyurur.Ctrl+Shift+NVDA+U:
  Announces previous feed title.
* Ctrl+Shift+NVDA+O: Sonraki akış başlığını duyurur.

## Bildirimler ##

* Başlık veya URL kopyalandığında.
* Bir akışa bağlanılamadığında/yenileme yapılamadığında veya URL, geçerli
  bir akışa karşılık gelmediğinde.
* PersonalFeeds klasörünü yedeklemek veya geri yüklemek mümkün değilse ve
  yeni bir akış oluşturulamıyorsa NVDA bir hata mesajı görüntüler.
* Makale listesi iletişim kutusunun başlığı, seçilen akış adını ve mevcut
  öğelerin sayısını gösterir.

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

[1]: https://addons.nvda-project.org/files/get.php?file=rf

[2]: https://addons.nvda-project.org/files/get.php?file=rf-dev

[3]: https://addons.nvda-project.org/files/get.php?file=rf-o
