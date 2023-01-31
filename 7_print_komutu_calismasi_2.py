dosya = open("deneme.txt", "w")
print("Ben python, Monty python!", file = dosya)
dosya.close()

import os
print(os.getcwd())