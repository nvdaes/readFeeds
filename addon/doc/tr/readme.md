# Akışları Oku #

* Yazarlar: Noelia Ruiz Martínez, Mesar Hameed

Bu eklenti NVDA kullanarak Atom veya RSS biçiminde akışları okumak için basit bir yol sunar.
Akışlar otomatik olarak yenilenmeyecektir.
Aşağıda akışlardan bahsettiğimizde, hem RSS hem de ATOM akışlarını kastediyoruz.

## Komutlar ##

### Akışları Oku iletişim kutusu ###

Akışları Oku iletişim kutusuna nvda menüsü, Araçlar alt menüsü, akış listesi öğesinden erişebilirsiniz.

Aşağıdaki kontrolleri içerir:

* Filtreleme kriteri: Önceden kaydedilmiş akışları aramak için bir düzenleme kutusu.
* İletişim kutusu açıldığında odaklanılan kayıtlı akışların listesi.
* Makale listesi: Geçerli akışınızdaki makalelerin listesini gösteren bir iletişim kutusu açar. Okumak istediğiniz makaleyi seçin ve Enter tuşuna basın veya seçilen makalenin web sayfasını aç düğmesine basarak ilgili sayfayı tarayıcınızda açın. Seçilen makalenin başlığını ve bağlantısını gösteren bir iletişim kutusu açmak için "Makale hakkında" düğmesine basın; bu iletişim kutusundan bu bilgileri panoya kopyalayabilirsiniz.
* Akışı aç: Seçili akışı varsayılan uygulamada açar.
* Akışı HTML olarak aç: Seçili akışı varsayılan web tarayıcısında açar. Makaleler hakkındaki bilgileri panoya kopyalamak için yayın tarihlerini ve düğmeleri gösterip gizleyebileceksiniz.
* Akış adresini kopyala: Akış adresini panoya kopyalamak isteyip istemediğinizi onaylamak için bir iletişim kutusu açar.
* Yeni: Yeni bir akışın adresini girmek için düzenleme kutusu içeren bir iletişim kutusu açar. Adres geçerliyse ve yayın kaydedilebilirse, yayın başlığına göre adı, yayın listesinin içinde görünecektir.
* Yeniden Adlandır: Seçili akışı yeniden adlandırmak için bir düzenleme kutusu içeren bir iletişim kutusu açar.
* Sil: Onaydan sonra seçilen akışın silinmesi için bir iletişim kutusu açar.
* Varsayılan olarak ayarla: Seçilen beslemeyi varsayılan olarak ayarlar, böylece makalelerine ilgili NVDA girdi hareketleriyle erişilebilir.
* OPML dosyasından akışları içe aktar: Bir OPML dosyasından yeni akışlar eklemek için bir iletişim kutusu açar.
* Akışları OPML dosyasına kaydet: Akışlar iletişim kutusunda bulunan beslemeleri bir OPML dosyasına kaydetmek için bir iletişim kutusu açar.
* Tercihler: NVDA menüsünde Tercihler, ayarlar, Akışları oku kategorisinde de bulunan akışları oku için ayarlar diyalog penceresini açar.
* Kapat: Akışlar iletişim kutusunu kapatır.

### Notlar #####

* Filtreye göre düzenleme kutusu NVDA menüsünden Tercihler, Ayarlar, Akışları oku kategorisinden veya akışlar iletişim kutusundaki Tercihler düğmesine basarak Makaleyi aç düğmesinden sonra yerleştirilebilir.
* Bu panel, Makalelerin listesi iletişim kutusunda makale tarihlerini gösterme seçeneğine sahiptir.


### Klavye komutları ###

* Ctrl+Shift+NVDA+Aralık Tuşu: Mevcut makalenin URL'sini duyurur. İki kez basmak web sayfasını açar.
* Ctrl+Shift+NVDA+8: Seçili akışı yeniler ve en son başlığı duyurur.
* Ctrl+Shift+NVDA+I: Mevcut akış başlığını ve bağlantısını duyurur. İki kez basmak, başlığı ve ilgili bağlantıyı panoya kopyalar.
* Ctrl+Shift+NVDA+U: Önceki akış başlığını duyurur.
* Ctrl+Shift+NVDA+O: Sonraki akış başlığını duyurur.

## Bildirimler ##

* Başlık veya URL kopyalandığında.
* Bir akışa bağlanılamadığında/yenileme yapılamadığında veya URL, geçerli bir akışa karşılık gelmediğinde.
* Yeni bir akış oluşturulamıyorsa NVDA bir hata mesajı görüntüler.
* Makale listesi iletişim kutusunun başlığı, seçilen akış adını ve mevcut öğelerin sayısını gösterir.

## 44.0.0 İçin değişiklikler

* NVDA'ya dahil edilen xml paketi kaldırıldı.

## 39.0.0 İçin değişiklikler

* Başlık veya URL kopyalandığında geliştirilmiş bildirimler.

## 34.0.0 İçin değişiklikler

* Rss.cbc.ca akışları için destek eklendi.

## 21.0 İçin değişiklikler

* Başlıksız makaleler içeren akışlar, Makaleler iletişim kutusunda sunulabilir ve HTML olarak açılabilir.

## 20.0 İçin değişiklikler

* universalFeedParser, 5.0.1'e güncellendi ve daha fazla akış için destek eklendi.

