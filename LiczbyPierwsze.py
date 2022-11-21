n = int(input("ile liczbpierwszych mam znaleść? "))

for i in range(2,n+1):
  flaga = True;
  for j in range(2,i):
    if i%j==0:
      flaga = False
      break
  if flaga:
        print(i, end=" ")