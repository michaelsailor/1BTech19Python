# //Wygeneruj tablicę n losowych liczb:
from random import randint
L = [randint(1,21) for i in range(20)]
print(L) 
#1
print(max(L))
#2
print(min(L))
#3
print(L.count(max(L)))
#4
print(L.count(min(L)))

# 1. Znajdź największą liczbę w tablicy
# 2. Znajdź najmniejszą liczbę w tablicy
# 3. Podaj ile razy występuje najwieksza liczba w tablicy
# 4. Podaj ile razy występuje najmniejsza liczba w tablicy
# 5. Podaj rozpiętość tablicy (różnica max - min)
# 6. Podaj sumę liczb w tablicy
# 7. Podaj średnią wartość liczb w tablicy
# 8. Których liczb jest więcej w tablicy: parzystych czy nieparzystych?
# 9. Ile w tablicy jest liczb pierwszych?
# 10. Podaj v-ce max i v-ce min liczb tablicy