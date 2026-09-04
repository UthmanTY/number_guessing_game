def score_calculator(max_attempt, attempts_used, difficulty_multiplier):
  total = (max_attempt - attempts_used + (1 / (difficulty_multiplier ** 2))) * (difficulty_multiplier * 100)
  return total
