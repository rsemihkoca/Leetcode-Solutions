class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        min_value = 101

        stack = []
        result = [0] * len(temperatures)


        for key, value in enumerate(temperatures):


            while stack and value > stack[-1][1]:

                last_item = stack.pop()
                result[last_item[0]] = key - last_item[0]
            
            min_value = value
            stack.append((key,value))

        return result