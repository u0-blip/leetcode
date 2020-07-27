class Solution:
    def letterCasePermutation(self, S: str):
        if len(S) == 0:
            return ''
        letters = [ele for ele in S if ele.isalpha()]
        pos = [i for i, c in enumerate(S) if c.isalpha()]
        num = [ele for ele in S if ele.isnumeric()]

        diff_perm = 2**len(pos)

        letters_uplow = [[ele.upper(), ele.lower()] for ele in letters]
        import itertools
        comb = [[*S] for i in range(diff_perm)]

        for i, p in enumerate(itertools.product(*letters_uplow)):
            for j, ele in enumerate(p):
                comb[i][pos[j]] = ele
        return [''.join(ele) for ele in comb]
        
s = Solution()
a = 'f12d'
print(s.letterCasePermutation(a))

''' 
this is very easy, have no problem with it
basically take all the alpha values out and turn that into product fo iteration
'''