from hashtable.prime import generate_prime

class HashTable:
    def __init__(self):
        self.DEFAULT_SIZE = 8
        self.capacity = self.DEFAULT_SIZE
        self.free_space = self.capacity
        self.array = [None] * self.capacity
        self.prime = generate_prime(self.capacity)

    def insert(self, key, value):
        """
        Creates a hash from `key` and `self.prime` and uses this hash to store
        the (key, value) tuple inside `self.array`.
        """
        if self.free_space == 0:
            self.__grow_hashtable()
        hashed = key % self.prime
        if self.array[hashed] == None:
            self.array[hashed] = [(key, value)]
        else:
            element = self.array[hashed]
            found = False
            to_be_updated = None
            for index, pair in enumerate(element):
                k, v = pair
                if k == key:
                    to_be_updated = index
                    found = True
                    break
            if found:
                self.array[hashed][to_be_updated] = (key, value)
            else:
                self.array[hashed].append((key, value))
        self.free_space -= 1

    def __grow_hashtable(self):
        """
        Doubles the size of `self.array` when `self.capacity` is exceeded.
        """
        self.free_space = self.capacity
        self.capacity *= 2
        self.prime = generate_prime(self.capacity)
        new_array = [None] * self.capacity
        for element in self.array:
            if element:
                for key, value in element:
                    hashed = key % self.prime
                    if new_array[hashed] == None:
                        new_array[hashed] = [(key, value)]
                    else:
                        new_array[hashed].append((key, value))
        self.array = new_array
        del new_array
