# #palindrom za pomocą tablicy
# s = input()
# for i in range(len(s)//2):
#   if s[i] != s[len(s)-1-i]:
#     exit("NIE")
# exit("TAK")


# #anagramy
# a=input()
# b=input()
# A=list(a)
# B=list(b)
# A.sort()
# B.sort()
# if A==B:
#   print("TAK")
# else:
#   print("NIE")

# #zadanie 1
# L=input()
# print(L[0])
# print(L[len(L)-1])

# #zadanie 2
# x=input()
# print(x[1:len(x)-1])

# #zadanie 3
# a=input()
# A=list(a)
# A.reverse()
# for i in range(4):
#   print(A[i])

# # zadanie 4
# b=input()
# suma=0
# for i in b:
#   suma=suma+ord(i)
# print(suma)

# # 5. Policz ile we wpisanym napisie jest liter A.
# e=input()
# ilość=0
# for i in e:
#   if i == "a" or i == "A":
#     ilość+=1
# print(ilość)

# # 6. Podaj dominującą literkę we wpisanym napisie. 
# # Niech to będzie tylko jedna literka.
# g=input()
# domin=0
# for i in g:
#   if g.count(i)>domin:
#     domin=g.count(i)
#     literka=i
# print(literka, domin)

# 7. Znajdź literkę-dominantę w napisie (może ich być kilka, a może nie być żadnej)


# 8. Sprawdź czy w napisie występują trzy podciągi "LA"
e=input()
print(e.count("LA"))



# 9. Znajdź "średnią literkę" w napisie. (Przejdź na kody ASCII i jeśli wynik będzie
# ułamkowy to zaokrąglij średnią w dół)

# 10. Wypisz literki, których nie ma w napisie

# 11. Znajdź ilość trzyznakowych palindromów w napisie (trzy literki koło siebie)




T = [500, 200, 100, 50, 20, 10, 5, 2, 1]
x = int(input())
W = []
for i in T:
    ilosc = x//i
    if ilosc >0:
        x = x - ilosc * i 
        for j in range(ilosc):
            W.append(i)
print(W)