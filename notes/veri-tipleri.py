# Temel Veri Tipleri

### Booleans ###
# Mantıksal veri türüdür
# bool sınıfına işaret
# True veya False olabilir  
    # Makine dilinde
        # 1 -> True
        # 0 -> False
# Tüm veri tiplerinin varsayılan değerleri bool türden `False` yani `Yanlış` olarak bulunur
    # Örneğin: 
        # Int: 0 -> False
        # String: '' -> False
        # Float: 0.0 -> False 
        # Complex: 0j -> False
        # Bool: False -> False
# Tam sayılar 0 olmadığı müddetçe, negatif olsalar dahi;
# bool türden `True` yani `Doğru` kabul edilir

ogrenci_mi = True
calisiyor_mu = False

# print("Öğrenci mi? : ", ogrenci_mi, "\nÇalışıyor mu? : ", calisiyor_mu)

yas = 0

bool(yas) # False



# print(bool(yas)) # False
# print(bool(-1)) # True
# print(bool(" ")) # True
# print(bool("")) # False


# print(bool()) # False False
# print(bool(int())) # False 0
# print(bool(str())) # False ""
# print(bool(float())) # False 0.0
# print(bool(complex())) # False 0j

# bool türler integer gibi davranabilir

# 3 ifade de birbirinin eşitidir
yeni_yas = yas + 1
yeni_yas = yas + True 
yeni_yas = yas + int(True)

# aynı şekilde, division örneği:

# 1 / False -> 1 / 0 # hata: ZeroDivisionError

### Strings ###
# Metinleri tutmaya yarayan veri tipidir
# 4 farklı metin tanımlama şekli vardır
# Tek tırnak ve çift tırnak -> "Mert", 'Mert'
# Üç tırnak tanımları -> """Life is good""", '''Life is good'''
# Varsayılan değeri '' yani boş metindir
# Iterate edilebilir (içinde gezilebilir) bir veri tipidir
# 3 adet metin formatlama çeşidi vardır (ders sonuna doğru detaylandırıcam)
    # f-string
    # str.format fonksiyonu
    # % operatörü

# single-line (tek satır string ifadeleri)
isim = "Mert"

# multi-line (çok satırlı string ifadeleri)

siir = """
Sana gitme demeyeceğim.
Üşüyorsun ceketimi al.
Günün en güzel saatleri bunlar.
Yanımda kal.

Sana gitme demeyeceğim.
Gene de sen bilirsin.
Yalanlar istiyorsan yalanlar söyleyeyim,
İncinirsin.

Sana gitme demeyeceğim,
Ama gitme, Lavinia.
Adını gizleyeceğim
Sen de bilme, Lavinia.
"""

# inner strings (iç içe stringler)

cumle = "Biri avazı çıktığınca bağırdı: 'Neler oluyor orada? Ne bu gürültü!'"

kompozisyon = """
Python'ın yanısıra hoşuma giden diller:
'''
C/C++ (std17, std20, std23)
Rust
Swift
TypeScript
Golang
'''
"""

# içiçe metinlerde içteki metin ifadesi dıştaki ile aynı metin karakteri ile tanımlanamaz
# sözdizimi hatası
# cumle =  "Biri avazı çıktığınca bağırdı: "Neler oluyor orada? Ne bu gürültü!""

# metinlerde escaping operatörü 

# Alttaki ifade sözdizimi hatası iken;
# cumle =  "Biri avazı çıktığınca bağırdı: "Neler oluyor orada? Ne bu gürültü!""

# Bu cümle tamamen geçerlidir
# Escape karakteri hataya neden olan karakterlerden önce getirilirse ifade geçerli olur
cumle =  "Biri avazı çıktığınca bağırdı: \"Neler oluyor orada? Ne bu gürültü!\""

### Floats ### Floating Point Numbers 
# Ondalıklı sayıları tutan veri tipidir
# Varsayılan değeri 0.0 'dır
# `float` sınıfına işaret eder
# Diğer aritmetik/mantıksal türlerle işleme girebilir (int/complex/bool)
# Matematiksel açıdan tamsayıların sıfır ile bölümü belirsiz (0.0)
# Negatif ve Pozitif olarak da tanımlanabilir

# negatif ondalıklı sayı
negatif = -8.5
pozitif = 8.5
pozitif = +8.5
pozitif = -(-8.5)
pozitif = (-1 * -8.5)

### Integers ###
# Tam sayıları tutan veri tipidir
# Varsayılan değeri sıfırdır (0)
# `int` sınıfına işaret eder 
# Diğer aritmetik/mantıksal türlerle işleme girebilir (float/complex/bool)
# Bir tamsayının ondalıklı gösterimi kendisine eşittir (1 = 1. = 1.0)
# Matematiksel açıdan tamsayıların sıfır ile bölümü belirsiz
# olduğundan sıfıra bölme işlemi hatalıdır

