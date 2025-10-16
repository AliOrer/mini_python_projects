
import random , string

def sifre_uret(uzunluk =16):
    karakterler = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(karakterler) 

for i in range(uzunluk))

print("rastgele sifre : " , sifre_uret(17))


