#elif

print("Sacma sapan sayi analiz tool'una hos geldiniz.")
print(" ")
print('''Bu tool bir sayinin 100'den buyuk olup olmadigini size soyler.
cikan ciktiya gore sayinin 100'den buyuk olup olmadigini anlarsiniz.
Lutfen fazla sorgulamayin. Tesekkurler. ''')

sayi = input("Lutfen analiz etmek istediginiz sayi yi yaziniz: ")
sayi = int(sayi)
print(" ")

if sayi > 100:
    print("Girdiginiz sayi 100'den buyuktur.")

elif sayi > 150:
    print("Girdiginiz sayi 150'den buyuktur.")

elif sayi == 100:
    print("Girdiginiz sayi 100'dur.")

elif sayi < 100:
    print("Girdiginiz sayi 100'den kucuktur.")

elif sayi < 50:
    print("Girdiginiz sayi 50'den kucuktur.")