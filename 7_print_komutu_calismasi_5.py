import sys
f = open("deneme_5.txt", "w")
sys.stdout, f = f, sys.stdout
print("deneme", flush=True)
f, sys.stdout = sys.stdout, f
print("deneme")