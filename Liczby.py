# n = int(input("do ilu mam znaleść liczby pierwsze? "))

# for i in range(2,n+1):
#   flaga = True;
#   for j in range(2,i):
#     if i%j==0:
#       flaga = False
#       break
#   if flaga:
#         print(i, end=" ")

# #od n do e liczb 1
# n = int(input()) 
# e = int(input()) 

# for i in range(n,e+1):
#   flaga = True;
#   for j in range(2,i):
#     if i%j==0:
#       flaga = False
#       break
#   if flaga:
#         print(i, end=" ")

# #NWD no.1
# a=int(input())
# b=int(input())
# while a!=b:
#  if a>b:
#   a=a-b
#  elif b>a:
#   b=b-a
# if a==b:
#   print(a)

# #NWD no.2
# a=int(input())
# b=int(input())
# while b>0:
#   a = b
#   b = a%b
# print(a)

# #NWW no.1
# a=int(input())
# b=int(input())
# iloczyn=a*b
# while a!=b:
#  if a>b:
#   a=a-b
#  elif b>a:
#   b=b-a
# if a==b:
#   print(iloczyn/a)

# #NWW no.2
# a=int(input())
# b=int(input())
# iloczyn=a*b
# while b>0:
#   a, b = b, a%b
# print(iloczyn//a)

#funkcja ord() - zwraca kod ASCII znaku
#kod ASCI dla dużych liter jest od 65 do 90
#funkcja chr() zwraca znak dla danego kodu

# #zad test (wypisz duże A-Z)
# for i in range(65,91):
#   print(chr(i))
  
#string w pythonie - tablica
# napis = "polska"
# print(napis[0], napis[1], napis[2])

# for i in range(len(napis)):
#   print(napis[i], end="")

# #szyfr cezara
# napis=input()
# szyfr=""
# for i in range(len(napis)):
#   szyfr=szyfr+chr(65+ ((ord(napis[i])-65+3) %26))
# print(szyfr)

#dodawanie ułamków ???????
a=int(input("licznik ułamku nr.1  "))
b=int(input("mianownik ułamku nr.1  "))
c=int(input("licznik ułamku nr.2  "))
d=int(input("mianownik ułamku nr.2  "))
nww=0
iloczyn=b*d
while b!=d:
 if b>d:
  b=b-d
 elif d>b:
  d=d-b
nww=iloczyn//b
x=(nww//b)*a
y=(nww//d)*c
z=x+y
print(f"{a}/{b} + {c}/{d} = {x}/{nww} + {y}/{nww} = {z}/{nww}")