import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def findEncryptedWord(s):
  # Write your code here
  
  
  if len(s) <= 2:
    return "".join(s)
  result = ""
  
  index_of_middle = find_middle(s)
    
  left_side = s[:index_of_middle]
  
  right_side = s[index_of_middle+1:]
  
  
  result += s[index_of_middle] + findEncryptedWord(left_side) + findEncryptedWord(right_side)
  return result
  

def find_middle(li:list) -> int:
  
  
  left = 0
  right = len(li)-1
  
  mid = (left + right) // 2
  
  return mid










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
  s1 = "abc"
  expected_1 = "bac"
  output_1 = findEncryptedWord(s1)
  check(expected_1, output_1)

  s2 = "abcd"
  expected_2 = "bacd"
  output_2 = findEncryptedWord(s2)
  check(expected_2, output_2)

  # Add your own test cases here
  