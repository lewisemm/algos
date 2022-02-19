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

    def get(self, key):
        """
        Creates a hash from `key` and `self.prime` and uses this hash to locate
        value within `self.array`.
        """
        hashed = key % self.prime
        element = self.array[hashed]
        for k, v in element:
            if k == key:
                return v
        raise KeyError(f"'{key}'")

    def delete(self, key):
        """
        Creates a hash using `key` and `self.prime` and uses this hash to locate
        the (key, value) entry in `self.array` for removal.
        """
        used_space = self.capacity - self.free_space
        if used_space <= self.capacity / 4 and self.capacity > self.DEFAULT_SIZE:
            self.__shrink_hashtable(used_space)
        hashed = key % self.prime
        element = self.array[hashed]
        if element == None:
            raise KeyError(f"'{key}'")
        to_be_popped = None
        found = False

        for index, pair in enumerate(element):
            k, v = pair
            if k == key:
                to_be_popped = index
                found = True
                break
        if found:
            self.array[hashed].pop(to_be_popped)
            self.free_space += 1
            return
        raise KeyError(f"'{key}'")

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

    def __shrink_hashtable(self, used):
        """
        Shrinks the size of `self.array` by half when 3/4 of `self.capacity` is
        unused.
        """
        self.capacity //= 2
        self.prime = generate_prime(self.capacity)
        self.free_space = self.capacity - used
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
