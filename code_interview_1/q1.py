
def word_in(sorted_w, w_c, chars, count_chars):
    p1 = 0
    p2 = 0
    while p1 < len(sorted_w):
        while p2 < len(chars) and chars[p2] < sorted_w[p1] :
            p2 += 1
        if p2 >= len(chars):
            return False

        if w_c[sorted_w[p1]] > count_chars[sorted_w[p1]]:
            return False
        p1 += 1
    print(sorted_w)
    return True

class Solution:
    def countCharacters(self, words, chars) -> int:
        if len(words) == 0 or len(chars) == 0:
            return 0
        from collections import Counter
        import numpy as np

        count_chars = Counter(chars)
        chars = np.unique(sorted(chars))

        print(count_chars)
        total_len = 0

        for word in words:
            w_c = Counter(word)
            sorted_w = np.unique(sorted(word))
            
            if word_in(sorted_w, w_c, chars, count_chars):
                total_len += len(word)

        return total_len
            
words = ["hello","world","leetcode"]
chars = "welldonehoneyr"

s = Solution()
print(s.countCharacters(words, chars))