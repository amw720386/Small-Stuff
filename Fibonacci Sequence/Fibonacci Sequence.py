terms = int(input("How many terms would you like in your fibonacci sequence?\n"))
num = 1
total = 0
term_counter = 0
sequence = ""
sequence_list = {0:0}

while not term_counter == terms:
  sequence += str(sequence_list[term_counter]) + ' + '
  total += sequence_list[term_counter]
  term_counter += 1   
  sequence_list[term_counter] = num
  num += sequence_list[term_counter - 1]

print(f'{sequence[0:-2]} = {total}')