## 15.0 İçin değişiklikler

* NVDA 2023.1 ile uyumlu.

## 14.0 İçin değişiklikler

* Bazı akışların eklenmesini engelleyen bir hata düzeltildi.

## 13.0 İçin değişiklikler

* Eklenti, güvenli ekranlarda kullanılamaz.
* Akışlar, OPML dosyalarından yönetilir.
* Akış yönetim sistemindeki değişiklikler nedeniyle, varsayılan akışın  ayarlandığı yapılandırma dosyasında değişiklikler var. Tekrar ayarlamak istiyorsanız lütfen akışlar iletişim kutusunu kullanın.
* Önceki sürümlerde kullanılan eski metin dosyalarınız, eklenti başlatıldığında otomatik olarak yeni OPML biçimine aktarılacaktır.
* Akışları kopyala ve geri yükle özelliği, OPML dosyalarından içe aktarma ve kaydetme özelliğiyle değiştirildi.
* İyi biçimlendirilmemiş akış adresleri  , eklentiyle uyumlu hale getirilmeleri için eklenmeden önce işlenebilir.
* Akışları oku ayarları panelinde yeni bir seçenek, makale tarihlerinin Makale listesi iletişim kutusunda gösterilmesine olanak tanır.

## 12.0 İçin değişiklikler

* NVDA'nın araçlar menüsündeki öğeler için kısayolların beklendiği gibi çalışmamasına neden olan bir hata düzeltildi.

## 11.0 İçin değişiklikler

* NVDA 2021.1 ile uyumlu

## 10.0 İçin değişiklikler ##

* Varsayılan web tarayıcısında seçilen akışı HTML olarak açmak için bir düğme eklendi.
* Yeni bir akış oluşturulamıyorsa, bu durum bir hata iletişim kutusunda bildirilir.
* Bazı makalelerin düzeni ve sunumunda iyileştirme.
* Daha fazla akış desteklenebilir.
* Akışlar iletişim kutusu açıldığında, arama düzenleme kutusu yerine yayınların listesine odaklanılacaktır.
* Arama düzenleme kutusunun akış listesinden sonra yerleştirilip yerleştirilmeyeceğini seçebilirsiniz; bu, akışlar iletişim kutusunu kapatmadan başka bir pencereden geçiş yaparken bile listeye odaklanmak için yararlı olabilir.
* Akışlar iletişim kutusundan akış adresini panoya kopyalamak için bir düğme eklendi.

## 9.0 İçin değişiklikler ##

* NVDA 2019.3 veya daha yeni sürümler gerekli.

## 8.0 İçin değişiklikler ##

* Eklenti güncellendiğinde, NVDA'nın ana yapılandırma klasörüne kaydedilen akışları içe aktarmayı tercih etmediğiniz sürece, eklentinin önceki sürümünde kaydedilen akışlar otomatik olarak yeni sürüme kopyalanacaktır.
* Akışları kopyalamak için iletişim kutusunu kullanırken, seçilen klasörün adı personalFeeds değilse, Belgeler veya İndirilenler gibi önemli verileri içeren dizinlerin silinmesini önlemek için bu ada sahip bir alt klasör oluşturulacaktır.

## 7.0 İçin değişiklikler ##

* Akışlar iletişim kutusu, akışların yedeğini içerebilecek bir klasörü açmak için bir düğme içerir.
* Akışları filtrelemek için düzenleme kutusunu kullanırken, hiçbir sonuç bulunmazsa, akışların listesi ve diğer kontroller devre dışı bırakılır, böylece NVDA boş listede "bilinmeyen" demez.
* Örneğin, akışta hatalar nedeniyle makale listesi iletişim kutusu gösterilemiyorsa, NVDA bir hata mesajı verir; böylece NVDA'yı yeniden başlatmaya gerek kalmadan Akışlar iletişim kutusu kullanılabilir.

## 6.0 İçin değişiklikler ##

* Varsayılan akış güncellendiğinde ve sunucu sorunları nedeniyle çalışmayı durdurduğunda, önceki makaleler silinmez ve ilgili tuşlarla okunabilir.
* Hata düzeltmesi: Varsayılan akış iki kez tekrar güncellenebilir.

## 5.0 İçin değişiklikler ##

* Makaleler listesi iletişim kutusu geliştirildi.
* NVDA 2018.3 veya daha yeni sürümlerle uyumlu (gerekli).

## 4.0 İçin değişiklikler ##

* Akışlar iletişim kutusundan seçilen akışı açmak için bir düğme eklendi.

## 3.0 İçin değişiklikler ##

* Akış dosyalarını yönetmek için kullanılan iletişim kutuları kaldırıldı. Artık işlevleri akışlar iletişim kutusuna dahil edildi.
* NVDA'da gösterilen iletişim kutularının görünümüne bağlı kalınarak iletişim kutularının görsel sunumu geliştirildi.
* Varsayılan akış, NVDA'nın Konfigürasyon dosyasına kaydedilir. Dolayısıyla, yapılandırma profillerinde farklı varsayılan akışlar ayarlamak mümkündür.
* NVDA 2016.4 gerekli.

## 2.0 İçin değişiklikler ##

* Eklenti yardımına, Eklenti Mağazasından ulaşılabilir.

## 1.0 İçin değişiklikler ##

* İlk sürüm.
