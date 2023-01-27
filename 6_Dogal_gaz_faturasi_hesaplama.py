#Bu bir alistirmadir.

#Oncelikle aylarin gun sayisini atiyoruz.
ocak = mart = mayis = temmuz = agustos = ekim = aralik = 31
nisan = haziran = eylul = kasim = 30
subat = 28

#Girilecek degerleri yaziyoruz.
aylik_sarfiyat = input("Lutfen aylik sarfiyyatinizi giriniz: ")
fatura_tutari = input("Lutfen aylik fatura tutarinizi giriniz: ")

#Aralara bosluk koyuyoruz.
print(" ")

#Gazin birim fiyatini hesaplatiyoruz
birim_fiyat = float(fatura_tutari) / float(aylik_sarfiyat)
print("Harcadiginiz gazin birim fiyati: " + str(float(birim_fiyat)))

print(" ")

#Mart ayinin gunluk sarfiyatini yazdiriyoruz.
gunluk_sarfiyat = float(aylik_sarfiyat) / float(mart)
print("Mart ayinin gunluk sarfiyati: " + str(float(gunluk_sarfiyat)))

print(" ")

#Nisan ayinin faturasini yazdiriyoruz.
nisan_fatura = float(birim_fiyat) * float(gunluk_sarfiyat) * float(nisan)
print("Nisan ayinin faturasi: " + str(float(nisan_fatura)))

print(" ")

#Subat ayinin faturasini yazdiriyoruz.
subat_fatura = float(birim_fiyat) * float(gunluk_sarfiyat) * float(subat)
print("Subat ayinin faturasi: " + str(float(subat_fatura)))