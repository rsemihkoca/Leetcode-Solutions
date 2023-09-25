import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
# def calcUser(gr, t):
  
#   return gr**t

# def getBillionUsersDay(growthRates):
#   # Write your code here
  
#   t = 1
#   N = 0
#   while N<=1000000000:
#     t += 1
#     sum_value = 0
    
#     users = [calcUser(i, t) for i in growthRates]
    
#     sum_value = sum(users)
#     N += sum_value
#     print(N)
    
#   return t 
    
def calcUser(gr, t):
    
    return gr**t

def getBillionUsersDay(growthRates):
  # Başlangıç ve bitiş aralığını belirle
    left = 1
    right = 11**3  # Büyük bir sayı kullanabiliriz

    while left <= right:
        t_mid = (left + right) // 2
        user = 0
        total_users = 0
        for gr in growthRates:
            user = calcUser(gr, t_mid)
            total_users += user
            
        if total_users < 10**9:
            left = t_mid + 1
        else:
            right = t_mid -1

    return left



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
  test_1 = [1.1, 1.2, 1.3]
  expected_1 = 79
  output_1 = getBillionUsersDay(test_1)
  check(expected_1, output_1)

  test_2 = [1.01, 1.02]
  expected_2 = 1047
  output_2 = getBillionUsersDay(test_2)
  check(expected_2, output_2)

  # Add your own test cases here