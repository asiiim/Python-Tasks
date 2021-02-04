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

        found_key = False
        for index, rec in enumerate(bucket):
            rec_key, rec_value = rec

            # Check if the key to be inserted already exists in the bucket
            if rec_key == key:
                found_key = True
                break

        # Update the key value if existing key found else append it in the bucket
        if found_key:
            bucket[index] = (key, value)

        else:
            bucket.append((key, value))
 