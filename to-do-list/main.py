todo = []

while True:
  print("\n1.Gorev Ekle\n2.Gorevleri Gor\n3.Sil\n4.Cikis")
  secim = input("Seciminiz: ")
  
  if secim == '1':
    gorev = input("Yeni Gorev: ")
    todo.append(gorev)

  elif secim == '2':

    for i, g in enumerate(todo, 1):
      print(f"{i}, {g}")

  elif secim == '3':
    sil = int(input("Silmek Istediginiz Gorev Numarasi: "))

    if 0 < sil <= len(todo):
      todo.pop(sil-1)

  elif secim == '4':
    break
    
  else:
    print("gecersiz bir secim yaptinizz !")