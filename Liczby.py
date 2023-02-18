#sprawdź czy wpisana liczba jest liczbą pierwszą
# n = int(input("Podaj liczbę: "))
# if n<=2:
#   print("NIE")
# else:
#   for i in range(2, n):
#     if n % i == 0:
#       print("NIE")
#       break
#   else:
#     print("TAK")

# #n = int(input("do ilu mam znaleść liczby pierwsze? "))
# for i in range(2,n+1):
#   flaga = True;
#   for j in range(2,i):
#     if i%j==0:
#       flaga = False
#       break
#   if flaga:
#     print(i, end=" ")

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
#     print(i, end=" ")

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

# #NWW no.3
# a=int(input())
# b=int(input())
# from math import gcd
# iloczyn=a*b
# NWD=gcd(a,b)
# NWW=iloczyn//NWD
# print(NWW)

#funkcja ord() - zwraca kod ASCII znaku
#kod ASCI dla dużych liter jest od 65 do 90
#funkcja chr() zwraca znak dla danego kodu

# #zad test (wypisz duże A-Z)
# for i in range(65,91):
#   print(chr(i))
  
# #string w pythonie - tablica
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


# #dodawanie ułamków 
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# from math import gcd
# x, y = b, d
# iloczyn = x*y
# nwd=gcd(x,y)
# nww=iloczyn//nwd
# e=(nww//b)*a
# f=(nww//d)*c
# g=e+f
# print(f"{g}/{nww}")

