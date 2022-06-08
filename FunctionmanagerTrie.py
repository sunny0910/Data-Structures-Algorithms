#FunctionmanagerTrie
import collections
class Node:
    def __init__(self) -> None:
        self.hashMap = collections.defaultdict(Node)
        self.isVarTrue = []
        self.isVarFalse = []
    
    def __repr__(self) -> str:
        return 'hashMap: ' + str(self.hashMap) + '\n' + 'isVarTrue: ' + str(self.isVarTrue) + '\n' + 'isVarFalse: ' + str(self.isVarFalse)
        
class Trie:
    def __init__(self) -> None:
        self.root = Node()
    
    def insert(self, name, arguments, isVariadic):
        current = self.root
        
        for argument in arguments:
            current = current.hashMap[argument]
        
        if isVariadic:
            current.isVarTrue.append(name)
        else:
            current.isVarFalse.append(name)

    def isSame(self, arguments, argument):
        for arg in arguments:
            if arg != argument:
                return False
        
        return True
        
    def match(self, arguments):
        result = []
        start = self.root
        
        for i, argument in enumerate(arguments):
            if argument not in start.hashMap:
                return result
            else:
                if i != len(arguments)-1 and len(start.hashMap[argument].isVarTrue) > 0:
                    if self.isSame(arguments[i:], argument):
                        result.append(start.hashMap[argument].isVarTrue)
                    
                if i == len(arguments)-1:
                    if len(start.hashMap[argument].isVarTrue) > 0:
                        result.append(start.hashMap[argument].isVarTrue)
                    if len(start.hashMap[argument].isVarFalse) > 0:
                        result.append(start.hashMap[argument].isVarFalse)
                            
            start = start.hashMap[argument]
        
        return result
    
t=Trie()
t.insert("FuncA", ["String", "Integer", "Integer"], False)
t.insert("FuncB", ["String", "Integer"], True)
t.insert("FuncC", ["Integer"], True)
t.insert("FuncD", ["Integer", "Integer"], True)
t.insert("FuncE", ["Integer", "Integer", "Integer"], False)
t.insert("FuncF", ["String"], False)
t.insert("FuncG", ["Integer"], False)
print(t.root)

print("Print match")
print(t.match(["String"])) #[FuncF]
print(t.match(["Integer"])) #[FuncC, FuncG]
print(t.match(["Integer", "Integer", "Integer", "Integer"])) #[FuncC, FuncD]
print(t.match(["Integer", "Integer", "Integer"])) #[FuncC, FuncD, FuncE]
print(t.match(["String", "Integer", "Integer", "Integer"])) #FuncB
print(t.match(["String", "Integer", "Integer"])) #FuncA,FuncB }}}
