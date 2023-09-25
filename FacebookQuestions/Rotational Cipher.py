import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

"""

ascii yontemini denedim olmadı bu yontemi denedim yine olmadı
"""
def rotationalCipher(input_str, rotation_factor):
  # Write your code here
  
  result = ""
  for i in input_str:
    print(i)
    if i.isalnum():
      result+=encrypt_string(i, rotation_factor)
      
    else:
      result+=i
      
      
  return result


def encrypt_string(string, rotationFactor):
  
  result = ""
  for i in string:
    if i.isalpha():
      if i.islower() : 
        result += encode_lower_letters(i, rotationFactor)
      elif i.isupper():
        result += encode_upper_letters(i, rotationFactor)
    elif i.isnumeric():
      result += encode_numbers(i, rotationFactor)
    else:
      result += i

  return result

def encode_lower_letters(string, rotationFactor):
  lower_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  
  try:
    new_index = (lower_letters.index(string) + rotationFactor) % len(lower_letters)
    
    return lower_letters[new_index]
  except:
    print(string, " does not exist")


def encode_upper_letters(string, rotationFactor):
  upper_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]  
  
  try:
    new_index = (upper_letters.index(string) + rotationFactor) % len(upper_letters)

    return upper_letters[new_index]
  except:
    print(string, " does not exist")

def encode_numbers(string, rotationFactor):
  numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  
  try:
    new_index = (numbers.index(string) + rotationFactor) % len(numbers)
    
    return numbers[new_index]
  except:
    print(string, " does not exist")


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

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
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  input_1 = "All-convoYs-9-be:Alert1."
  rotation_factor_1 = 4
  expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
  output_1 = rotationalCipher(input_1, rotation_factor_1)
  check(expected_1, output_1)

  input_2 = "abcdZXYzxy-999.@"
  rotation_factor_2 = 200
  expected_2 = "stuvRPQrpq-999.@"
  output_2 = rotationalCipher(input_2, rotation_factor_2)
  check(expected_2, output_2)

  # Add your own test cases here
  