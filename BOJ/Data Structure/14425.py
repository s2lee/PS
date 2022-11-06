class Trie:
    head = {}

    def add(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['*'] = True

    def search(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]
        if '*' in cur:
            return True
        else:
            return False


n, m = map(int, input().split())
dic = Trie()
for _ in range(n):
    dic.add(input())

cnt = 0
for _ in range(m):
    if dic.search(input()):
        cnt += 1

print(cnt)
