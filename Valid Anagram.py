class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)
    


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(s)==Counter(t):
            return True
        return False    


Counter("")  RETURN True OR False