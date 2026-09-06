def get_valid_number(max_number):
    while True:
        try:
            guess = int(input())
            if guess >= 1 and guess <= max_number:
                return guess
            else:
                print("Invalid number! Please enter a number within the range.")
        except ValueError:
            print("Invalid input! Please enter a number.")
          
def score_calculator(max_attempt, attempts_used, difficulty_multiplier):
  total = (max_attempt - attempts_used + 1) * difficulty_multiplier
  return total
