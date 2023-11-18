import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        if len(tokens) ==1 : return int(tokens[0])
        stack = []
        operators = {

            '+' : operator.add, 
            '-' : operator.sub, 
            '*' : operator.mul, 
            '/' : operator.truediv
        }

        for key, value in enumerate(tokens):

            if value in operators:
                a = int(stack.pop())
                b = int(stack.pop())
                # truediv and int() guarentees truncate toward zero
                result = int(operators[value](b, a))
                stack.append(result)
            else:
                stack.append(int(value))
        return result
        


        