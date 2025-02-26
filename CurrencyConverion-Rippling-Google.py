'''
You are given the following parameters:


Rates: ['USD', 'JPY', 110] ['US', 'AUD', 1.45] ['JPY', 'GBP', 0.0070]
To/From currency ['GBP', 'AUD']
Find the rate for the 'To/From' curency. In this case, the correct result is 1.89.
'''


from collections import defaultdict, deque
def currecyConversion(rates, queries):
    graph = defaultdict(dict)
    for src, des, cost in rates:
        graph[src][des] = cost
        graph[des][src] = 1/cost
    
    output = [-1.0] * len(queries)
    print(graph)
    for i, (src, des) in enumerate(queries):
        if src not in graph or des not in graph:
            continue

        q = deque([(src, 1.0)])
        seen = set()
        while q:
            node, cost = q.popleft()
            if node == des:
                output[i] = cost
                break

            seen.add(node)
            for nei in graph[node]:
                if nei not in seen:
                    q.append((nei, cost * graph[node][nei]))
    
    return output

rates = [['USD', 'JPY', 110], ['USD', 'AUD', 1.45], ['JPY', 'GBP', 0.0070]]
queries =  [['GBP', 'AUD']]

print(currecyConversion(rates, queries))