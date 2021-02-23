"""
Project 4 - Circular Queues
Name:
"""
from collections import defaultdict


class CircularQueue:
    """
    Circular Queue Class.
    """

    # DO NOT MODIFY THESE METHODS
    def __init__(self, capacity=4):
        """
        Initialize the queue with an initial capacity
        :param capacity: the initial capacity of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0

    def __eq__(self, other):
        """
        Defines equality for two queues
        :return: true if two queues are equal, false otherwise
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False

        if self.head != other.head or self.tail != other.tail:
            return False

        for i in range(self.capacity):
            if self.data[i] != other.data[i]:
                return False

        return True

    def __str__(self):
        """
        String representation of the queue
        :return: the queue as a string
        """
        if self.is_empty():
            return "Empty queue"

        str_list = [str(self.data[(self.head + i) % self.capacity]) for i in range(self.size)]
        return "Queue: " + ", ".join(str_list)

    # -----------MODIFY BELOW--------------


    def is_empty(self):
        """
        Function to check if queue is empty
        :param self queue to check
        :return Boolean T/F
        """
        return self.head == self.tail

    def __len__(self):
        """
        Function to find length of the queue
        :param self queue to find length of
        :return a number, the length or # of elements in the queue
        """
        return (self.capacity - self.head + self.tail) % self.capacity



    def head_element(self):
        """
        Function to return head element
        :param  self queue to find head
        :return: None or the element
        """

        # Check for empty queue
        if self.is_empty():

            # Return None
            return None
        else:

            # return Head
            return self.data[self.head]

    def tail_element(self):
        """
        Function to find tail element
        :param self queue to find tail
        :return The tail element or None
        """
        # Check for empty queue
        if self.is_empty():

            # Return None
            return None
        else:

            # return Head
            return self.data[self.tail-1]

    def grow(self):
        """
        Function to grow sie of current queue
        :param self queue to grow
        :return does not return
        """

        if self.size == self.capacity:

            # Make copy of data
            old = self.data
            old_cap = self.capacity

            # Double Capacity
            self.capacity *= 2

            # Resize the new queue
            self.data = [None] * self.capacity

            walk = self.head
            for i in range(self.size):
                self.data[i] = old[walk]
                walk = (1 + walk) % old_cap

            self.head = 0
            self.tail = (self.head + self.size) % self.capacity

    def shrink(self):
        """
        Function to shrink queue
        :param self queue to shrink
        :return does not return
        """

        if 0 < self.size <= self.capacity//4 and self.capacity//2 >= 4:

           # self.capacity //= 2

            old = self.data
            old_cap = self.capacity

            self.capacity //= 2

            self.data = [None] * self.capacity
            walk = self.head
            for i in range(self.size):
                self.data[i] = old[walk]
                walk = (1 + walk) % old_cap

            self.head = 0
            self.tail = (self.head + self.size) % self.capacity

    def enqueue(self, val):
        """
        Function to add element to tail of queue
        :param self queue to add to
        :param val value to add
        :return None
        """

        avail = (self.head + self.size) % self.capacity
        self.data[avail] = val
        self.size += 1

        if self.size == self.capacity:
            self.grow()

        self.tail = (self.head + self.size) % self.capacity

        return None

    def dequeue(self):
        """
        Function to remove item from front of queue
        :param self queue to remove from
        :return Element removed, or None if not found or empty
        """

        if self.is_empty():
            return None
        else:
            answer = self.data[self.head]
            self.data[self.head] = None
            self.head = (self.head + 1) % self.capacity
            self.size -= 1

            if 0 < self.size <= self.capacity // 4:
                self.shrink()
           # self.shrink()

            return answer


class QStack:
    """
    Stack class, implemented with underlying Circular Queue
    """
    # DO NOT MODIFY THESE METHODS
    def __init__(self):
        self.cq = CircularQueue()
        self.size = 0

    def __eq__(self, other):
        """
        Defines equality for two QStacks
        :return: true if two stacks are equal, false otherwise
        """
        if self.size != other.size:
            return False

        if self.cq != other.cq:
            return False

        return True

    def __str__(self):
        """
        String representation of the QStack
        :return: the stack as a string
        """
        if self.size == 0:
            return "Empty stack"

        str_list = [str(self.cq.data[(self.cq.head + i) % self.cq.capacity]) for i in range(self.size)]
        return "Stack: " + ", ".join(str_list)

    # -----------MODIFY BELOW--------------
    #
    #   Stacks are Last In -> First Out
    #
    # O(n)* time complexity
    def push(self, val):
        """
        Function to push new item onto top of stack
        :param self stack to add to
        :param val value to add to stack
        :return None
        """

        self.cq.enqueue(val)
        self.size += 1

        count = 1
        while count < self.size:
            temp = self.cq.dequeue()
            self.cq.enqueue(temp)
            count += 1

        return None

    def pop(self):
        """
        Function to Pop element from top of stack
        :param self stack to pop from
        :return element that was popped, or None if stack is empty
        """

        if self.cq.is_empty():
            return None
        else:
            answer = self.cq.dequeue()
            self.size -= 1

            return answer

    def top(self):
        """
        Function to return, but not remove the top element in the stack
        :param self stack to return top element of
        :return top element, or None if stack is empty
        """

        if self.cq.is_empty():
            return None
        else:
            return self.cq.head_element()


def digit_swap(nums, replacements):
    """
    Function to determine longest length of consecutive numbers in a string
    :param nums string to find consecutive numbers from
    :param replacements number of items in nums we can replace at will
    :return The largest substring of a consecutive number that can be created
    """

    if nums is None:
        return 0
    elif len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return 1

    queue = CircularQueue()
    my_dict = dict()
    num_size = len(nums)

    # Digit which appears most frequently in string
    largest = 0
    # number of times the most frequent digit appears
    l_size = 0

    for item in nums:

        if item in my_dict:

            my_dict[item] += 1

            if my_dict[item] > l_size:

                queue.enqueue(item)
                largest = item
                l_size = my_dict[item]
        else:
            my_dict[item] = 1
            #largest = item

    if replacements is None:
        replacements = 0

    queue.enqueue(largest)
    q_size = len(queue)
    final_size = q_size + replacements

    if q_size == num_size:
        return q_size

    elif q_size + replacements <= num_size:
        return final_size

    else:
        return num_size
