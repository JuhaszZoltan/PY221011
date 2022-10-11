jegy:int = int(input('milyen jegyet kaptál? '))

if   jegy == 1: print('elégtelen')
elif jegy == 2: print('elégséges')
elif jegy == 3: print('közepes')
elif jegy == 4: print('jó')
elif jegy == 5: print('jeles')
else:           print('nincs ilyen osztályzat!')