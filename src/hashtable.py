# import bcrypt
# import hashlib

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        # self.count = 0
        


    def _hash(self, key):

        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        # def hash(key) :
        #     hash_value = 0
        #     for char in key:
        #         hash_value += ord(char)
            
        #     return hash_value

        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass
        


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity
        


    def insert(self, key, value):
        
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.

        '''
        # if self.count >= self.capacity:
        #     self.resize()

        index = self._hash_mod(key)
        if self.storage[index] == None:
            self.storage[index] = LinkedPair(key, value)
        else: 
            pair = self.storage[index]
            while pair.next != None and pair.key != key:
                pair = pair.next
            
            if pair.key == key:
                pair.value = value
            else:
                pair.next = LinkedPair(key, value)
        
        # self.count += 1
        



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        pair = self.storage[index]
        prev_pair = None

        while pair != None and pair.key != key:
            prev_pair = pair
            pair = pair.next

        if pair != None:
            if pair.next == None and prev_pair == None:
                self.storage[index] = None
            
            elif pair.next == None and prev_pair != None:
                prev_pair.next = None
            
            else:
                prev_pair.next = pair.next

        # self.count -= 1
                

    #     if self.storage[self._hash_mod(key)] == None:
    #         print("warning")
    #     else:
    #         self.storage[self._hash_mod(key)] = None


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        pair = self.storage[index]
        while pair != None:
            if pair.key == key:
                return pair.value
            pair = pair.next
        
        return None
        # return self.storage[self._hash_mod(key)]


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity
        old_storage = self.storage
        self.storage = new_storage

        for i in range(len(old_storage)):
            if old_storage[i] != None:
                pair = old_storage[i]
                while pair != None:
                    self.insert(pair.key, pair.value)
                    pair = pair.next
        # for x in [i for i in self.storage if i != None]:
        #     new_storage[self._hash_mod(x.key)] = LinkedPair(x.key, x.value)
        
        # self.storage = new_storage



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
