class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        flag = 0
        pos = 1
        out = ''

        for i in range(len(s)):
            if flag == 0:
                if s[i] == '-':
                    pos = 0
                    flag = 1
                    continue
                elif s[i] == '+':
                    pos = 1
                    flag = 1
                    continue
                elif s[i].isdigit():
                    flag = 1
                else:
                    break

            if flag == 1:
                if s[i].isdigit():
                    out += s[i]
                else:
                    break

        if not len(out):
            return 0
        else:
            out = int(out) if pos else -1 * int(out)
            # if out < -2 ** 31:
            #     out = -2 ** 31
            # elif out > 2 ** 31 - 1:
            #     out = 2 ** 31 - 1
            out = max(-2 ** 31, min(out, 2 ** 31 - 1))
            return out
