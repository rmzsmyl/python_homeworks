from django.shortcuts import render

# Create your views here.

def index(request):
    mesaj = ''
    exchange_azn = {'usd':0.59, 'eur': 0.54}
    exchange_usd = {'azn':1.7, 'eur': 0.91}
    exchange_eur = {'usd': 1.84, 'azn':1.84}

    if request.method == 'POST':
        al = request.POST['al']
        sat = request.POST['sat']
        miqdar = request.POST['miqdar']
    
        if al == 'azn' and sat == 'usd':
            num = float(miqdar) * exchange_azn['usd']
            mesaj = str(miqdar) + "AZN = " + str(num) + 'USD'
            
        elif al == 'azn' and sat =='eur':
            num = float(miqdar) * exchange_azn['eur']
            mesaj = str(miqdar) + "AZN = " + str(num) + 'EUR'
        
        elif al == 'usd' and sat =='azn':
            num = float(miqdar) * exchange_usd['azn']
            mesaj = str(miqdar) + "USD = " + str(num) + 'AZN'
        
        elif al == 'usd' and sat =='eur':
            num = float(miqdar) * exchange_usd['eur']
            mesaj = str(miqdar) + "USD = " + str(num) + 'EUR'

        elif al == 'eur' and sat =='azn':
            num = float(miqdar) * exchange_eur['azn']
            mesaj = str(miqdar) + "EUR = " + str(num) + 'AZN'

        elif al == 'eur' and sat =='usd':
            num = float(miqdar) * exchange_eur['usd']
            mesaj = str(miqdar) + "EUR = " + str(num) + 'USD'

        context = {
            'mesaj': mesaj
        }

    return render(request, 'index.html', context)