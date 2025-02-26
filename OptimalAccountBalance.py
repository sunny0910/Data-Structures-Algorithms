'''
Example 1:

Input: transactions = [[0,1,10],[2,0,5]]
Output: 2
Explanation:
Person #0 gave person #1 10.
Person #2 gave person #0 5.
Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 5 each.

Example 2:

Input: transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
Output: 1
Explanation:
Person #0 gave person #1 10.
Person #1 gave person #0 1.
Person #1 gave person #2 5.
Person #2 gave person #0 5.
Therefore, person #1 only need to give person #0 4, and all debt is settled.
'''
from collections import defaultdict
import heapq


def OptimalAccountBalancing(transactions):
    debts = defaultdict(int)
    for (sender, receiver, amount) in transactions:
        debts[sender] -= amount
        debts[receiver] += amount
    
    print(debts)
    negativeMinHeap, positiveMaxHeap = [], []
    for person, amount in debts.items():
        if amount < 0:
            negativeMinHeap.append([amount, person])
        elif amount > 0:
            positiveMaxHeap.append([-amount, person])
        # ignoring people with 0 debt as they are settled
    
    heapq.heapify(negativeMinHeap)
    heapq.heapify(positiveMaxHeap)
    print(negativeMinHeap, positiveMaxHeap)

    totalTransactions = 0
    while negativeMinHeap and positiveMaxHeap:
        maxReceiverAmount, maxReceiver = heapq.heappop(negativeMinHeap)
        maxSenderAmount, maxSender = heapq.heappop(positiveMaxHeap)
        maxSenderAmount *= -1
        
        transactionValue = maxSenderAmount + maxReceiverAmount
        print(maxSenderAmount, maxReceiverAmount, transactionValue)
        owedAmount = 0
        if transactionValue == 0:
            owedAmount = maxReceiverAmount
        elif transactionValue > 0:
            owedAmount = maxReceiverAmount
            heapq.heappush(positiveMaxHeap, [-transactionValue, maxSender])
        else:
            owedAmount = maxSenderAmount
            heapq.heappush(negativeMinHeap, [transactionValue, maxReceiver])
    
        totalTransactions += 1
        print("{} sent {} to {}".format(maxSender, owedAmount, maxReceiver))

    return totalTransactions
        

transactions = [
    [[0,1,10],[2,0,5]],
    [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
    ]

for transaction in transactions:
    print(OptimalAccountBalancing(transaction))