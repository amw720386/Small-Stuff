num = input('Input number: ')
slices = 0
index = 0

if len(num) > 3:
  num += ','
  while num.find(',') > 3:
    num = num[:num.find(',') -3] + ',' + num[num.find(',') -3:]
  print(num[0:-1])  
 else:
  print(num)