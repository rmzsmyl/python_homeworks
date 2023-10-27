login = input("Login daxil edin: ")
parol = input("Parol daxil edin: ")

if not login or not parol:
    if not login and not parol:
        print("Login ve parol daxil etmediniz")
    elif not login:
        print("Login daxil etmediniz")
    elif not parol:
        print("Parol daxil etmediniz")
else:
    if login == "test" and parol == "12345":
        print("Xosh geldiniz")
    elif login == "test":
        print("Parol yanlishdir")
    elif parol == "12345":
        print("Login yanlishdir")
    else:
        print("Login ve parol yanlishdir")
