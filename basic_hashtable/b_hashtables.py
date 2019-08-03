


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None



class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.original_capacity = capacity
        self.storage = [None] * capacity
        self.count = 0


def hash(string):
    hash = 5381
    for x in string:
        hash = ((( hash << 5) + hash) + ord(x)) & 0xFFFFFFFF
    return hash


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    hash_key = hash(key)
    index = hash_key % hash_table.capacity

    if hash_table.storage[index] != None:
        if key == hash_table.storage[index].key:
            hash_table.storage[index].value = value
        else:
            current_linked_pair = hash_table.storage[index]
            while current_linked_pair.next != None:
                current_linked_pair = current_linked_pair.next
            if current_linked_pair.key == key:
                current_linked_pair.value = value
            else:
                new_linked_pair = LinkedPair(key, value)
                current_linked_pair.next = new_linked_pair
    
    else:
        new_linked_pair = LinkedPair(key, value)
        hash_table.storage[index] = new_linked_pair
    hash_table.count += 1
  
    if hash_table.count >= hash_table.capacity * 0.7:
        new_capacity = hash_table.capacity * 2
        new_storage = [None] * new_capacity
        for i in range(0, hash_table.capacity):
            if hash_table.storage[i] is not None:
                # Hash key for new index
                index = hash(hash_table.storage[i].key) % new_capacity
                new_storage[index] = hash_table.storage[i]
        hash_table.storage = new_storage
        hash_table.capacity = new_capacity


def hash_table_remove(hash_table, key):
    hash_key = hash(key)
    index = hash_key % hash_table.capacity
    print(index)
    if hash_table.storage[index] != None:
        if hash_table.storage[index].key == key:
            hash_table.storage[index] = hash_table.storage[index].next
            return
        
        if hash_table.storage[index].next != None:
            current_linked_pair = hash_table.storage[index]
            while current_linked_pair != None:
                if current_linked_pair.next.key == key:
                    current_linked_pair.next = current_linked_pair.next.next
                    hash_table.count -= 1
                    return
                current_linked_pair = current_linked_pair.next

    else:
        print(f"{key} not found in hash table, cannot be removed.")
    if hash_table.count <= hash_table.capacity * 0.2 and hash_table.capacity > hash_table.original_capacity:
        new_capacity = hash_table.capacity / 2
        new_storage = [None] * new_capacity
        for i in range(0, hash_table.capacity):
            if hash_table.storage[i] is not None:
                index = hash(hash_table.storage[i].key) % new_capacity
                new_storage[index] = hash_table.storage[i]
        hash_table.storage = new_storage
        hash_table.capacity = new_capacity


def hash_table_retrieve(hash_table, key):
    hash_key = hash(key)
    index = hash_key % hash_table.capacity
    if hash_table.storage[index] != None:
        if hash_table.storage[index].key == key:
            return hash_table.storage[index].value
        
        if hash_table.storage[index].next != None:
            current_linked_pair = hash_table.storage[index].next
            while current_linked_pair != None:
                if current_linked_pair.key == key:
                    return current_linked_pair.value
                current_linked_pair = current_linked_pair.next
    
    else:
        print(f"{key} not found in hash table, cannot be removed.")


def hash_table_resize(hash_table):
    new_hash_table = HashTable(hash_table.capacity * 2)
    new_hash_table.storage = [None] * new_hash_table.capacity
    for i in range(len(hash_table.storage)):
        new_hash_table.storage[i] = hash_table.storage[i]
        hash_table.storage[i] = None
    return new_hash_table


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Small hash table")
    hash_table_insert(ht, "line_2", "Hash table is far beyond its capacity")
    hash_table_insert(ht, "line_3", "Linked List")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")

Testing()