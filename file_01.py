# integer (egész szám)
a:int = 1984
# floating point number (lebegőpontos szám) "racionális szám"
b:float = 3.1415

print(10 + 3)
print(10 - 3)
print(10 * 3)

print(10 / 3) # "sima" osztás         OP: 3.33333...
print(10 // 3) # "egész" osztás (div) OP: 3
print(10 % 3) # maradékszámítás (mod) OP: 1

print(2 ** 10) # hatványozás          OP: 1024

# numerikus típusok kompatibilisek egymással
print(10 + 3.14)
print(10 / .5)
print(16 ** .5) # "gyökvonás", mert sqrt(x) = x^(1/2)

# string (karakterlánc) "szöveges"
c:str = 'karakterlánc' # vagy "karakterlánc"

print('kutya' + 'ház') # konkatenáció (összefűzés) OP: 'kutyaház
print(3 * 'cica ') # OP: 'cica cica cia '

# Boolean (logikai)
d:bool = True # vagy False

print(True and False) # 'ÉS' OP: F
print(True or False)  # 'VAGY' OP: T
print(not True)       # F

# ------------------------

# ÖSSZEHASONLÍTÓ (compare) operátorok:
# numerikus: <, >, <=, <=
print(10 < 3)     # OP: F
print(10 >= 3)    # OP: T

# általános: ==, !=
# ==: 'egyenlő'
# !=: 'nem egyenlő'

print(5 == 5) # T
print(True != True) # F
print('kutya' == 'dog') # F

#            T
#        F                T
print(10 < 3 or 'macska' != 'kutya') # OP: T