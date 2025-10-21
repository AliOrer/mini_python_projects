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


    """
    gorevler = []  # 'todo'yu 'gorevler' yaptım, tutarlılık için.

while True:
  print("\n1. Gorev Ekle\n2. Gorevleri Gor\n3. Sil\n4. Cikis")
  secim = input("Seciminiz: ")
  
  if secim == '1':
    gorev = input("Yeni Gorev: ")
    if gorev.strip():  # Boş girişi önle
      gorevler.append(gorev)
    else:
      print("Gorev bos olamaz!")
  elif secim == '2':
    if not gorevler:
      print("Liste bos!")
    else:
      for i, g in enumerate(gorevler, 1):
        print(f"{i}. {g}")
  elif secim == '3':
    try:
      sil = int(input("Silmek Istediginiz Gorev Numarasi: "))
      if 0 < sil <= len(gorevler):
        gorevler.pop(sil-1)
        print("Gorev silindi!")
      else:
        print(f"Gecersiz numara! Lutfen 1 ile {len(gorevler)} arasinda bir sayi girin.")
    except ValueError:
      print("Lutfen gecerli bir sayi girin!")
  elif secim == '4':
    print("Cikis yapiliyor...")
    break
  else:
    print("Gecersiz bir secim yaptiniz!")

    """