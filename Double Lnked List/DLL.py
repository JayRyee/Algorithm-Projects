class DLLError(Exception):
    """
    Class representing an error related to the DLL class implemented below.
    """
    pass

class DLLNode:
    """
    Class representing a node in the doubly linked list implemented below.
    """

    def __init__(self, value, next=None, prev=None):
        """
        Constructor
        @attribute value: the value to give this node
        @attribute next: the next node for this node
        @attribute prev: the previous node for this node
        """
        self.next = next
        self.prev = prev
        self.value = value

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)

class DLL:
    """
    Class representing a doubly linked list.
    """
    def __init__(self):
        """
        Constructor
        @attribute head: the head of the linked list
        @attribute tail: the tail of the linked list
        @attribute size: the size of the linked list
        """
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        """
        iterates through the linked list to generate a string representation
        :return: string representation of the linked list
        """
        res = ""
        node = self.head
        while node:
            res += str(node)
            if node.next:
                res += " "
            node = node.next
        return res

    def __str__(self):
        """
        iterates through the linked list to generate a string representation
        :return: string representation of the linked list
        """
        res = ""
        node = self.head
        while node:
            res += str(node)
            if node.next:
                res += " "
            node = node.next
        return res

    ######### MODIFY BELOW ##########

    def is_empty(self):
        """
        Determines if the linked list is empty or not
        :return: [boolean] true if DLL is empty, false otherwise
        """
        if self.head is None:
            return True
        else:
            return False

    def insert_front(self, value):
        """
        Inserts a value into the front of the list
        :param value: the value to insert
        """
        if self.head is None:
            new_node = DLLNode(value)
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node = DLLNode(value)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.size += 1

    def insert_back(self, value):
        """
        Inserts a value into the back of the list
        :param value: the value to insert
        """
        if self.tail is None:
            new_node = DLLNode(value)
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node = DLLNode(value)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def delete_front(self):
        """
        Deletes the front node of the list
        """
        if self.head is None:
            raise DLLError

        if self.head.next is not None:
            self.head.next.prev = None
            self.head = self.head.next
            self.size -= 1

        elif self.head.next is None:
            self.head = None
            self.tail = None
            self.size -= 1

    def delete_back(self):
        """
        Deletes the back node of the list
        """
        if self.tail is None:
            raise DLLError
        if self.tail.prev is not None:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.size -= 1
        elif self.tail.prev is None:
            self.head = None
            self.tail = None
            self.size -= 1

    def delete_value(self, value):
        """
        Deletes the first instance of the value in the list.
        :param value: The value to remove
        """
        if self.head is None:
            raise DLLError

        node = self.head
        while node is not None:
            if node.value is value:
                break
            node = node.next

        if node is None:
            raise DLLError

        if node is self.head:
            self.delete_front()
            return
        elif node is self.tail:
            self.delete_back()
            return
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
            node.next = None
            node.prev = None
            self.size -= 1
            return



    def delete_all(self, value):
        """
        Deletes all instances of the value in the list
        :param value: the value to remove
        """
        len = self.size
        if self.head is None:
            raise DLLError

        node = self.head
        while node is not None:
            temp = node.next
            if node.value is value:
                self.delete_value(value)
            node = temp

        if len is self.size:
            raise DLLError


    def find_first(self, value):
        """
        Finds the first instance of the value in the list
        :param value: the value to find
        :return: [DLLNode] the first node containing the value
        """

        if self.head is None:
            raise DLLError

        node = self.head
        while node is not None:
            if node.value is value:
                return node
            node = node.next

        if node is None:
            raise DLLError

    def find_last(self, value):
        """
        Finds the last instance of the value in the list
        :param value: the value to find
        :return: [DLLNode] the last node containing the value
        """

        if self.tail is None:
            raise DLLError

        node = self.tail
        while node is not None:
            if node.value is value:
                return node
            node = node.prev

        if node is None:
            raise DLLError

    def find_all(self, value):
        """
        Finds all of the instances of the value in the list
        :param value: the value to find
        :return: [List] a list of the nodes containing the value
        """

        if self.head is None:
            raise DLLError
        new_list = []

        node = self.head
        while node is not None:
            if node.value == value:
                new_list.append(node)
            node = node.next

        if len(new_list) == 0:
            raise DLLError
        return new_list

    def count(self, value):
        """
        Finds the count of times that the value occurs in the list
        :param value: the value to count
        :return: [int] the count of nodes that contain the given value
        """
        if self.size == 0:
            return 0

        count = 0
        node = self.head
        while node is not None:
            if node.value == value:
                count += 1
            node = node.next
        return count

    def sum(self):
        """
        Finds the sum of all nodes in the list
        :param start: the indicator of the contents of the list
        :return: the sum of all items in the list
        """
        if self.size == 0:
            return None

        my_sum = self.head.value

        node = self.head.next
        while node is not None:
            my_sum += node.value
            node = node.next

        #if type(my_sum) is float:
         #   return round(my_sum, 2)
        print(my_sum)
        return my_sum

def reverse(LL):
    """
    Reverses a linked list in place
    :param LL: The linked list to reverse
    """

    if LL.size == 0:
        return
    if LL.size == 1:
        return

    temp = None
    curr = LL.head
    temp_head = LL.head
    while curr is not None:
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp
        curr = curr.prev
    LL.head = temp.prev
    LL.tail = temp_head



