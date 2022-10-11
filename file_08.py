pin:int = 1234
probak_szama = 0

while probak_szama < 3 and int(input('PIN: ')) != pin:
    probak_szama += 1
    print('nem jó!')
    if probak_szama != 3:
        print('próbáld újara!')
        print(f'még {3 - probak_szama}x próbálkozhatsz!')

if probak_szama < 3:
    print('Siker!')
else:
    print('elfogytak a lehetőségek, kérem a PUK kódot..')
print('vége')