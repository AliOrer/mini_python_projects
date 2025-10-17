import random

secenekler = ["tas", "kagit", "makas"]

while True:
  kullanici = input("tas, kagit veya makas? : ").lower()
  bilgisayar = random.choice(secenekler)
  print("bilgisayar: ", bilgisayar)
  
  if kullanici == bilgisayar:
    print("berabere")
    elif (kullanici == "tas" and bilgisayar == "makas") or \
         (kullanici == "kagit" and bilgisayar == "tas") or \
         (kullanici == "makas" and bilgisayar == "kagit"):
           print("kazandiniz!!!")
           else:
             print("kaybettiniz!!!")
      # TODO: write code...