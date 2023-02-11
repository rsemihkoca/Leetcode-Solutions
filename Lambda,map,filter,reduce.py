square = lambda n: n ** 2

# Calling lambda function
square(5)

maxi = lambda x, y: x if x > y else y
maxi(4, 6)




#FILTER VE REDUCE MANTIKLI OLABİLİR FILTER: CUSTOM FUNCTIONA GÖRE SEÇİM YAPAR
def find_odd(x):
    if x % 2 != 0:
        return x
nums = [1, 34, 23, 56, 89, 44, 92]
odds = list(filter(find_odd, nums))
print(odds)
# Output: [1, 23, 89]

nums = [1, 34, 23, 56, 89, 44, 92]
odds = list(filter(lambda x: x % 2 != 0, nums))
print(odds)
# Output: [1, 23, 89]

#REDUCE  ITERATIVE OLARAK CUMULATİF İŞLEM YAPAR VE TEK DEĞER DÖNDÜRÜR


The simpler answers already given may well suit your needs, but the reduce command is very powerful at applying a rolling computation sequentially to pairs of numbers in a list.

def multiply(*args):
    return reduce((lambda x, y: x * y), args)