# pozitif tamsayı tanımı
yil = 2023 

# negatif tamsayı tanımı
kat = -1

# varsayılan tamsayı tanımları
para = 0
para = int()

# ondalıklı sayıların tamsayı olarak okunması

pi_ondalikli = 3.14

pi_ondaliksiz = 3

# bu noktada int sınıfı 3.14 ile çağrılırsa int türden 3'e karşılık gelir

pi = int(pi_ondalikli) # 3

# sıfıra bölünme istisnası

# ifade = pi / 0  # geçersiz&hata: ZeroDivisionError

# ondalıklı sayılarla işlem ilişkisi

# 75000.0 -> ifade ondalığa dönüşür fakat 75000 de diyebiliriz
faizli_odenecek_tutar = 30000 * 2.5 # %150

# Örneğin: 
print(75000 == faizli_odenecek_tutar) # True


### TÜR DÖNÜŞÜMLERİ ###

# Stringlerden Aritmetik Türlere Dönüşüm

# tamsayılar

# ondalıklı sayılar

sayi = "3e25"
sayi = float(sayi)

# print(f"{sayi:.2f}")

# print(sayi == int(sayi))

# booleans 

# float to int - ondalıklı sayılardan  tam sayılara dönüşüm

print(int(3.14)) # değer kaybı

# temel türlerden stringe dönüşüm

# print("id", "isim", "email", sep="  ", end="\n---------------\n")
# print("1", "Mert", "mert@proton.me", sep="   ")

### STRING FORMATTERS ###


# f-string
""""""
yas = 19

selamlama = f"Merhaba, ben Mert. {yas} yaşındayım."

# print(selamlama)

# print("PI sayısı, yaklaşık olarak: ", f"{3.14159:.2f}")

# print(f"Merhaba, {'Mert'}, yaşınız: f'{yas}'")

moodum_nasil = 2

# print("Merhaba Mert. Bugün Nasılsın? ")
# print(f"Ben bugün, {'çok iyiyim' if moodum_nasil > 5 else 'fena değilim'}")

# str.format fonksiyonu

selamlama_metni = "Adınız: {isim}\nYaşınız: {yas}\nOkuduğunuz Bölüm: {bolum}\nÇalışıyor Musunuz? {is_durumu}"

sonuc = selamlama_metni.format(is_durumu="Çalışmıyorum", yas=20, isim="Ahmet", bolum="Mekatronik Müh.")

# print(sonuc)

# % operatörü ile formatlama

# tamsayılar %d
# float %f, %.2f
# string %s

selamlama_metni = "Adınız: %s\nYaşınız: %d\nOkuduğunuz Bölüm: %s\nÇalışıyor Musunuz? %s"
ad = "Mert"
yas = 20
bolum = "CSE"
calisilan_is = "Freelance Developer"

# print(selamlama_metni % (ad, yas, bolum, calisilan_is))

# print("Not ortalamanız: %.2f" % (2.156))

# string fonksiyonları

# tüm harfleri küçük yapma

text = "Merhaba Dünya"

lowertext = text.lower() # merhaba dünya
uppertext = text.upper() # MERHABA DÜNYA
titletext = lowertext.title() # Merhaba Dünya
captext = text.capitalize() # Merhaba dünya

bosmetin = "     mert\n\t"

bosmetin.strip() # 'mert'
bosmetin.rstrip() # '     mert'
bosmetin.lstrip() # 'mert\n\t'

komut = "add elraenn 1d nreload"

add = komut.startswith("add") # True
komut.endswith("-reload") # False

# print(komut.find("1df")) # -1 
# print(komut.find("1d")) # 12

# print(komut.count(" "))

isim = "546377546"
isim = isim.replace("M", "B").replace("t", "k")

inp = " "

# split 

dosya = "/Users/mert/Desktop/eğitim/ders-2.py"

dirs = (dosya.removeprefix("/").split("/"))

user_dir, user, dir, dir_name, file_name = dirs

# print("%s kullanıcısı %s dizininde %s isimli bir dosya oluşturdu." % (user, dir_name, file_name))

file_name, file_extension = file_name.split(".") # 'ders-2', 'py'

# print("%s isimli dosya %s uzantısıyla oluşturuldu, tam dosya adı: %s" % (file_name, file_extension, f"{file_name}.{file_extension}"))

# -maxsplit

metin = "scope/mert/desktop/egitim"

dir, path = (metin.split("/", maxsplit=1))

# print("{} isimli dizinde {} path adresindeki dosya tanımlandı.".format(dir, path))

hello_world_text = """
 merhaba dünya
 hello world
 hello mundo
"""

hello_world_text = hello_world_text.strip()

# print(hello_world_text.split("\n "))
# print(hello_world_text.splitlines()[1].strip())