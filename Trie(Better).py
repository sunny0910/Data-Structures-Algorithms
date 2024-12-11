from collections import defaultdict
class TrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)
        self.endOfWord = False

class Trie:
    def __init__(self) -> None:
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()
    
    def insert(self, folder):
        nodePointer = self.root
        folderPath = folder.split('/')
        # print(folderPath)
        for i in range(1, len(folderPath)):
            folderKey = folderPath[i]
            child = nodePointer.children[folderKey]
            nodePointer = child
        nodePointer.endOfWord = True
    
    def print(self):
        def recur(root, allKeys = []):
            if root.endOfWord:
                folderPath = '/' + '/'.join(allKeys)
                # print(folderPath)
                return
            
            keys = root.children.keys()
            for key in keys:
                # print(key)
                allKeys.append(key)
                recur(root.children[key], allKeys)
                allKeys.remove(key)
        
        allKeys = []
        recur(self.root, allKeys)
    
    def removeSubFolders(self, root):
        def recur(root, values):
            if root.endOfWord:
                folder = ''.join(values)
                result.append(folder)
                return
            for key, childNode in root.children.items():
                values.append('/'+key)
                recur(childNode, values)
                values.pop()
        values = []
        result = []
        recur(self.root, values)
        return result
    
inputs = [
    ["/a","/a/b","/c/d","/c/d/e","/c/f"],
    ["/a","/a/b/c","/a/b/d"],
    ["/a/b/c","/a/b/ca","/a/b/d"],
    ["/a/b/c","/a/b/ca","/a/b/d", "/a/b"],
    ["/a/b/ca/b","/a/b/ca/d","/a/c/d/a", "/a/b", "/a/c/d", "/a"]
]
for input in inputs:
    t = Trie()
    for folder in input:
        t.insert(folder)
    result = t.removeSubFolders(t.root)
    print(input, " ==> ", result)
# t.print()