def vurma(x, y):
    return x * y
def bolme(x, y):
    if y == 0:
        return "0'a bölmək mümkün deyil"
    else:
        return x / y
def toplama(x, y):
    return x + y
def cixma(x, y):
    return x - y
while True:
    try:
        print("Vurma (1)")
        print("Bölmə (2)")
        print("Toplama (3)")
        print("Çıxma (4)")
        secim = input("Aparmaq istədiyiniz əməliyyatı seçib, enteri vurun (1/2/3/4): ")

        if secim not in ['1', '2', '3', '4']:
            print("Seçim yanlışdır (1/2/3/4)")
            continue

        reqem1 = float(input("Birinci sayıyı girin: "))
        reqem2 = float(input("İkinci sayıyı girin: "))

        if secim == '1':
            print(f"Cavab: {reqem1} * {reqem2} = {vurma(reqem1, reqem2)}")
        elif secim == '2':
            sonuc = bolme(reqem1, reqem2)
            if type(sonuc) == str:
                print(f"Error Mesajı: {sonuc}")
            else:
                print(f"Cavab: {reqem1} / {reqem2} = {sonuc}")
        elif secim == '3':
            print(f"Cavab: {reqem1} + {reqem2} = {toplama(reqem1, reqem2)}")
        elif secim == '4':
            print(f"Cavab: {reqem1} - {reqem2} = {cixma(reqem1, reqem2)}")

    except ValueError:
        print("Rəqəm daxil edin")
