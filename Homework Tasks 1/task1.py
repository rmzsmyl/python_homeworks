adlar = {
    "Aslan": "emi ogludur",
    "Imran": "dayi ogludur",
    "Afaq": "bibi qizidir",
    "Uzeyir": "xala ogludur",
    "Shahin": "yaxin dostdur"
}

a = input("Ad daxil edin: ")

if a in adlar:
    print(adlar[a])
elif a == "":
    print("Siz ad daxil etmediniz ")
else:
    print("kimdir? Men onu tanimadim")
