class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_val = 0
        stack = []

        for height in heights:
            total_area = 0
            total_area += height

            pair = [height,total_area]

            k = len(stack) - 1
            while stack and k>=0:

                elem = stack[k]
                if elem[0] <= height:
                    elem[1] += elem[0]
                    max_val = max(max_val, elem[1])
                else:
                    #stack.pop()
                    pair[1] += pair[0]
                k -= 1


            stack.append(pair)
            print(height, ":", stack)



            max_val = max(max_val, pair[1])

        return max_val
    # [2,0,2]
    # [3,6,5,7,4,8,1,0] kalıyor