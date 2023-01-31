import sys
f = open("dosya.txt", "w")
sys.stdout = f
print("deneme metni", flush=True)
print(sys.stdout, flush=True)

