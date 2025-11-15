
"""
# 1. Ödev
isim = input("İsminizi giriniz: ")
soyisim = input("Soyisminizi giriniz: ")
dogum_yili = int(input("Doğum yılınızı giriniz: "))

yas = 2025 - dogum_yili

print(f"{isim} {soyisim}, {yas} yaşındadır.")

# 2. Ödev
kisa_kenar = float(input("Dikdörtgenin kısa kenarını giriniz: "))
uzun_kenar = float(input("Dikdörtgenin uzun kenarını giriniz: "))

alan = kisa_kenar * uzun_kenar
cevre = 2 * (kisa_kenar + uzun_kenar)

print(f"Dikdörtgenin Alanı: {alan}")
print(f"Dikdörtgenin Çevresi: {cevre}")

# 3. Ödev
elma_kilo = float(input("Kaç kilo elma aldınız? "))
armut_kilo = float(input("Kaç kilo armut aldınız? "))
cilek_kilo = float(input("Kaç kilo çilek aldınız? "))

elma_fiyat = 12
armut_fiyat = 15
cilek_fiyat = 25

toplam_tutar = (elma_kilo * elma_fiyat) + (armut_kilo * armut_fiyat) + (cilek_kilo * cilek_fiyat)

print(f"Toplam Ödenecek Tutar: {toplam_tutar} TL")

# 4. Ödev
sayi = int(input("Bir tam sayı girin: "))

buyuk_mu = sayi > 100
cift_mi = sayi % 2 == 0
pozitif_mi = sayi


print("Sayı 100'den büyük mü? :", buyuk_mu)
print("Sayı çift mi?          :", cift_mi)
print("Sayı pozitif mi?       :", pozitif_mi)


# 5. Ödev
kayitli_sifre = "1234"
girilen_sifre = input("Lütfen şifrenizi girin: ")
eslesiyor_mu = girilen_sifre == kayitli_sifre
farkli_mi = girilen_sifre != kayitli_sifre

print("Şifre doğru mu?       :", eslesiyor_mu)
print("Şifre farklı mı?      :", farkli_mi)

# 6. Ödev

hiz = float(input("Aracın hızını girin (km/s): "))
zaman = float(input("Yolculuk süresini girin (saat): "))

mesafe = hiz * zaman

print("Gidilen Toplam Mesafe:", mesafe, "km")

# 7. Ödev

vize_notu = float(input("Vize notunu girin: "))
final_notu = float(input("Final notunu girin: "))

gecme_durumu = (final_notu >= 50) and ((vize_notu + final_notu) / 2 >= 50)

print("Dersten geçme durumu:", gecme_durumu)


# 8. Ödev

misket_sayisi = int(input("Toplam misket sayısını girin: "))
cocuk_sayisi = int(input("Kaç çocuğa paylaştırılacak?: "))

kisiye_dusen = misket_sayisi // cocuk_sayisi

artan = misket_sayisi % cocuk_sayisi

print("Çocuk Başına Düşen Misket:", kisiye_dusen)
print("Artan Misket Sayısı:", artan)

# 9. Ödev
yas = int(input("Yaşınızı girin: "))
ehliyet = input("Ehliyetiniz var mı? (True/False): ")

ehliyet = ehliyet.lower() == "true"
uye_olabilir = (yas > 25 and ehliyet) or (yas > 18 and not ehliyet)
print("Araba kullana billir mi:", uye_olabilir)

"""
# 10. Ödev

sayi_bir = int(input("1 sayısını girin: "))
sayi_iki = int(input("2 sayısını girin: "))
sayi_uc = int(input("3 sayısını girin: "))

toplam_buyuk_mu = (sayi_bir + sayi_iki + sayi_uc) > 100
sirali_mi = (sayi_bir > sayi_iki) and (sayi_iki > sayi_uc)
cift_buyuk_mu = (sayi_bir % 2 == 0) or (sayi_iki > 50)
carpim_buyuk_mu = (sayi_bir * sayi_iki * sayi_uc) > (sayi_bir + sayi_iki + sayi_uc)

print("1 + 2 + 3 toplamı 100'den büyük mü?:", toplam_buyuk_mu)
print("1 > 2 > 3 (büyükten küçüğe sıralı mı?):", sirali_mi)
print("1 çift VEYA 2 50'den büyük mü?:", cift_buyuk_mu)
print("1. * 2. 3., (1 + 2 + 3)'den büyük mü?:", carpim_buyuk_mu)
