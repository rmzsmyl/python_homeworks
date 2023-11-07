from datetime import datetime
from datetime import timedelta
from datetime import date


def yas_hesabla(dogum_tarixi):
    indi = datetime.now()
    ferq = indi - dogum_tarixi
    yas = ferq.days // 365
    muddet = datetime(indi.year, dogum_tarixi.month, dogum_tarixi.day)
    if muddet < indi:
        muddet = datetime(indi.year + 1, dogum_tarixi.month, dogum_tarixi.day)
    qalangun = (muddet - indi).days
    saniye = ferq.total_seconds()
    deqiqe = saniye / 60
    saat = deqiqe / 60
    gun = ferq.days
    ay = (yas * 12) + (datetime.now().month - dogum_tarixi.month)

    return yas, gun, ay, saat, deqiqe, saniye, qalangun

def main():
    dogum_gunu = input("Doğum tarixinizi (YYYY-MM-DD) formatında yazın: ")
    dogum_tarixi = datetime.strptime(dogum_gunu, "%Y-%m-%d")
    
    yas, gun, ay, saat, deqiqe, saniye, qalangun = yas_hesabla(dogum_tarixi)
    
    print(f"""
          Siz heyatta 
          {saniye:.0f} saniye, 
          {deqiqe:.0f} deqiqe, 
          {saat:.0f} saat, 
          {gun} gün, 
          {ay} aydır yasayirsiniz.
          Və sizin {yas} yaşınız var.
          Doğum gününüzə isə {qalangun} gün qaldı.
          """)

if __name__ == "__main__":
    main()
