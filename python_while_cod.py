# >>>
cars = ['cobalt','centra','damaz','nexia','centra','malibu']
while 'centra' in cars:
    cars.remove('centra')
print(cars)

# >>>
print("Do'stlaringiz haqida malumot to'playmiz: ")
dostlar = {}
n = 1
while True:
    ism = input(f"{n} - do'stingiz ismi? ")
    yosh = input(f"{ism.title()}nig yoshi?  ")
    dostlar[ism] = int(yosh)
    n += 1
    jovob = input("Yana qo'shasizmi? (ha/yoq)")
    if jovob != 'ha':
        break
for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")
print(dostlar)


# >>>
buyurtmalar1 = []
n = 1
while True:
    print("Kafega hush kelibsiz! Nima buyurtma qilasiz?")
    buyurtmalar = input(f"{n} - buyurtmani kiriting: ")
    buyurtmalar1.append(buyurtmalar)
    n += 1
    sorov = input('Yana buyurtma berasizmi? (ha/yoq)')
    if sorov != 'ha':
        break

print("\nSizning buyurtmangiz: ")
for royxat in buyurtmalar1:
    print(royxat.title())


# >>>
son = 1
while son <= 5:
    print(son, end=' ')
    son += 1
print('\nDastur tugadi')

# >>>
sonlar = list(range(2,10))
for son in sonlar:
    if son == 10:
        break # break > sindirish, continue > bir qadam otkazib yuboradi
    print(f"{son} ning kvadrati {son**2} ga teng")

# >>>
son = 0
while son < 10:
    son += 1
    if son % 2 != 0:
        continue
    print(son)
