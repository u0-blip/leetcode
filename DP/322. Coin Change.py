"""You are given coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1."""


import numpy as np
class Solution:
    
    def recur(self, amount):
        if amount < 0:
            return False
        if amount in self.sub_change:
            return self.sub_change[amount]

        sub_problem = amount - self.coins

        sub_problem = sub_problem[sub_problem >= 0]

        res = []
        changes = []

        for i, s in enumerate(sub_problem):
            if s == 0:
                return 1
            a = self.recur(s)
            self.sub_change[s] = a

            if a is not False:
                changes.append(a)

        if len(changes) > 0:
            self.sub_change[amount] = min(changes) + 1
        else:
            return False

        # print(amount, self.sub_change[amount])
        return self.sub_change[amount]

    def coinChange(self, coins, amount) -> int:
        if len(coins)==0:
            return -1
        if amount == 0:
            return 0

        self.coins = np.array(coins)
        self.sub_change = dict()
        for c in coins:
            self.sub_change[c] = 1
        a = self.recur(amount)
        return a if a != False else -1


# much fast BFS solution
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        value1 = [0]
        value2 = []
        nc =  0
        visited = [False]*(amount+1)
        visited[0] = True
        while value1:
            nc += 1
            for v in value1:
                for coin in coins:
                    newval = v + coin
                    if newval == amount:
                        return nc
                    elif newval > amount:
                        continue
                    elif not visited[newval]:
                        visited[newval] = True
                        value2.append(newval)
            value1, value2 = value2, []
        return -1
        


s = Solution()
coins = [186,419,83,408]

amount = 6249
print(s.coinChange(coins, amount))