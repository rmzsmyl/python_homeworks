a = {
    "key1": "value1",
    "key2": "value2",
}

secim = input("Daxil edin - 1 Keys, 2 Values: ")

if secim == "1":
    print("Keys:", a.keys())
elif secim == "2":
    print("Values:", a.values())
else:
    print("Melumat daxil etmediniz!")