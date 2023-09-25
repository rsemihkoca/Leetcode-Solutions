import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def matching_pairs(s, t):
  """
  assumed set of strings are identical"""
  # Write your code here
  
  initial_matching_number = sum(1 for i,j in zip(s,t) if i==j)
  
  s_sorted = sorted(s)
  t_sorted = sorted(t)
  
  sorted_matching_number = sum(1 for i,j in zip(s_sorted,t_sorted) if i==j)

    
  return calculate_pairs(sorted_matching_number, initial_matching_number)

def calculate_pairs(sorted_matching_number, initial_matching_number):
  
  difference = sorted_matching_number - initial_matching_number
  
  if difference == 0:
    return initial_matching_number - 2
  if difference == 1:
    return initial_matching_number
  if difference == 2:
    return initial_matching_number + 2
  if difference >= 2:
    return initial_matching_number + 2











# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  s_1, t_1 = "abcde", "adcbe"
  expected_1 = 5
  output_1 = matching_pairs(s_1, t_1)
  check(expected_1, output_1)

  s_2, t_2 = "abcd", "abcd"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)

  # Add your own test cases here
  