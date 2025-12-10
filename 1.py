class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        mod=1337
        result=1
        for digit in b:
            temp = 1
            for _ in range(10):
                temp=(temp * result) % mod
            for _ in range(digit):
                temp=(temp * a) % mod
            result=temp
        return result

class Solution:
    def longestNiceSubstring(self, s: str) ->  str:
        n=len(s)
        answer=""

        for i in range(n):
            char_set=set()
            for j in range(i, n):
                char_set.add(s[j])
                good = True
                for c in char_set:
                    if c.swapcase() not in char_set:
                        good = False
                        break
                if good and (j+1-i)>len(answer):
                    answer = s[i:j+1]

        return answer
