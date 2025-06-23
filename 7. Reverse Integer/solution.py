class Solution:
    def reverse(self, x: int) -> int:
        # Violates the assumption that the environment cannot store 64-bit int
        # pos = 1 if x > 0 else 0

        # x = str(abs(x))
        # x = x[::-1]
        # x = int(x)
        
        # x = x if pos else -1 * x
        
        # return 0 if x < -2 ** 31 or x > 2 ** 31 - 1 else x
        # x = 123
        pos = 1 if x > 0 else 0
        x = abs(x)

        y = 0
        while x != 0:
            pop = x % 10
            if y > 2 ** 31 // 10 or (y > (2 ** 31 - 1) // 10 and pop > 7):
                return 0
            y = y * 10 + pop
            x = x // 10
        
        y = y if pos else -1 * y

        return y