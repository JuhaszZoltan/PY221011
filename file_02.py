jegy:int = int(input('milyen jegyet kaptál? '))

if jegy == 1:
    print('elégtelen')
else:
    if jegy == 2:
        print('elégséges')
    else:
        if jegy == 3:
            print('közepes')
        else:
            if jegy == 4:
                print('jó')
            else:
                if jegy == 5:
                    print('jeles')
                else:
                    print('nincs ilyen osztályzat!')