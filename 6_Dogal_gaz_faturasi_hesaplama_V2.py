#Bu bir alistirmadir.

#Liste tanimi yapiyoruz.
aylar_sozluk = {"ocak":31, "mart":31, "mayis":31, "temmuz":31, "agustos":31, "ekim":31, "aralik":31, "nisan":30, "haziran":30, "eylul":30, "kasim":30, "subat":28,  }

#Girilecek degerleri yaziyoruz.
aylik_sarfiyat = input("Lutfen aylik sarfiyyatinizi giriniz: ")
fatura_tutari = input("Lutfen aylik fatura tutarinizi giriniz: ")
girilen_ay = input("Lutfen girdiginiz faturanin hangi aya ait oldugunu giriniz: ")
hesaplanacak_ay = input("Lutfen Hesaplamak istediginiz faturanin ayini giriniz: ")

#Aralara bosluk koyuyoruz.
print(" ")

#Gazin birim fiyatini hesaplatiyoruz
birim_fiyat = float(fatura_tutari) / float(aylik_sarfiyat)
print("Harcadiginiz gazin birim fiyati: " + str(float(birim_fiyat)))

print(" ")

#Genel gunluk sarfiyati yazdiriyoruz.
gunluk_sarfiyat = float(aylik_sarfiyat) / float(aylar_sozluk[girilen_ay])
print("Hesaplana aydaki gunluk sarfiyat: " + str(float((gunluk_sarfiyat))))

print(" ")

#Hedef ayin faturasini yazdiriyoruz.
hedef_ay_fatura = float(gunluk_sarfiyat) * float(birim_fiyat) * float(aylar_sozluk[hesaplanacak_ay])
print("Girdiginiz ayin faturasi: " + str(float(hedef_ay_fatura)))