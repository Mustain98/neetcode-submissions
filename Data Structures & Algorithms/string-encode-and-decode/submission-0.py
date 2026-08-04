class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs)):
            res += str(len(strs[i]))
            res += '#'
            res += strs[i]
        return res

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            r = ""
            j = i

            while True:
                if s[j] != '#':
                    r += s[j]
                    j += 1
                else:
                    break

            r = int(r)
            strs.append(s[j + 1:j + 1 + r])
            i = j + 1 + r

        return strs