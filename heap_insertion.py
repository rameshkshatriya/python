class heap:
    def __init__(self):
        self.maxsize = 10
        self.data = [-1] * self.maxsize
        self.idx = 0

    def __len__(self):
        return len(self.data)

    def isempty(self):
        return len(self.data) == 0

    def insert(self,e):
        if self.idx == self.maxsize == 0:
            print("heap has no space")
            return
        self.idx = self.idx + 1
        a = self.idx
        while a > 1 and e > self.data[a//2]:
            self.data[a] = self.data[a//2]
            a = a//2
        self.data[a] = e

    def max(self):
        if self.idx == 0:
            print("heap is empty")
            return
        return self.data


s = heap()
s.insert(25)
s.insert(26)
s.insert(24)
print(s.data)
