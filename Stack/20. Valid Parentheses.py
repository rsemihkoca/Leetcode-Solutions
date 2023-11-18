class Solution:
    def isValid(self, s: str) -> bool:
        """
        Runtime
        Details
        38ms
        Beats 59.24%of users with Python3
        Memory
        Details
        16.21MB
        Beats 53.49%of users with Python3
        """

        stack = []

        mapping = {
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }

        for char in s:

            if char in mapping:
                stack.append(char)
            elif stack and char == mapping[stack[-1]]:
                stack.pop()
            else:
                return False
        return not stack
