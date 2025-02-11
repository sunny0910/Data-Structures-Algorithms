coins = [1, 3, 4, 5]
amount = 12

def coinChangeRecursive(coins, amount):
    
    if amount < 0:
        return -1
    
    if amount == 0:
        return 0
    
    res = float('inf')
    for c in coins:
        subResult = coinChangeRecursive(coins, amount-c)
        if subResult >= 0 and subResult < res:
            res = subResult + 1
            
    return -1 if res == float('inf') else res

def coinChangeTabu(coins, amount):
    dp = [amount+1] * (amount+1)
    dp[0] = 0
    
    for amt in range(1, amount+1):
        for c in coins:
            if amt-c >= 0:
                dp[amt] = min(dp[amt], 1+dp[amt-c])
    
    return dp[amount] if (dp[amount] != amount+1) else -1

def coinChangeMemo(coins, amount):
    def getMin(coins, amount, dp):
        if amount < -1:
            return -1
        
        if dp[amount] != -1:
            return dp[amount]
        
        res = float('inf')
        for coin in coins:
            sub_result = getMin(coins, amount-coin, dp)
            if sub_result >= 0 and sub_result < res:
                res = sub_result + 1
        
        dp[amount] = -1 if res == float('inf') else res
        return dp[amount]
        
    dp = [-1] * (amount+1)
    dp[0] = 0
    return getMin(coins, amount, dp)

def coinChangeAns(coins, amount):
    res = []
    
    def backtracking1(i, path, total):
        if i>=len(coins) or total>amount:
            return
        
        if total == amount:
            if not res:
                res.append(path.copy())
            elif len(path) < len(res[0]):
                res[0] = path.copy()
            return
        
        path.append(coins[i])
        backtracking1(i, path, total+coins[i])
        
        path.pop()
        backtracking1(i+1, path, total)
    
    def backtracking2(i, path, total):
        if i>=len(coins) or total>amount:
            return
        
        if total == amount:
            if not res:
                res.append(path.copy())
            elif len(path) < len(res[0]):
                res[0] = path.copy()
            return
        
        for i in range(len(coins)):
            path.append(coins[i])
            backtracking2(i, path, total + coins[i])
            path.pop()
    
    currPath = []
    backtracking2(0, currPath, 0)
    return res

print(coinChangeRecursive(coins, amount))
x = coinChangeTabu(coins, amount)
y = coinChangeMemo(coins, amount)
print(x, y)
print(coinChangeAns(coins, amount))