# #zad.1
# a=int(input())
# b=int(input())
# c=int(input())
# if (b-a)==(c-b):
#   print("ciąg arytmetyczny")

# if (b/a)==(c/b):
#   print("ciąg geometryczny")

# if a<b<c:
#   print("ciąg rosnący")

# if a>b>c:
#   print("ciąg malejący")


# #zad.2
# s=0
# for i in range(100,1000):
#   if i % 8 == 0 and i % 16 != 0:
#     s=s+i
# print(s)


#zad.4
ilosc=0
for i in range(10,100):
  cj=i//10
  cd=i%10
  if cd>=2*cj:
    ilosc=+1
print(ilosc)