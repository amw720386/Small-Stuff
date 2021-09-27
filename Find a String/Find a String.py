import random
strings_checked = open('Strings.txt','a+')
str_to_find = open('StrToFind.txt','r')
str_to_check = str_to_find.readline()
str_checker = ''
checks = 0
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

while True:
  for num in range(0,6):
    str_checker += random.choice(alphabet)
  checks += 1
  print(str_checker)
  strings_checked.write('\n' + str_checker)  

  if str_checker in strings_checked:
    continue;
  if str_checker == str_to_check:
    break;
  else:
    str_checker = ''

print(f'String, {str_to_check} found took {len(strings_checked)} checks')
