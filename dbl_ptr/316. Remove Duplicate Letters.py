import numpy as np
from collections import Counter

class Solution:
    def recur(self, s, c):
        if s == '':
            return ''
        pos = 0
        for i, char in enumerate(s):
            if s[pos] > char:
                pos = i
            c[char] -= 1
            if c[char] == 0:
                break
        
        return s[pos] + self.recur(s[pos+1:].replace(s[pos], ''), c)

    def removeDuplicateLetters(self, s: str) -> str:
        if s == '':
            return ''
        c = Counter([*s])
        
        return self.recur(s, c)

s = Solution()
a = "bcabc"
print(s.removeDuplicateLetters(a))


""" 
It is not too difficult, but I didn't understand the greedy algorithm very much,
I don't know how to prove it gives the best answer
"""