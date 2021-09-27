number_str = input("Find the square root of integer: ")
number_int = int(number_str)
guess_str = input("Initial guess: ")
guess_float = float(guess_str)
tolerance_float = float(input("What tolerance: "))
original_guess_float = guess_float # hang onto the o ri ginal guess
count_int = 0 # count the number of guesses
previous_float = 0 # track the previous calculated value
while (previous_float - guess_float) > tolerance_float:
  previous_float = guess_float
  quotient_float = number_int/guess_float
  guess_float = (quotient_float + guess_float)/2
  count_int = count_int + 1
print("Square root of",number_int," is: ",guess_float)
print("Took ",count_int," reps to get it to tolerance: ",tolerance_float)
print("Starting from a guess of: ", original_guess_float)