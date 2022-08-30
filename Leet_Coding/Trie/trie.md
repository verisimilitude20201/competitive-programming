              

# Representation
```
                            ""
                        
                         a    b    c
                  
                  
        TrieNode("") -> {TrieNode("a"), TrieNode("b"), TrieNode("c")}  

class TrieNode:
    def __init__(self):
        self.children = dict()
```

# Insert
```
current = root
for char in input_string:
    if char not in current.children:
        current.children[char] = TrieNode()
    current = current.children[char]
```

# Search prefix string

```
current = root
for char in input_string:
    if char not in current.children:
        return False
    current = current.children[char]
```