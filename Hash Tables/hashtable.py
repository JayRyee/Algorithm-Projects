"""
Implemented by: Yash Vesikar and Brandon Field
"""


class HashNode:
    """
    DO NOT EDIT
    """
    __slots__ = ["key", "value", "deleted"]

    def __init__(self, key, value, deleted=False):
        self.key = key
        self.value = value
        self.deleted = deleted

    def __repr__(self):
        return f"HashNode({self.key}, {self.value})"

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value

    def __iadd__(self, other):
        self.value += other


class HashTable:
    """
    Hash Table Class
    """
    __slots__ = ['capacity', 'size', 'table', 'prime_index']

    primes = (
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
        89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
        181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
        281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
        397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
        503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
        619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
        743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
        863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991,
        997)

    def __init__(self, capacity=8):
        """
        DO NOT EDIT
        Initializes hash table
        :param capacity: capacity of the hash table
        """
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

        i = 0
        while HashTable.primes[i] <= self.capacity:
            i += 1
        self.prime_index = i - 1

    def __eq__(self, other):
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True

    def __repr__(self):
        """
        DO NOT EDIT
        Represents the table as a string
        :return: string representation of the hash table
        """
        represent = ""
        bin_no = 0
        for item in self.table:
            represent += "[" + str(bin_no) + "]: " + str(item) + '\n'
            bin_no += 1
        return represent

    def _hash_1(self, key):
        """
        ---DO NOT EDIT---
        Converts a string x into a bin number for our hash table
        :param key: key to be hashed
        :return: bin number to insert hash item at in our table, None if key is an empty string
        """
        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)
        return hashed_value % self.capacity

    def _hash_2(self, key):
        """
        ---DO NOT EDIT---
        Converts a string x into a hash
        :param x: key to be hashed
        :return: a hashed value
        """
        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)

        prime = HashTable.primes[self.prime_index]

        hashed_value = prime - (hashed_value % prime)
        if hashed_value % 2 == 0:
            hashed_value += 1
        return hashed_value

    def __len__(self):
        """
        don't edit this plz
        Getter for size
        :return: size
        """
        return self.size

    ########## EDIT BELOW ##########

    def __setitem__(self, key, value):

        self._insert(key, value)
        return None

    def __getitem__(self, key):
        item = self._get(key)
        if item is None:
            raise KeyError
        else:
            return item.value


    def __delitem__(self, key):
        item = self._get(key)
        if item is None:
            raise KeyError
        else:
            self._delete(key)

        return None

    def __contains__(self, key):

        if self._get(key) is None:
            return False

        return True

    def hash(self, key, inserting=False):

        # Inserting a new HashNode
        i = 0
        bucketsProbed = 0
        while bucketsProbed < self.capacity:
            bucket = (self._hash_1(key) + i * self._hash_2(key)) % self.capacity

            if self.table[bucket] is None:
                return bucket

            if inserting is True:
                if self.table[bucket].key is None:
                    return bucket

            if self.table[bucket].key == key:
                return bucket

            i = i + 1
            bucket = (self._hash_1(key) + i * self._hash_2(key)) % self.capacity
            bucketsProbed = bucketsProbed + 1

    def _insert(self, key, value):

        # Table index
        index = self.hash(key)
        # Create Node
        node = HashNode(key, value)
        # Insert Node
        self.table[index] = node
        # Increment size
        self.size = self.size + 1

        if (self.size / self.capacity) >= 0.5:
            self._grow()

    def _get(self, key):
        index = self.hash(key)
        if self.table[index] is None:
            return None
        elif self.table[index].key == key:
            return self.table[index]

    def _delete(self, key):
        index = self.hash(key)
        if self.table[index] is None:
            return None
        elif self.table[index].key == key:
            self.table[index].value = None
            self.table[index].deleted = True
            self.table[index].key = None
            self.size = self.size - 1

    def _grow(self):
        old_table = self.table
        old_cap = self.capacity
        prime_index = self.prime_index

        self.capacity = old_cap * 2

        while self.primes[prime_index] < self.capacity:
            prime_index = prime_index + 1

        self.prime_index = prime_index - 1
        self.table = [None] * self.capacity
        self.size = 0
        bucket = 0
        while bucket < old_cap:
            if old_table[bucket] is not None and old_table[bucket].deleted is False:
                node = old_table[bucket]
                self._insert(node.key, node.value)

            bucket = bucket + 1

        return None

    def update(self, pairs=[]):

        for item in pairs:
            self._insert(item[0], item[1])

        return None

    def setdefault(self, key, default=None):

        item = self._get(key)
        if item is None:
            self._insert(key, default)
            return default

        return item.value

    def keys(self):
        for item in self.table:
            if item:
                yield item.key

    def values(self):
        for item in self.table:
            if item:
                yield item.value



    def items(self):
        for item in self.table:
            if item:
                yield item.key, item.value


    def clear(self):

        for i in range(self.capacity):
            if self.table[i] is not None:
                self.table[i] = None
                self.size = self.size - 1

def hurdles(grid):
    pass



