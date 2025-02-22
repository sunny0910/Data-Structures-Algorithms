# autocomplete using Trie
import collections
class TrieNode:
    def __init__(self) -> None:
        self.endOfWord = True
        self.children = collections.defaultdict(TrieNode)
        # store the function name that are part of this node
        self.childFunctions = set()
        
    def __repr__(self) -> str:
        return str(self.childFunctions)

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root
        
        for w in word:
            current = current.children[w]
            current.childFunctions.add(word)
        
        current.endOfWord = True

class FunctionManager:
    def __init__(self) -> None:
        self.trie = Trie()
    
    def addFunction(self, functionName):
        self.trie.insert(functionName)
    
    def printNode(self, node, char=None):
        print(char, node)
        for key, child in node.children.items():
            self.printNode(child, key)
    
    def getMatches(self, input):
        result = []
        def recur(node: TrieNode, input, index):
            if index >= len(input):
                # reached the end of input and can return the function names part of this node
                result.extend(list(node.childFunctions))
                return
            
            # if first char or small case char and not in node.children, return
            if (index == 0 or input[index].islower()) and input[index] not in node.children:
                return
            
            # first char or lower char should always have a node value
            if index == 0 or input[index].islower():
                return recur(node.children[input[index]], input, index+1)
            else:
                # for index>1 and capital character, we can traverse all small case nodes to check all functionName to find occurrance of capital char
                for key, value in node.children.items():
                    if input[index] in value.children:
                        # if char is present, call on it's child nodes
                        recur(value.children[input[index]], input, index+1)
                    else:
                        # else call on all child nodes and backtrack
                        recur(value, input, index)
                return
        recur(self.trie.root, input, 0)
        return result

fm = FunctionManager()
fm.addFunction('Container')
fm.addFunction('Panel')
fm.addFunction('AutoPanel')
fm.addFunction('RidePrinter')
fm.addFunction('ResumePanel')
fm.addFunction('RegularContainer')
fm.addFunction('RegularContainerBall')
# fm.printNode(fm.trie.root)

print(fm.getMatches("R"))       # ["RegularContainerBall","ResumePanel", "RidePrinter", 'RegularContainer']
print(fm.getMatches("Re"))      # ['RegularContainerBall', "ResumePanel", "RegularContainer"]
print(fm.getMatches("RP"))      # ["RidePrinter", "ResumePanel"]
print(fm.getMatches("RPr"))     # ["RidePrinter"]
print(fm.getMatches("RCB"))     # ["RegularContainerBall"]
print(fm.getMatches("RCoBa"))   # ["RegularContainerBall"]
