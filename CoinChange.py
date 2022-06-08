coins = [1,3,4,5]
amount = 7

def getMinCoins(coins, amount):
    if amount < 0:
        return -1
    if amount == 0:
        return 0
    res = float('inf')
    
    for coin in coins:
        subResult = getMinCoins(coins, amount-coin)
        if subResult >= 0 and subResult < res:
            res = subResult + 1
    
    return -1 if res == float('inf') else res

def getMinCoins(coins, amount):
    dp = [amount+1] * (amount+1)
    dp[0] = 0
    for amt in range(1, amount+1):
        for c in coins:
            if amt-c >= 0:
                dp[amt] = min(dp[amt], 1+dp[amt-c])
    return dp[-1]

def getMinCoinsArray(coins, amount):
    res = []
    def recur(i, currentCoins, total):
        if total>amount:
            return
        if total == amount:
            if not res or len(currentCoins) < len(res[0]):
                while res:
                    res.pop()
                res.append(currentCoins.copy())
            elif len(res[-1]) == len(currentCoins):
                res.append(currentCoins.copy())
            return
        
        for i in range(len(coins)):
            currentCoins.append(coins[i])
            recur(i, currentCoins, total+coins[i])
            currentCoins.pop()
    
    currentCoins = []
    recur(0, currentCoins, 0)
    return res

m = getMinCoins(coins, amount)
print(m)
a = getMinCoinsArray(coins, amount)
print(a)