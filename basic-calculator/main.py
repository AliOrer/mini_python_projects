#basit hesap makinesi

def toplama(a, b):
  return a+b

def cikarma(a, b):
  return a-b

def carpma(a, b):
  return a*b

def bolme(a, b):
  return a/b if b != 0  else "sıfıra bölünemez!"
    
while True:
  print('yapmak istediginiz islemi secin :')
  print("1. toplama \n2.cikarma\n3.carpma\n4.bolme\n5 cikis")
  secim = input("seciminiz : ")
  
 if secim == '5':
    print("çıkılıyor...")
    break
  
  a = float(input("birinci sayi: "))
  b = float(input("ikinci sayi: "))
  
  if secim == '1': print(toplama(a,b))
  elif secim == '2': print(cikarma(a,b))
  elif secim == '3': print(carpma(a,b))
  elif secim == '4': print(bolme(a,b))
  else : print("gecersiz secim!!!")