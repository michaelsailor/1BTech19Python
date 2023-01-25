#PRE
# from math import gcd
# print(gcd(20,15)))

 #1 wybór liczb pierwszych
p=11
q=13
 #2 obliczenie n=p*q i funkcji Eulera f=(p-1)*(q-1)
n=p*q
f=(p-1)*(q-1)
print(n)
print(f)
 #3 generujemy klucz publiczny E taki, że NWD(E,f)=1
from math import gcd
for i in range(2,f):
  if gcd(i,f)==1:
    e=i
    break
print(e,n)
 #generujemy klucz prywatny D taki, że (d*e)%f=1
for j in range(2,f):
  if ((j*e)%f)==1:
    d=j
    break
print(d,n)

#Przykład RSA
#m - moja wiadomość
#c=m**e%n (zaszyfrowane - cypher)
#t=c**d%n (odszyfrowane - txt)
m=input()
for i in m:
  print((ord(i)**e)%n)

m=input()
for i in range(m):
  cypher+=chr((ord(i)**e)%n)