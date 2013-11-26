# RSS Akışlarını Oku #

* Yazarlar: Noelia Ruiz Martínez, Mesar Hameed
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

- Haber listesi...  Geçerli akış içindeki haber listesini gösterir. Okumak
istediğiniz haberi seçip ilgili sayfayı tarayıcıda açmak için tamam tuşuna
basın.  - Geçici akış adresi... control + NVDA + shift + enter: Takip etmek
istediğiniz akış adresini girmeniz için bir iletişim kutusu açar. İletişim
kutusunu açtığınızda   takip  etmekte olduğunuz adres gösterilir. - Kayıtlı
akış adresleri... NVDA+control+enter: Akış adreslerinin kaydedildiği
dosyalardan birini seçmeniz için bir iletişim kutusu açar.  - Geçerli adresi
dosyaya kaydet... NVDA+shift+enter: Geçerli adresi bir dosyaya kaydetmeniz
için bir iletişim kutusu açar.  Eğer adressFile.txt adlı dosyaya
kaydederseniz, bu adres varsayılan olarak takip edilen akış olacaktır.  -
Mevcut akışı güncelle: control+shift+NVDA+8: Seçilen akışı
günceller. Akışlar otomatik olarak güncellenmez.  - Akış klasörünü
yedekle...  Kayıtlı akış adreslerinizin bulunduğu dosyalarla ilgili klasörü
yedeklemeniz için bir iletişim kutusu açar. Varsayılan olarak seçilen klasör
NVDA kullanıcı konfigürasyon dizinidir.  - Beslemeleri Geri Yükle...  Akış
adreslerinin yedeklendiği klasörden adreslerin kaydedildiği dosyaları geri
yükler. Akış adresleriyle ilgili klasörü seçtiğinizden emin olun.

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

## 1.0 Değişiklikler ##
*	 İlk sürüm.

[[!tag dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf-dev

[2]: http://addons.nvda-project.org/files/get.php?file=rf

