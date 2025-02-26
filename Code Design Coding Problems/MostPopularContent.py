'''
Imagine you are given a stream of content ids along with an associated action to be performed on them.

Example of contents are video, pages, posts etc. There can be two actions associated with a content id:

increasePopularity → increases the popularity of the content by 1. The popularity increases when someone comments on the content or likes the content
decreasePopularity → decreases the popularity of the content by 1. The popularity decreases when a spam bot's/users comments are deleted from the content or its likes are removed from the content
content ids are positive integers
Implement a class that can return the mostPopular content id at any time while consuming the stream of content ids and its associated action. If there are no contentIds with popularity greater than 0, return -1
'''

class DllNode:
    def __init__(self, freq):
        self.freq = freq
        self.contentIds = set()
        self.prev = self.next = None


class TrendingContent:
    def __init__(self):
        self.contentIdToMap = {}
        self.head = DllNode(None)
        self.tail = DllNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def addNodeToTail(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
    
    def printDll(self):
        curr = self.head.next
        while curr.freq:
            print("freq: {}, ({})".format(curr.freq, curr.contentIds), end=", ")
            curr = curr.next
        print()

    def increasePopularity(self, contentId):
        if contentId not in self.contentIdToMap:
            if self.tail.prev.freq == 1:
                node = self.tail.prev
            else:
                node = DllNode(1)
                self.addNodeToTail(node)
            
            node.contentIds.add(contentId)
            self.contentIdToMap[contentId] = node
        else:
            node = self.contentIdToMap[contentId]
            node.contentIds.remove(contentId)
            if node.prev.freq == node.freq + 1:
                node.prev.contentIds.add(contentId)
                self.contentIdToMap[contentId] = node.prev
            else:
                newNode = DllNode(node.freq + 1)
                newNode.contentIds.add(contentId)
                newNode.next = node
                newNode.prev = node.prev
                node.prev.next = newNode
                node.prev = newNode
                self.contentIdToMap[contentId] = newNode
        # self.printDll()
    
    def decreasePopularity(self, contentId):
        if contentId not in self.contentIdToMap:
            raise KeyError('contentId not found')
        
        node = self.contentIdToMap[contentId]
        node.contentIds.remove(contentId)
        if node.freq > 1:
            if node.next.freq == node.freq - 1:
                node.next.contentIds.add(contentId)
                self.contentIdToMap[contentId] = node.next
            else:
                newNode = DllNode(node.freq-1)
                newNode.contentIds.add(contentId)
                newNode.next = node
                newNode.prev = node.prev
                node.prev.next = newNode
                node.prev = newNode
                self.contentIdToMap[contentId] = newNode
        
        # self.printDll()
    
    def mostPopularContent(self, k=None):
        if not k:
            return next(iter(self.head.next.contentIds))
        output = []
        curr = self.head.next
        while len(output) < k and curr.freq:
            output.extend(list(curr.contentIds))
            curr = curr.next
        
        return output if len(output) <= k else output[:k+1]


tc = TrendingContent()
stream = [('c1', 1),('c2', 1),('c3', 1),('c3', 1),('c3', 1),('c2', 1),('c1', -1),('c4', 1),('c5', 1),('c4', 1),('c3', -1),('c3', -1),('c3', -1)]
for contentId, vote in stream:
    if vote == 1:
        tc.increasePopularity(contentId)
    else:
        tc.decreasePopularity(contentId)
    tc.printDll()
    print(tc.mostPopularContent(2))