import random

while True:
    zar = random.randint(1, 6)
    print('zar sonucu', zar)
    devam = input('tekrar atmak ister misin? (e/h): ')
    if devam.lower() != 'e':
        break