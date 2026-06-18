class HashSet:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def add(self, key):
        index = self.hash_function(key)
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key):
        index = self.hash_function(key)
        if key in self.buckets[index]:
            self.buckets[index].remove(key)

    def contains(self, key):
        index = self.hash_function(key)
        return key in self.buckets[index]

    def display(self):
        for i, bucket in enumerate(self.buckets):
            print(f"Bucket {i}: {bucket}")

hash_set = HashSet()
hash_set.add("100")
hash_set.add("200")
hash_set.add("300")
hash_set.add("100")  # No se agregará un duplicado
hash_set.display()
print("Contiene '100':", hash_set.contains("100"))
hash_set.remove("100")
print("Contiene '100':", hash_set.contains("100"))
hash_set.display()