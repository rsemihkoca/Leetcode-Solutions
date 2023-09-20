
# Minimum çözüm

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """        
        Runtime        45 ms        Beats        82.53%

        Memory        17.2 MB        Beats        61.6%
        """
        
        s = s \
        .replace(" ", "") \
        .replace(",", "") \
        .replace(":", "") \
        .replace(".", "") \
        .replace("@", "") \
        .replace("#", "") \
        .replace("_", "") \
        .replace("'", "") \
        .replace("\/", "") \
        .replace("\\", "") \
        .replace("{", "") \
        .replace("}", "") \
        .replace("[", "") \
        .replace("]", "") \
        .replace("\"", "") \
        .replace("--", "") \
        .replace("?", "") \
        .replace(";", "") \
        .replace("-", "") \
        .replace("!", "") \
        .replace("(", "") \
        .replace(")", "") \
        .replace("`", "") \

        s = s.lower()

        return s==s[::-1]



class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Runtime        55 ms        Beats        38.97%
        Memory        22.5 MB        Beats        5.25%
        """
        s = [char.lower() for char in s if char.isalnum()]
    return s == s[::-1]