# Create the hash table class with chaining
class ChainingHashTable:
    # Create a constructor
    def __init__(self, initial_capacity=40):
        # initialize the hash table with empty bucket list entries
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # insert a new item or update existing to the hash table
    def insert(self, key, item):
        # get the bucket list where this item will go
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # insert the item to the end of the bucket list
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # searches for item with matching key in hash table
    # returns the item if found or None if not found
    def search(self, key):
        # get the bucket list where this item would be
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for key_value in bucket_list:
            # find the item's index and then return the item that is in the bucket list
            if key_value[0] == key:
                return key_value[1]
            else:
                return None

    # removes the item with matching key from the hash table
    def remove(self, key):
        # get the bucket list where this item will be removed from
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove item from bucket list if key is present
        for key_value_pair in bucket_list:

            if key_value_pair[0] == key:
                bucket_list.remove([key_value_pair[0], key_value_pair[1]])
