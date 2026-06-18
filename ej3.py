hash_table = [None] * 11
keys = [9, 26, 50, 15, 2, 21, 36, 22, 32]

for key in keys:
    index = key % 11
    while hash_table[index] is not None:
        index = (index + 1) % 11
    hash_table[index] = key
print("Hash table con linear probing:", hash_table)

hash_table_chaining = [[] for _ in range(11)]
for key in keys:
    index = key % 11
    hash_table_chaining[index].append(key)
print("Hash table con separate chaining:", hash_table_chaining)