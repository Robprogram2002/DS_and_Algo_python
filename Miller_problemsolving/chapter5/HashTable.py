# Below we use two lists to create a HashTable class that implements the Map abstract data
# type. One list, called slots, will hold the key items and a parallel list, called data, will hold
# the data values. When we look up a key, the corresponding position in the data list will hold
# the associated data value. We will treat the key list as a hash table using the ideas presented
# earlier. Note that the initial size for the hash table has been chosen to be 11. Although this
# is arbitrary, it is important that the size be a prime number so that the collision resolution
# algorithm can be as efficient as possible.

def hash_function(key, size):
    return key % size


def rehash(old_hash, size):
    return (old_hash + 1) % size


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    # hash_function implements the simple remainder method. The collision resolution technique is linear probing with a
    # “plus 1” rehash function. The put function assumes that there will eventually be an empty slot unless the key
    # is already present in the self.slots. It computes the original hash value and if that slot is not empty,
    # iterates the rehash function until an empty slot occurs. If a nonempty slot already contains the key, the
    # old data value is replaced with the new data value.

    def put(self, key, data):
        hash_value = hash_function(key, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data  # replace/update
            else:
                next_slot = rehash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = rehash(next_slot, len(self.slots))

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data  # replace

    # Likewise, the get function begins by computing the initial hash value. If the value is not in the
    # initial slot, rehash is used to locate the next possible position.

    # y checking to make sure that we have not returned to the initial
    # slot. If that happens, we have exhausted all possible slots and the item must not be present.

    def get(self, key):
        start_slot = hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    # We
    # overload the __getitem__ and __setitem__ methods to allow access using “[].” This
    # means that once a HashTable has been created, the familiar index operator will be available.

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
