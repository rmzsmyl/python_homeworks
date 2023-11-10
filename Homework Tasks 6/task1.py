import sqlite3
import random

conn = sqlite3.connect('atm.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS ATM (
    id INTEGER PRIMARY KEY,
    kart_nomresi TEXT UNIQUE,
    pin TEXT,
    balans INTEGER
)
''')

conn.commit()
def kart_yarat():
    kart_nomresi = str(random.randint(1000, 9999))
    pin = input('PİN yarat: ')
    balans = 0
    cursor.execute('INSERT INTO ATM (kart_nomresi, pin, balans) VALUES (?, ?, ?)', (kart_nomresi, pin, balans))
    conn.commit()
    print(f'\n Kartınız yaradıldı. Kart nömrəniz: {kart_nomresi}\n')
def balans_goster(kart_nomresi):
    cursor.execute('SELECT balans FROM ATM WHERE kart_nomresi = ?', (kart_nomresi,))
    result = cursor.fetchone()
    if result:
        print(f'Balansınız: {result[0]} AZN\n')
    else:
        print('Hesab tapılmadı.\n')
def withdraw(kart_nomresi, mebleg):
    cursor.execute('SELECT balans FROM ATM WHERE kart_nomresi = ?', (kart_nomresi,))
    result = cursor.fetchone()

    if result:
        balans = result[0]
        if balans >= mebleg:
            yeni_balans = balans - mebleg
            cursor.execute('UPDATE ATM SET balans = ? WHERE kart_nomresi = ?', (yeni_balans, kart_nomresi))
            conn.commit()
            print(f'{mebleg} AZN çıxarıldı. Yeni balansınız: {yeni_balans} AZN\n')
        else:
            print('Balansınızda kifayət qədər məbləğ yoxdur.\n')
    else:
        print('Hesab tapılmadı.\n')
def depozit(kart_nomresi, mebleg):
    cursor.execute('SELECT balans FROM ATM WHERE kart_nomresi = ?', (kart_nomresi,))
    result = cursor.fetchone()
    if result:
        balans = result[0]
        yeni_balans = balans + mebleg
        cursor.execute('UPDATE ATM SET balans = ? WHERE kart_nomresi = ?', (yeni_balans, kart_nomresi))
        conn.commit()
        print(f'{mebleg} AZN artırıldı. Yeni balansınız: {yeni_balans} AZN\n')
    else:
        print('Hesab tapılmadı.\n')
def pin_yeni(kart_nomresi, yeni_pin):
    cursor.execute('UPDATE ATM SET pin = ? WHERE kart_nomresi = ?', (yeni_pin, kart_nomresi))
    conn.commit()
    print('PİN dəyişdirildi.\n')
def exit_atm():
    print('ATM\'dən kartınızı götürün. Təşəkkürlər!\n')
    conn.close()
    exit()
while True:
    print('1. Kart sifariş et')
    print('2. Balansı göstər')
    print('3. Pul çıxart')
    print('4. Pul əlavə et')
    print('5. PİN Dəyişdir')
    print('6. Kartı qaytar')
    choice = input('Əməliyyat seçin: ')
    if choice == '1':
        kart_yarat()
    elif choice == '2':
        kart_nomresi = input('Kart nömrənizi daxil edin: ')
        balans_goster(kart_nomresi)
    elif choice == '3':
        kart_nomresi = input('Kart nömrənizi daxil edin: ')
        mebleg = float(input('Çıxartmaq istədiyiniz məbləği daxil edin: '))
        withdraw(kart_nomresi, mebleg)
    elif choice == '4':
        kart_nomresi = input('Kart nömrənizi daxil edin: ')
        mebleg = float(input('Məbləği əlavə edin: '))
        depozit(kart_nomresi, mebleg)
    elif choice == '5':
        kart_nomresi = input('Kart nömrənizi daxil edin: ')
        yeni_pin = input('Yeni PİN-i yazın: ')
        pin_yeni(kart_nomresi, yeni_pin)
    elif choice == '6':
        exit_atm()
    else:
        print('Düzgün seçim edin.\n')