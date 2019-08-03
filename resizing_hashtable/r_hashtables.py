class LinkedPair:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None

class HashTable:
  def __init__(self, capacity):
    self.storage = [None] * capacity
    self.capacity = capacity
    self.count = 0


def hash(string, max):
  hash = 5381
  
  for character in string:
    hash = ((hash << 5) + hash) + ord(character)
   
  return hash % max


def hash_table_insert(hash_table, key, value):
  index = hash(key, hash_table.capacity)
  print(f"Insert Print Statement {key} {index}")

  current_pair = hash_table.storage[index]

  while current_pair is not None and current_pair.key != key:
    current_pair = current_pair.next
  
  if current_pair is None:
    new_pair = LinkedPair(key, value)
    old_head = hash_table.storage[index]
    hash_table.storage[index] = new_pair
    new_pair.next = old_head

    if new_pair.next is None: 
      hash_table.count += 1
  else:
    current_pair.value = value


def hash_table_remove(hash_table, key):
  index = hash(key, hash_table.capacity)
  current_pair = hash_table.storage[index]
  prev_pair = None

  if current_pair is not None:
    while current_pair is not None and current_pair.key != key:
      prev_pair = current_pair
      current_pair = current_pair.next
  
    if prev_pair is None and current_pair.key == key:
      hash_table.storage[index] = None
      hash_table.count -= 1
    elif current_pair is None:
      print(f"Error 1: {key} not found.")
    else:
      prev_pair.next = None
  else:
    print(f"Error 2: {key} not found.")


def hash_table_retrieve(hash_table, key):
  index = hash(key, hash_table.capacity)
  print(f"Retrieve Print Statement {key} {index}")
  
  current_pair = hash_table.storage[index]

  if current_pair is not None:
    while current_pair is not None and current_pair.key != key:
      current_pair = current_pair.next
  
    if current_pair is None:
      print(f"Error: {key} not found.")
    else:
      return current_pair.value
  else:
    print(f"Error: {key} not found.")


def hash_table_resize(hash_table):
  new_hash_table = HashTable(hash_table.capacity * 2)

  for x in range(hash_table.count):
    current_pair = hash_table.storage[x]

    while current_pair is not None:
      hash_table_insert(new_hash_table, current_pair.key, current_pair.value)
      current_pair = current_pair.next
  
  return new_hash_table

def check_hash_table(hash_table):
  arr = []

  for x in range(hash_table.count):
    arr.append([])
    current_pair = hash_table.storage[x]

    while current_pair is not None:
      if current_pair.next is None:
        arr[x].append((current_pair.key, current_pair.value, None))
      else:
        arr[x].append((current_pair.key, current_pair.value, current_pair.next.key))
      current_pair = current_pair.next
  
  print('new hash table', arr)
  

def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
