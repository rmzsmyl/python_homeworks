name_list = []

while True:
    name = input("Ad daxil edin: ")

    if not name:
        print("Ad daxil etmediniz ")
    elif len(name) > 15:
        print("Ad cox uzundur maksimum 15 herf")
    else:
        name_list.append(name)
        print("Ad Bazaya ugurla elave olundu. ")
