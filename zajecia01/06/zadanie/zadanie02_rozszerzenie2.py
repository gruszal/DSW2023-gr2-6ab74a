imiona = ['Artur', 'Barbara', 'Czesław']

print(imiona)

nowe_imie = input('Proszę podać nowe imię: ')

if nowe_imie and nowe_imie not in imiona:
    imiona.append(nowe_imie)
else:
    print(f'Imię "{nowe_imie}" nie zostanie dodane')

print(sorted(imiona))
