class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word):
        def _delete(node, word, depth):
            if depth == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0
            
            char = word[depth]
            if char not in node.children:
                return False
            
            should_delete_current_node = _delete(node.children[char], word, depth + 1)
            
            if should_delete_current_node:
                del node.children[char]
                return len(node.children) == 0
            
            return False
        
        _delete(self.root, word, 0)

    def get_words_with_prefix(self, prefix):
        def _collect_words(node, prefix, words):
            if node.is_end_of_word:
                words.append(prefix)
            for char, child_node in node.children.items():
                _collect_words(child_node, prefix + char, words)
        
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        words = []
        _collect_words(node, prefix, words)
        return words

# Example usage
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("apricot")
trie.insert("banana")

# Search
print(trie.search("app"))  # True
print(trie.search("apple"))  # True
print(trie.search("appl"))  # False

# Prefix matching
print(trie.starts_with("app"))  # True
print(trie.starts_with("ban"))  # True
print(trie.starts_with("bat"))  # False

# Get words with prefix
print(trie.get_words_with_prefix("ap"))  # ['apple', 'app', 'apricot']
print(trie.get_words_with_prefix("b"))  # ['banana']

# Deletion
trie.delete("app")
print(trie.search("app"))  # False
print(trie.search("apple"))  # True
