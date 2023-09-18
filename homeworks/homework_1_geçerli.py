## Homework - 1 ##
# Not: Açıklamalar [] içinde olacaktır.

## 5 GEÇERLİ STRİNGS

# 1.örnek [Python için stringsler çift tırnak ile gösterilebilir.]
print("Başlamak başarmanın yarısıdır.\n") 

# 2.örnek [Python için stringsler tek tırnak ile gösterilebilir.]
print('Dostoyeski\n')

# 3.örnek [Değişkene strings atanabilir.]
a="Sevdiğim birkaç sanatçıdan biri\n"
print(a)

# 4.örnek [Çok satırlı dizi, üç tırnak işaretiyle değişkene atanabilir. Ve değişken için büyük / küçük harf kullanılabilir.]
Birsarkı="""Gemimizin yükü ağır
Bilmem daha kaç dalga alır
Yaşımızın tuzu kuru
Ondan pınarında donup kalır\n"""
print(Birsarkı)

# 5. örnek [Çok satırlı dizi, üç tekli tırnakla değişkene atanabilir.]
c='''Ruhumun derdi büyük
Geceler küskün gibi önümde
Bu hayat geçmiyor acıyla
Değmiyor kalbin inceliklerine\n'''
print(c)

## ESCAPE
# Normalde izin verilmeyen bir durum için kullanılabilir.
# Yeni satır oluşturmak için kullanılar. 
derskonusu= "\nSınavda limit,türev \"en önemlisi integral\" olacaktır.\n"
print(derskonusu)
xue= 'Ayşe\'nin başarısının sırrı azim ve kararlılığıdır.\n'
print(xue)

 ## Tür Dönüşümleri 
 
#Float to integer

x=float(3.16)
x=int(x)
print(x)

#İnteger to float

yb=int(25)
yb=float(yb)
print(yb)

sayi=15.641845644
print(f"Ortalama değer {sayi:.2f}\n")
print(sayi == int(sayi))
print(sayi >= int(sayi)) 

#String Fonksiyonlarına Örnekler

#1.Örnek [Dizenin kaç karakterden oluştuğunu bulmak için len() kullanılır. Fakat hesaplamada escape karakterinin sayılmaması için .lstrip()  .rstrip() .strip() kullanılır. Başlangıçta escape ile yazdırdım. Sonrasında boşluğu çıkarıp karakter sayısını hesapladım. Saymaya sıfırdan başladığı için sonuç 14 çıktı.]
x="\nİstiklal Marşı"
print(x)
x=x.strip()
print(len(x))

#2.örnek [Escape karakterlerinin sayılmasını istemediğim için .lstrip yaptım ve yeni bir değişken atadım. Sonra bulmak istediğim harf için .index fonksiyonunu kullandım. Escape saymadan, saymaay sıfırdan başladığı için sonuç 15 çıktı. Ve sonrasında tekrar tüm küçük harfler arasından index değeri bulmak için, .index() ve .lower() fonksiyonlarını kulladnım. Sıfırdan başladığı için sonuç 7 çıktı.]
p="\nSARI MAVİ KIRMIZI YEŞİL TURUNCU"
print(p)
p=p.lstrip()
print(p.index("Z"))
p=p.lower()
print(p.index("v"))

#3.örnek [Atadığım değişkenin .isalnum(), yani sayı veya harflerden oluşup oluşmadığını test etmek için kullandım. Harf ve sayılardan oluştuğu için sonuç "True". Aynı değişkenin .islower tüm hepsinin küçük harflerden oluşup oluşmadığının sonucu "False" çıktı (Büyük harf varlığından dolayı), ve sadece rakamlardan oluşup oluşmadığını da test etmek için .isdigit() fonksiyonunu kullandım. Harflerin varlığından dolayı sonuç "False" çıktı.]

sehir_="İstanbul34Ankara06İzmir35"
print(sehir_.isalnum())
print(sehir_.isdigit())
print(sehir_.islower())

#4.örnek [Kız isimlerinin olduğu kısmı çıkarmak için .rstrip kulladnım. Erkek isimlerini tek tek ayrılması için .split kullandım.]
kız_erkek_isimleri="Ali-Ahmet-Deniz, Selin-Elif-Sude"
erkek_isimleri=kız_erkek_isimleri.rstrip(", Selin-Elif-Sude")
print(erkek_isimleri.split("-"))

# String Formatlama

# f-string
print("\n")
pasta_çilek_sayısı=15
print(f"Pasta {'muzlu' if pasta_çilek_sayısı <=15 else 'çilekli'}")

hırsız_sayısı="5 hırsız"
print(f"Polisler bu gece toplam {hırsız_sayısı} yakaladı.\n")

# str.format fonksiyonu
sevdığım_sanatcılar_lıst="Birinci {ad1}\nİkinci {add}\n"
sonuc=sevdığım_sanatcılar_lıst.format(ad1="Melek Mosso", add="Suzan Hacıgarip")
print(sonuc)

pasta_dilimleme="Ali {parça} parçaya pastasını böldü, Elif ise pastasını {parça2} parçaya böldü. İkisinin toplam {parça3} dilim pastaları oldu.\n"
sonuc2=pasta_dilimleme.format(parça="2", parça2="3", parça3="10")
print(sonuc2)

# % operatörü
print("Lise obp puanı %.2f" %(85.4562))
print("Milli sporcu yaşının %d olduğunu söyledi. Takım yaş ortalaması %d olduğundun grubun en küçük üyesi unvanını yine %s aldı.\n" % (24, 22,"İpek"))

#İç içe string tanımlayabilmek için, dışarıda"" kullanılan yerlerde içeride '' kullanırız. Ya da tam tersi durumu kullanırız. Eğer hem dışarıda hem içeride aynı tırnak kullanacaksak \ escaping operatörü kullanabiliriz.
print("Öğretmen \"Sınav notlarını açıklayacağım.\"dedi.")
print("Mavi kalem '0.5' uç ile kullanılır.")

#2 konu açıklama

#starswith fonksiyonu
#bir şeyin ne ile başladığını test etmek için kullanılır.
sosyal_medya="Facebook, Youtube, Instagram"
print(sosyal_medya.startswith("Face"))

#bool
#varsayılan türlerin hepsi False. boşluk ya da negatif ise True 'dur. 
# int 0 float 0.0 string ''
yas=26
mezuniyet=23
iş_sayısı=0
print("\n")
print(bool(yas))
print(bool(mezuniyet))
print(bool(iş_sayısı))

sınıf_mı=True
anadolu_lisesi_mi=False
print("\n'10.sınıf mı?' ", sınıf_mı, "\n'Anadolu lisesinde mi okuyor?' ", anadolu_lisesi_mi)
