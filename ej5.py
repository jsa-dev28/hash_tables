class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)  # Modifica el valor existente
                return
        self.buckets[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return None  # Retorna None si la clave no existe

    def display(self):
        for i, bucket in enumerate(self.buckets):
            print(f"Bucket {i}: {bucket}")

hash_map = HashMap()
hash_map.put("100", "Ciento")
hash_map.put("200", "Doscientos")
hash_map.put("300", "Trescientos")
hash_map.put("100", "Cien")  # Modifica el valor asociado a la clave "100"
hash_map.display()
print("Valor asociado a '100':", hash_map.get("100"))
print("Valor asociado a '200':", hash_map.get("200"))
print("Valor asociado a '400':", hash_map.get("400"))  # La clave no existe, por esto retorna None

