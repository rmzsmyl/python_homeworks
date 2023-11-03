a = "text.txt"

with open(a, "r") as fayl:
    setir = fayl.read().strip()

if setir:
    ilk_index = setir[0]
    son_index = setir[-1]

    print("ilk index:", ilk_index)
    print("son index:", son_index)
else:
    print("fayl boş veya mevcut değil.")