from collections import defaultdict
from abc import ABC, abstractmethod


class AtlassianRouter(ABC):
    @abstractmethod
    def withRoute(self, route, value):
        pass
    @abstractmethod
    def route(self, route, root=None):
        pass

class TrieNode:
    def __init__(self, value=None):
        self.children = defaultdict(TrieNode)
        self.value = value

class Trie:
    def __init__(self):
        self.root = TrieNode()

class Router(AtlassianRouter):
    def __init__(self):
        self.trie = Trie()
    
    def validateRoute(self, route):
        if route[0] != '/':
            return Exception("Route should start with /")
        return

    def withRoute(self, route, value):
        self.validateRoute(route)
        route = route.split('/')
        curr = self.trie.root
        for i in range(1, len(route)):
            curr = curr.children[route[i]]
        
        curr.value = value
    
    def route(self, route, root=None):
        self.validateRoute(route)
        route = route.split('/')
        if not root:
            curr = self.trie.root
        else:
            curr = root
        
        for i in range(1, len(route)):
            if route[i] == '*':
                for child in curr.children.values():
                    result = self.route(''.join(['/']+route[i+1:]), child)
                    if result:
                        return result
            if route[i] not in curr.children:
                return None
            
            curr = curr.children[route[i]]
        
        return curr.value

router = Router()
router.withRoute("/bar", "result")
print(router.route("/bar"), "result")

router.withRoute("/bar/abc", "abc")
print(router.route("/bar/abc"), "abc")
print(router.route("/bar/abc/dd"), None)
router.withRoute("/bar/abc/dd", "dd")
# router.withRoute("/bar/abc/cde/dd") -> "ee"	
print(router.route("/bar/abc/dd"), "dd")
print(router.route("/bar/*/dd"), "dd")
'''
Router.withRoute("/bar", "result")
Router.route("/bar") -> "result"

Router.withRoute("/bar/abc", "abc")
Router.route("/bar/abc") -> "abc"
Router.route("/bar/abc/dd") -> null	

Router.withRoute("/bar/abc/dd", "dd")
Router.withRoute("/bar/abc/cde/dd") -> "ee"	
Router.route("/bar/abc/dd") -> "dd"	
Router.route("/bar/*/dd") -> "dd"
'''