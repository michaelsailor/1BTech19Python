# #zad.1

# n=int(input())
# suma=0
# while n>0:
#   cyfra=n%10
#   suma+=cyfra
#   n=n//10
# print(suma)

#zad.2
n = int(input())
for i in range(2, n):
  if n % i == 0:
    print("TAK")
