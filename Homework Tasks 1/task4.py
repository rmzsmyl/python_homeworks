boy = float(input("Boy (metr): "))
ceki = float(input("Çəki (kiloqram): "))

bki = ceki / (boy * boy)

if bki < 18.5:
    print("Zəif")
elif 18.5 <= bki < 25:
    print("Normal")
elif 25 <= bki < 30:
    print("Kilolu")
else:
    print("Obez")
