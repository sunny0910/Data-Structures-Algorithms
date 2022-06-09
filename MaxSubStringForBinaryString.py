
all_examples = ["1100011","110111000","1000011", "101011"]

def maxSubArray(binaryString):
    if not binaryString:
        return []
    
    maxCount = 0
    count = 0
    startIndex = -1
    length = 0
    maxLength = 0
    ans= []
    for i, n in enumerate(binaryString):
        if n == '1':
            count += 1
        else:
            count -= 1
        
        length += 1
        
        if startIndex == -1:
            # starting the index again after resetting it
            startIndex = i
        
        if count > maxCount:
            # highest priority of maxCount
            maxCount = count
            maxLength = length
            ans = [binaryString[startIndex:i+1]]
        elif count == maxCount and length > maxLength:
            # if count matched, select the one with max length
            ans = [binaryString[startIndex:i+1]]
            maxLength = length
        elif count == maxCount and length == maxLength:
            # if count and length matches, select both
            ans.append(binaryString[startIndex:i+1])
        
        if count < 0:
            # resetting the count, length and startIndex when count goes negative
            count = 0
            length = 0
            startIndex = -1
            
    return ans

for s in all_examples:
    x = maxSubArray(s)
    print(s, x)