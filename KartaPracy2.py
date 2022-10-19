# #zad 2
# n = int(input())
# if n >= 100 and n < 1000 and n % 17 == 0:
#   print("TAK")
# else:
#   print("NIE")

# #zad 3
# n = int(input())
# if n > 18:
#   print("TAK")
# else:
#   print("NIE")

# #zad 4
# LIMIT = 20
# waga = int(input())
# if waga>LIMIT:
#   print("STÓJ")
# else:
#   print("JEDŹ")

# #zad 5
# a = int(input())
# b = int(input())
# c = int(input())
# if (a<c<b) or (b<c<a):
#   print("tak")
# else: 
#   print("nie")

# #zad 6
# a = int(input())
# p = int(input())
# if (a**p-a) % p == 0:
#   print("tak")
# else:
#   print("nie")

#zad 7
start = int(input())
koniec = int(input())
skok = int(input())
odległość=koniec-start
if odległość/skok<=3:
  print("tak")
else:
  print("nie")