class TrieNode:
    def __init__(self):
        self.childrens = [None]*26
        self.is_end_of_word = False
    
class Trie:
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def _character_to_index(self, char):
        return ord(char) - ord('a')

    def insert(self, key):
        p_crawl = self.root
        length = len(key)
        for level in range(length):
            index = self._character_to_index(key[level])
            if not p_crawl.childrens[index]:
                p_crawl.childrens[index] = self.get_node()
            p_crawl = p_crawl.childrens[index]
        p_crawl.is_end_of_word = True
    
    def search(self, key):
        p_crawl = self.root
        length = len(key)
        for level in range(length):
            index = self._character_to_index(key[level])
            if not p_crawl.childrens[index]:
                return False
            p_crawl = p_crawl.childrens[index]
        return p_crawl.is_end_of_word if p_crawl else None
    
    def display(self):
        def recur(root, char_str, level=0):
            if not root:
                return
            if root.is_end_of_word:
                char_str[level] = "\0"
                op = ""
                for char in char_str:
                    if char == "\0":
                        break
                    if char:
                        op += char
                print(op)
            for i in range(26):
                if root.childrens[i]:
                    char_str[level] = chr(i + ord('a'))
                    recur(root.childrens[i], char_str, level+1)

        root = self.root
        char_str = [None] * 20
        level = 0
        recur(root, char_str, level)


keys = ["the", "a", "there", "answer", "any", "by", "their"]
output = ["Not present in trie", "present in trie"]

t = Trie()
for key in keys:
    t.insert(key)
t.display()
print("{} ---- {}".format("the",output[t.search("the")])) 
print("{} ---- {}".format("these",output[t.search("these")])) 
print("{} ---- {}".format("their",output[t.search("their")])) 
print("{} ---- {}".format("thaw",output[t.search("thaw")])) 