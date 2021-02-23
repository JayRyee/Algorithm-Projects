"""
PROJECT 2 - Linked List Recursion
Name:
PID:
"""


class LinkedNode:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = '_value', '_next'

    def __init__(self, value, next=None):
        """
        DO NOT EDIT
        Initialize a node
        :param value: value of the node
        :param next: pointer to the next node in the LinkedList, default is None
        """
        self._value = value  # element at the node
        self._next = next  # reference to next node in the LinkedList

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a node
        :return: string of value
        """
        return str(self._value)

    __str__ = __repr__

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next

    def set_value(self, value):
        self._value = value

    def set_next(self, next):
        self._next = next


# IMPLEMENT THESE FUNCTIONS - DO NOT MODIFY FUNCTION SIGNATURES #


def insert(value, node=None):
    """

    :param value:
    :param node:
    :return:
    1. LL is Empty
    2. LL is populated
    """
    if node is None:
        return LinkedNode(value)
    elif node.get_next() is None:
        node.set_next(insert(value))
    else:
        insert(value, node.get_next())

    return node



def to_string(node):
    """

    :param node:
    :return:
    """
    output_str = ''

    if node is None:
        return ""
    elif node.get_next() is None:
        output_str += str(node.get_value())
        next_node = node.get_next()
        output_str += to_string(next_node)
    else:
        output_str += str(node.get_value()) + ', '
        next_node = node.get_next()
        output_str += to_string(next_node)

    return output_str


def remove(value, node):
    """

    :param value:
    :param node:
    :return:
    """
    #   BASE CASES
    # 1. Remove first node
    # 2. Remove last node
    # 3. Remove middle node
    # 4. Node not found

    # Case 4, not found
    if node is None:
        return node
    #elif node.get_value()
    # Case 1, Remove first node
    elif node.get_value() == value: # Found the node to remove
        return node.get_next()
    elif node.get_next() is None:
        return None
    # Case 3, removing a middle node
    elif node.get_next().get_value() == value:
        to_remove = node.get_next()     # Grab the node to remove (next node)
        node.set_next(to_remove.get_next())     # Set next of current node, to next of next node
    # Case 2, removing the last node
    else:
        remove(value, node.get_next())

    return node

def remove_all(value, node):
    """

    :param value:
    :param node:
    :return:
    """

    # BASE CASES
    #  1. Remove value at head
    #  2. Remove value in middle
    #  3. Remove value at end
    #  4. Value is not found

    if node is None:
        return None
    else:
        # 1 Remove value at head
        if node.get_value() == value and node.get_next() is not None:
            node = remove_all(value, node.get_next())
        # 2 Remove value in middle
        elif node.get_value() == value and node.get_next() is None:
            node = None
        elif node.get_next() is not None and node.get_next().get_value() == value:
            to_remove = node.get_next()
            nxt = remove_all(value, to_remove.get_next())
            node.set_next(nxt)
        # 3 Remove last node
        else:
            remove_all(value, node.get_next())

    return node


def search(value, node):
    """

    :param value:
    :param node:
    :return:
    """
    if node is None:
        return False
    elif node.get_value() is value:
        return True
    else:
        if search(value, node.get_next()):
            return True
        else:
            return False


def length(node):
    """

    :param node:
    :return:
    """
    cnt = 0
    if node is None:
        return 0
    else:
        cnt = 1 + length(node.get_next())

    return cnt



def sum_list(node):
    """

    :param node:
    :return:
    """
    sum_cnt = 0
    if node is None:
        return 0
    else:
        sum_cnt = node.get_value() + sum_list(node.get_next())

    return sum_cnt

def count(value, node):
    """

    :param value:
    :param node:
    :return:
    """
    cnt = 0

    if node is None:
        return 0
    elif node.get_value() == value:
        cnt += 1 + count(value, node.get_next())
    else:
        cnt += count(value, node.get_next())

    return cnt



def reverse(node):
    """

    :param node:
    :return:
    """
    # 1. If None, return None
    # 2. if next is None, found last element/new Head node
    # 3. Recursively call
    # 4. Set next and Null nodes

    # Node is empty
    if node is None:
        return None

    # Found the last node
    elif node.get_next() is None:
        return node

    # swap node pointers
    else:
        next_node = node.get_next()
        node.set_next(None)
        head_node = reverse(next_node)
        next_node.set_next(node)

    return head_node

def list_percentage(node, percentage, counter=0):
    """

    :param node:
    :param percentage:
    :param counter:
    :return:
    """

    # 1. Node is None
    # 2. Percentage is 0
    #
    # A.) Step through list until at end of list, when node.get_next() is None
    #   B.) Each Recursive call



    # return counter from last node as length
    #   for each node after, check if counter/length == percentage
    if node is None and counter == 0:
        return None
    elif node is None:
        return counter

    elif percentage == 0:
        return None
    elif percentage >= .999999:
        return node

    # At end of list
   # elif node.get_next() is None:
    #    return node

    # Recurse through list
    else:
        counter += 1

        # Returns int, the counter
        # or returns Node, the new head of sublist
        result = list_percentage(node.get_next(), percentage, counter)
        #print(result)
        # if found sublist
        if type(result) is int:
            # return 100% of list
            if (1-((counter-1)/result)) >= percentage:
                return node
            else:
                return result
        else:
            return result

    #print('count', counter)
   # print('To string', to_string(node))
    #print('To string new node', to_string(result))



