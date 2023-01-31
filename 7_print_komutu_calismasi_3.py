f = open("Kisisel_bilgiler.txt", "w")

print("Ornek KISI", sep=(" "), file=f)
print("Kullanilan_sistem", "Windows", sep=(" "), file=f)
print("Cok_gizli_sifre", "za_xd", sep=(" "), file=f, flush=True)
print("Cok onemli gizli bilgi felan", file=f)
print("warthunder dan sizdirilan gizli bilgiler", file=f)
print("boyle ornekler yazmaya devam edersem basim belya girecek", file=f, flush=f)
print(*"TBMM", sep=("."))
print(*"KURTARINBENIIII", sep=("^"), file=f)
f.close()

import os
print(os.getcwd())
