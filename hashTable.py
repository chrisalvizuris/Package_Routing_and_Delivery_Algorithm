# Create the hash table class with chaining
"""
Create a custom hash table with methods to use the object (insert, search, delete, update). This will be used to store the
packages and later retrieve specific data.
"""


class ChainingHashTable:
    def __init__(self, initial_capacity=40):
        """
        O(N)

        This constructor will initialize the hash table with empty bucket list. This will be an array of arrays.

        :param initial_capacity: The initial capacity is set to 40 because that is the number of packages in the csv
        """
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def insert(self, key, item):
        """
        O(1)

        This function will let us insert items into the hash table. It will take in a key and then the item being
        inserted.

        The key will get hashed using the modulo of the table size.

        :param key: The key used to hash. This will be the package ID
        :param item: The package being inserted into the hash table
        :return: Returns True if something has been inserted.
        """
        # get the bucket list where this item will go
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # insert the item to the end of the bucket list
        # for kv in bucket_list:
        #     if kv[0] == key:
        #         kv[1] = item
        #         return True
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    def search(self, key):
        """
        O(N)

        This function searches for item with matching key in hash table and returns the value (similar to a dictionary)

        :param key: The package ID
        :return: Return's the package object being searched or None
        """
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

    def remove(self, key):
        """
        O(N)

        This function removes the item with matching key from the hash table.

        :param key: The package ID
        :return: Does not return anything.
        """
        # get the bucket list where this item will be removed from
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove item from bucket list if key is present
        for key_value_pair in bucket_list:

            if key_value_pair[0] == key:
                bucket_list.remove([key_value_pair[0], key_value_pair[1]])

    def update(self, key, item):
        """
        O(N)
        This function searches for the key in the parameter and then updates the item with the item being passed.

        :param key: Key of the item in the hash table
        :param item: Item that will replace the existing item
        :return: Returns true.
        """
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_value_pair in bucket_list:

            if key_value_pair[0] == key:
                key_value_pair[1] = item
                return True
