# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows == 1 or numRows >= len(s):
#             return s
        
#         out = []
#         for y in range(1, numRows + 1):
#             count = 1
#             flag = 0
#             for x in range(len(s)):
#                 if count == y:
#                     out.append(s[x])
#                 count += 1 if flag == 0 else -1
#                 flag = 1 if count >= numRows else 0 if count <= 1 else flag
            
#         return "".join(out)

# Researched algorithm for simplification:
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        out = []
        for x in range(numRows):
            for y in range(x, len(s), 2 * (numRows - 1)):
                out.append(s[y])
                if x > 0 and x < numRows - 1 and y + (2 * (numRows - 1) - (2 * x)) < len(s):
                    out.append(s[y + (2 * (numRows - 1) - (2 * x))])
        
        return ''.join(out)