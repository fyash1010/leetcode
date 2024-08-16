# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         return s == s[::-1]
    
#     def longestPalindrome(self, s: str) -> str:
#         out = s[0]

#         for a in range(len(s)):
#             for b in range(a, len(s)):
#                 if self.isPalindrome(s[a:b+1]):
#                     if len(s[a:b+1]) > len(out):
#                         out = s[a:b+1]
        
#         return out


# Researched "Expand Around Center" algorithm for simplification:
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundIndex(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        out = s[0]

        for a in range(len(s)):
            expandedStrOdd = expandAroundIndex(a, a)
            expandedStrEven = expandAroundIndex(a, a + 1)

            out = expandedStrOdd if len(expandedStrOdd) > len(out) else out
            out = expandedStrEven if len(expandedStrEven) > len(out) else out

        return "" if len(s) == 0 else out