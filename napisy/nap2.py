# #palindrom za pomocą tablicy
# s = input()
# for i in range(len(s)//2):
#   if s[i] != s[len(s)-1-i]:
#     exit("NIE")
# exit("TAK")


#anagramy
a=input()
b=input()
A=list(a)
B=list(b)
A.sort()
B.sort()
if A==B:
  print("TAK")
else:
  print("NIE")