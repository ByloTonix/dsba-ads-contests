class Trie:
    def __init__(self):
        self.son = {}
        self.flag = False


def build(words):
    root = Trie()
    for word in words:
        x = root
        for c in word:
            if c not in x.son:
                x.son[c] = Trie()
            x = x.son[c]
        x.flag = True
    return root


def search(text, trie, max_word_len):
    found = set()
    n = len(text)
    for i in range(n):
        x = trie
        for j in range(i, min(i + max_word_len, n)):
            c = text[j]
            if c not in x.son:
                break
            x = x.son[c]
            if x.flag:
                found.add(text[i : j + 1])
    return found


def find(text, words):
    max_word_len = max(len(word) for word in words)
    trie = build(words)
    found = search(text, trie, max_word_len)
    return ["Yes" if word in found else "No" for word in words]


print("\n".join(find(input().strip(), [input().strip() for _ in range(int(input()))])))
