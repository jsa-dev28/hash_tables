hash_codes = [217, 209, 265, 226, 234, 201, 207, 223]
hash_table = [[] for _ in range(8)]
for code in hash_codes:
    index = code % 8
    hash_table[index].append(code)
    chain_lengths = [len(bucket) for bucket in hash_table]
print("Longitudes de las cadenas en la hash table:", chain_lengths)