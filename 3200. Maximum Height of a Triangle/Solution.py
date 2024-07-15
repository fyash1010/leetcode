class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        redHeight = 0
        blueHeight = 0
        rRed = red
        rBlue = blue
        
        layer = 1
        # CASE1: Red first
        while (rRed >= layer):
            rRed = rRed - layer
            layer += 1
            redHeight += 1
            if rBlue >= layer:
                rBlue = rBlue - layer
                layer += 1
                redHeight += 1
            else:
                break
            
        layer = 1
        # CASE2: Blue first
        while (blue >= layer):
            blue -= layer
            layer += 1
            blueHeight += 1
            if red >= layer:
                red -= layer
                layer += 1
                blueHeight += 1
            else:
                break
            
        return max(redHeight, blueHeight)