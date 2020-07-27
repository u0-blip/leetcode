# %%|
import numpy as np
line = 'some line with text'
words = line.split(' ')
length = [len(w) for w in words]
max_arg = np.argmax(length)
line = words[max_arg]
print(line, end="")

# %%
import sys
import numpy as np

lookup = [np.binary_repr(ele, width=5) for ele in range(2**5)]
exit_all = False

def recur(card_left, val, dp, cards):
    global exit_all
    if exit_all:
        return False

    # print(np.binary_repr(card_left, width=5), val)
    if dp[card_left, val-1] != np.inf:
        return dp[card_left, val-1]
    elif card_left == 0 and val == 0:
        exit_all = True
        return True
    elif card_left == 0 and val != 0:
        return False

    else:
        left = np.binary_repr(card_left, width=5)
        
        res = False
        for i, l in enumerate(left):
            if l == '0':
                continue
            if i == len(left)-1:
                _left = left[:i] + '0'
            elif i < len(left)-1:
                _left = left[:i] + '0' + left[i+1:]
            _card_left = lookup.index(_left)
            
            _val = [0 for i in range(3)]
            _val[0] = val - cards[i]
            _val[1] = val + cards[i]
            _val[2] = int(val / cards[i])
            

            for v in _val:
                _res = recur(_card_left, v, dp, cards)
                if _res:
                    exit_all = True
                dp[_card_left, v-1] = _res
                # print(_res)
                res ^= np.bool(_res)
            
        dp[card_left, val-1] = res
        return res
                
line = '40 1 3 4 20'
cards = line.strip().split(' ')
cards = [int(ele) for ele in cards]

# the worse condiction would be 52, 51, 50, 49, 48
dp = np.ones((int(2**5), 250))*np.inf
for c in cards:
    dp[1, c] = True

res = recur(31, 42, dp, cards)
# print(dp)
if res == True:
    line = 'YES'
else:
    line = 'NO'
    
print(line, end="")

""" n: card numbers, v values, worse conditon max value: k
time complexity: O(2^n)
space complexity: O(n*k)
"""
# %%
