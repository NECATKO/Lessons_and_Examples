#Ters taksim (\)

print('Yarin Antep\'e geliyorum.')
print("Antep'in bir asil ismi \"Gazianterp\" tir.")
print(" ")


#Satir basi (\n)

print("birinci satir\nikinci satir\nucuncu satir")
print(" ")
baslik = "Merhaba bu derse hos geldiniz!"
print(baslik, "\n", "="*len(baslik), sep=(""))


#Zil sesi (\a)

print("\a" * 10)
print(" ")


#Ayni satirin basi (\r)

print("Merhaba \rzalim dunya")
print(" ")


#Dusey sekme (\v)

print("Dusey\vsekme")
print(" ")


#Imlec kaydirma (\b)

print("yahoo.com\b.uk")
print(" ")


#Kucuk Unicode (\u)

print("\u0131")
print(" ")


#Uzun ad (\N)

import unicodedata
print(unicodedata.name("a"))
print("\N{LATIN SMALL LETTER A}")
print(" ")


#Onaltili Karakter (\x)

print("\x4E")
print(" ")


#Etkisizlestirme (r)

print("ornek_metin\akmana\bilbord\x41_kere_mashallah  \, \n, \a, \b, \x41, \\, r" )
print(" ")
print(r"ornek_metin\akmana\bilbord\x41_kere_mashallah  \, \n, \a, \b, \x41, \\, r" )


#sayfa basi (\f)

f = open("kacis_dizisi_calisma.txt", "w")
print("deneme\fdeneme", file=f)
f.close()
