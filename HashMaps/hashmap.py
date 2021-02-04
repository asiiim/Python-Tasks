import logging
class HashTable:

    # Lets create empty list of given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    
    def create_buckets(self):
        return [[] for _ in range(self.size)]

    
    # Set value in the hash maps
    def set_value(self, key, value):
        
        # Using hash method to generate index from the given key
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to the generated index
        bucket = self.hash_table[hashed_key]

        gotten = False
        for index, rec in enumerate(bucket):
            rec_key, rec_value = rec

            # Check if the key to be inserted already exists in the bucket
            if rec_key == key:
                gotten = True
                bucket[index] = (key, value)
                return "Updated !"

        if not gotten:
            bucket.append((key, value))
            return "Value is set !"
    
    # Search the value and return it with specific key
    def get_value(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        gotten = False
        for index, rec in enumerate(bucket):
            rec_key, rec_value = rec

            if rec_key == key:
                gotten = True
                return rec_value
        if not gotten:
            return "Not Found."


    # Remove value of the specific key 
    def remove_value(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        gotten = False
        for index, rec in enumerate(bucket):
            rec_key, rec_value = rec

            if rec_key == key:
                gotten = True
                bucket.pop(index)
                return "Removed."
        if not gotten:
            return "No Value to be removed."


    # Print the items of the hash map
    def __str__(self):
        return "".join(str(hsh) for hsh in self.hash_table)


# Get size for the hash
hash_size = int(input("Size: "))

# Get hash table
hash_table = HashTable(hash_size)
print(f"{hash_table}\n")

# Get value and set in the hash table
key_value = input("Key: ")
content_value = input("Content: ")
print(hash_table.set_value(key_value, content_value))

# Seach with key
result = hash_table.get_value(key_value)
print("Gotcha >>> " + str(result))

# Remove with key
print(hash_table.remove_value(key_value))