pwd:str = 'Password123'
proba: str = '---'
while proba != pwd:
    proba = input('add meg a jelszót!')
    if proba != pwd:
        print('ez nem jött össze, próbáld újra!')

print('Sikeresen bejelentkeztél!')