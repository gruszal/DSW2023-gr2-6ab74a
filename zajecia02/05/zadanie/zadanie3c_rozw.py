import datetime

samochod = {'marka': 'Fiat',
            'model': '126p',
            'rocznik': 1973,
            'czy_oryginalny': True}

print(samochod)

aktualny_rok = datetime.date.today().year

# czy może być zarejestrowany jako pojazd zabytkowy?
if aktualny_rok - samochod['rocznik'] >= 25:
    if samochod['czy_oryginalny']:
        print('Twój {} może być zarejestrowany jako zabytek.'.format(samochod['marka']))
    else:
        print('Twój {} nie jest oryginalny :('.format(samochod['marka']))
else:
    print('Twój {} jest zbyt młody :)'.format(samochod['marka']))