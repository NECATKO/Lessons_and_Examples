#Bu kod bir alistirmadir.

print ("Aylik yol masrafi hesaplama programina hos geldiniz.")
Gelis = input ("Gidis ucretinizi yaziniz: ")
Gidis = input ("Gelis ucretinizi yaziniz: ")
Sure = input ("Bir ayda kac gun yolculuk yaptiginizi yaziniz: ")
Masraf = (float(Gelis) + float(Gidis)) * float(Sure)
print ("Bir aylik yol gideriniz: " + str(Masraf))