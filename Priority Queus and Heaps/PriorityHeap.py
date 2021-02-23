"""
PROJECT 6 - Priority Queues and Heaps
Name:
"""


class Node:
    """
    This class represents a node object with k (key) and v (value)
    Node definition should not be changed in any way
    """

    def __init__(self, k, v):
        """
        Initializes node
        :param k: key to be stored in the node
        :param v: value to be stored in the node
        """
        self.key = k
        self.value = v

    def __lt__(self, other):
        """
        Less than comparator
        :param other: second node to be compared to
        :return: True if the node is less than other, False otherwise
        """
        return self.key < other.key or (self.key == other.key and self.value < other.value)

    def __gt__(self, other):
        """
        Greater than comparator
        :param other: second node to be compared to
        :return: True if the node is greater than other, False otherwise
        """
        return self.key > other.key or (self.key == other.key and self.value > other.value)

    def __eq__(self, other):
        """
        Equality comparator
        :param other: second node to be compared to
        :return: True if the nodes are equal, False otherwise
        """
        return self.key == other.key and self.value == other.value

    def __str__(self):
        """
        Converts node to a string
        :return: string representation of node
        """
        return '({0},{1})'.format(self.key, self.value)

    __repr__ = __str__


class PriorityHeap:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """

    def __init__(self, is_min=True):
        """
        Initializes the priority heap
        """
        self._data = []
        self.min = is_min

    def __str__(self):
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self._data)

    def __len__(self):
        """
        Length override function
        :return: Length of the data inside the heap
        """
        return len(self._data)

    __repr__ = __str__

#   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Modify below this line
    def swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _parent(self, j):
        return (j-1)//2

    def _left(self, j):
        return 2*j + 1

    def _right(self, j):
        return 2*j + 2

    def _has_left(self, index):
        return self._left(index) < len(self._data)

    def _has_right(self, index):
        return self._right(index) < len(self._data)

    def empty(self):
        """
        Checls if heap is empty
        return: boolean true or false
        """
        return len(self) == 0;

    def top(self):
        """
        Gives the top value is heap is not empty
        param: self, heap to check
        return: None, or the top Node
        """

        if self.empty() is True:
            return None
        else:
            return (self._data[0]).value;

    def push(self, key, val):
        """
        Uses key and value params to add new node to tree
        param: self heap to add to
        param: key key for priority
        param: val val to insert
        """
        if key is None:
            return None
        #if val is None:
         #   return None

        self._data.append(Node(key, val))
        self.percolate_up(len(self._data) - 1)

        return None

    def pop(self):

        if self.empty() is True:
            return None
        if len(self._data) < 1:
            item = self._data.pop()
            return item

        if self.min is True:
            self.swap(0, len(self._data) - 1)
            item = self._data.pop()
            self.percolate_down(0)
            return item

        elif self.min is not True:
            self.swap(0, len(self._data) - 1)
            item = self._data.pop()
            self.percolate_down(0)
            return item

    def min_child(self, index):

        # 1. Invalid Index
        if index is None:
            return None
        # 2. Tree is empty
        elif self.empty():
            return None

        left_index = self._left(index)
        right_index = self._right(index)

        # 3. If no left node
        if self._has_left(index) is False:
            return None

        # 4. Left node but no Right Node
        elif self._has_right(index) is False:
            return left_index

        if self._data[left_index] == self._data[right_index]:
            return right_index
        elif self._data[left_index] < self._data[right_index]:
            return left_index
        elif self._data[left_index] > self._data[right_index]:
            return right_index

    def max_child(self, index):
        """
        Returns index or largest child
        param: self the heap to check in
        param: index index of parent node
        return: Index of greater child, or None
        """
        # 1. Invalid Index
        if index is None:
            return None
        # 2. Tree is empty
        elif self.empty():
            return None

        left_index = self._left(index)
        right_index = self._right(index)

        # 3. If no left node
        if self._has_left(index) is False:
            return None

        # 4. Left node but no Right Node
        elif self._has_right(index) is False:
            return left_index

        if self._data[left_index] == self._data[right_index]:
            return right_index
        elif self._data[left_index] > self._data[right_index]:
            return left_index
        elif self._data[left_index] < self._data[right_index]:
            return right_index

    def percolate_up(self, index):

        if self.min is True:

            while index > 0:
                parent_index = (index - 1) // 2
                # if parent is less than or equal to child ....
                parent = self._data[parent_index]
                child = self._data[index]

                if child < parent:
                    # If Child is is less than parent
                    self.swap(index, parent_index)
                    index = parent_index
                else:
                    return

        elif self.min is False:

            while index > 0:
                parent_index = (index - 1) // 2
                # If parent is greater than or equal to child
                parent = self._data[parent_index]
                child = self._data[index]

                if parent < child:
                    self.swap(index, parent_index)
                    index = parent_index
                else:
                    return

    def percolate_down(self, index):

        if self.min is True:
            if self.min_child(index) is not None:
                child_index = self.min_child(index)
                value = self._data[index]
            else:
                return

            while child_index < len(self._data):

                min_val = value
                min_index = -1

                if self._data[child_index] < min_val:
                    min_val = self._data[child_index]
                    min_index = child_index

                if min_val == value:
                    return
                else:
                    self.swap(index, min_index)
                    index = min_index
                    child_index = (2 * index) + 1

        elif self.min is not True:
            if self.max_child(index) is not None:
                child_index = self.max_child(index)
                value = self._data[index]
            else:
                return

            while child_index < len(self._data):
                max_val = value
                max_index = -1

                if self._data[child_index] > max_val:
                    max_val = self._data[child_index]
                    max_index = child_index
                #i = 0
                #while i < 2 and i + child_index < len(self._data):
                 #   if self._data[i + child_index] > max_val:
                  #      max_val = self._data[i + child_index]
                   #     max_index = i + child_index
                    #i += 1

                if max_val == value:
                    return
                else:
                    self.swap(index, max_index)
                    index = max_index
                    child_index = (2 * index) + 1

def heap_sort(array):
    """
    Funciton to perform HeapSort
    param: array array to sort
    return: sorted array
    """

    # Heapify Array
    max_heap = PriorityHeap(False)

    l = len(array)
    length = (l//2) - 1
    for i in range(length, 0, -1):
        max_heap.percolate_down(i)

    #print(max_heap)
    length2 = l - 1
    for j in range(length2, 1, -1):
        max_heap.swap(0, j)
        max_heap.percolate_down(0)

    #max_heap.swap(0,j)
    print(max_heap._data)
    return max_heap._data

def max_heap_perc_down(nodeIndex, heapArray, arraySize):

    child_index = 2 * nodeIndex + 1
    value = heapArray[nodeIndex]

    while child_index < arraySize:
        max_value = value
        max_index = -1
        i = 0
        while i < 2 and i + child_index < arraySize:
            if heapArray[i+child_index] > max_value:
                max_value = heapArray[i + child_index]
                max_index = i + child_index
            i = i + 1

        if max_value == value:
            return
        else:
            heapArray[nodeIndex], heapArray[max_index] = heapArray[max_index], heapArray[nodeIndex]
            nodeIndex = max_index
            child_index = 2 * nodeIndex + 1

def current_medians(values):
    pass



















