class DSU:
    def __init__(self):
        self.parent = [0] * 105
        self.size = [0] * 105

    def make_set(self, v):
        self.parent[v] = [v, 0]
        self.size[v] = 1

    def find_set(self, v):
        if self.parent[v][0] != v:
            len = self.parent[v][1]
            self.parent[v] = self.find_set(self.parent[v][0])
            self.parent[v][1] += len
        return self.parent[v].copy()

    def union(self, a, b):
        a = self.find_set(a)[0]
        b = self.find_set(b)[0]

        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.parent[b] = [a, 1]
            self.size[a] += self.size[b]

if __name__ == "__main__":
  dsu = DSU()
  for i in range(1, 10):
    dsu.make_set(i)

  dsu.union(1, 2)
  dsu.union(3, 4)
  dsu.union(5, 6)
  dsu.union(3, 5)
  dsu.union(1, 3)
  dsu.find_set(6)
  print()


