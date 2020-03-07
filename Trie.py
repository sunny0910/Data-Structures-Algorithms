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
            char = key[level]
            index = self._character_to_index(char)
            if not p_crawl.childrens[index]:
                p_crawl.childrens[index] = self.get_node()
            p_crawl = p_crawl.childrens[index]
        p_crawl.is_end_of_word = True
    
    def search(self, key):
        p_crawl = self.root
        length = len(key)
        for level in range(length):
            char = key[level]
            index = self._character_to_index(char)
            if not p_crawl.childrens[index]:
                return False
            p_crawl = p_crawl.childrens[index]
        return p_crawl.is_end_of_word
    
    def display(self):
        def recur(root, characters, level=0):
            if root.is_end_of_word:
                characters[level] = "\0"
                full_string = ""
                for char in characters:
                    if char == "\0":
                        break
                    full_string += char
                print(full_string)
            for i in range(26):
                if root.childrens[i]:
                    characters[level] = chr(i + ord('a'))
                    recur(root.childrens[i], characters, level+1)

        root = self.root
        characters = [None] * 20
        level = 0
        recur(root, characters, level)


if __name__ == "__main__":
    keys = ["the", "a", "there", "answer", "any", "by", "their"]
    output = ["Not present in trie", "present in trie"]

    t = Trie()
    for key in keys:
        t.insert(key)
    print("===All keys in Trie===")
    t.display()
    print("======")
    print("{} ---- {}".format("the",output[t.search("the")]))
    print("{} ---- {}".format("these",output[t.search("these")]))
    print("{} ---- {}".format("their",output[t.search("their")]))
    print("{} ---- {}".format("thaw",output[t.search("thaw")]))
