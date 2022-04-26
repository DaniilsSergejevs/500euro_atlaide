summa = int(input('Ievadi summu: '))
if summa>=200 and summa<500:
  a = int (summa/100*90)
  print('Pēdeja summa ar 10% atlaidi: ', a)
elif summa>=500:
  a = int (summa/100*80)
  print('Pēdeja summa ar 20% atlaidi: ', a)
else: print('Pēdeja summa bez atlaides: ', summa)