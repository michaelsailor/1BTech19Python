#string to prawie lista
 #konwersja lista <-> napis( list(), join() )
# s=input()
# L=list(s)
# print(s,L)
# L.sort()
# print(s,L)
# s="".join(L)
# print(s)

#sprawdź czy słowoto palindromem
s=input()
L=list(s)
X=L.copy()
L.reverse()
if L==X:
  print("TAK")
else:
  print("NIE")