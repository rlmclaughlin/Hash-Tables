


class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value



class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
       

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
    new_pair = Pair(key, value)

    if hash_table.storage[index] != None:
        if key == hash_table.storage[index].key:
            print(f"Collision detected for {key} and {hash_table.storage[index].key}")
        else:
            hash_table.storage[index].value = value
    else:
        hash_table.storage[index] = new_pair


def hash_table_remove(hash_table, key):
    hash_key = hash(key)
    index = hash_key % hash_table.capacity
    print(index)
    if hash_table.storage[index] != None:
        hash_table.storage[index] = None
          
    else:
        print(f"{key} not found in hash table, cannot be removed.")



def hash_table_retrieve(hash_table, key):
    hash_key = hash(key)
    index = hash_key % hash_table.capacity
    if hash_table.storage[index] != None:
        if hash_table.storage[index].key == key:
            return hash_table.storage[index].value
    
    return None




def Testing():
    ht = HashTable(2)

def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here's the goods \n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")



Testing()