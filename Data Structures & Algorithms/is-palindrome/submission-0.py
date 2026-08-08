class Solution:
    def isPalindrome(self, s: str) -> bool:
        word=[]
        for a in s:
            if a.isalnum():
                word.append(a.lower())
        
        return word == word[::-1]