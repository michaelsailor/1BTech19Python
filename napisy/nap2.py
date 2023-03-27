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

# zadanie 4
b=input()
suma=0
for i in b:
  suma=suma+ord(i)
print(suma)