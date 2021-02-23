"""
PROJECT 5 - AVL Trees
Name:
"""


class TreeNode:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'parent', 'left', 'right', 'height'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 0

    def __eq__(self, other):
        """
        Determine if the two nodes are equal
        :param other: the node being compared to
        :return: true if the nodes are equal, false otherwise
        """
        if type(self) is not type(other):
            return False
        return self.value == other.value

    def __str__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def __repr__(self):
        """String representation of a node by its value"""
        return str(self.value)


class AVLTree:

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        """
        self.root = None
        self.size = 0

    def __eq__(self, other):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.root is None and other.root is None:
            return True

        if self.size != other.size or self.root != other.root:
            return False  # size & root comp

        return self._is_equal(self.root.left, other.root.left) and self._is_equal(self.root.right, other.root.right)

    def _is_equal(self, root1, root2):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Checks if rootts are both not None then calls _compare, otherwise checks their equality.
        :param root1: root node of first tree
        :param root2: root node of second tree
        :return: True if equal, False if not
        """
        return self._compare(root1, root2) if root1 and root2 else root1 == root2

    def _compare(self, t1, t2):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if not
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        return self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)

    def __str__(self):
        """
        Collects a visual representation of AVL tree
        :return: string of AVL tree
        """
        if not self.root:
            return "Empty AVL Tree..."

        root = self.root
        ans = ""
        bfs_queue = []
        track = {}
        bfs_queue.append((root, 0, root.parent))
        h = AVLTree.height(self.root)

        for i in range(h+1):
            track[i] = []

        while bfs_queue:
            node = bfs_queue.pop(0)
            if node[1] > h:
                break
            track[node[1]].append(node)

            if node[0] is None:
                bfs_queue.append((None, node[1] + 1, None))
                bfs_queue.append((None, node[1] + 1, None))
                continue

            if node[0].left:
                bfs_queue.append((node[0].left, node[1] + 1, node[0]))
            else:
                bfs_queue.append((None,  node[1] + 1, None))

            if node[0].right:
                bfs_queue.append((node[0].right, node[1] + 1, node[0]))
            else:
                bfs_queue.append((None,  node[1] + 1, None))

        spaces = pow(2, h) * 12
        ans += "\n"
        ans += "\t\tVisual Level Order Traversal of AVL Tree - Node (Parent Height)".center(spaces)
        ans += "\n\n"
        for i in range(h+1):
            ans += f"Level {i}: "
            for node in track[i]:
                level = pow(2, i)
                space = int(round(spaces / level))
                if node[0] is None:
                    ans += " " * space
                    continue
                ans += "{} ({} {} {} {})".format(node[0], node[2], node[0].height, node[0].left, node[0].right).center(space, " ")
            ans += "\n"
        return ans

    # ------- Implement/Modify the functions below ------- #

    def insert(self, node, value):
        """
        Inserts new node into tree
        :param node: Root node
        :param value: Value to insert in tree
        :return: nothing
        """

        if self.root is None:
            self.root = TreeNode(value)
            self.size += 1

        else:
            if value < node.value:
                if node.left is None:
                    AVLTree.set_child(node, TreeNode(value), True)
                    self.size += 1
                else:
                    AVLTree.insert(self, node.left, value)
                    AVLTree.rebalance(self, node)

            elif value > node.value:
                if node.right is None:
                    AVLTree.set_child(node, TreeNode(value), False)
                    self.size += 1
                else:
                    AVLTree.insert(self, node.right, value)
                    AVLTree.rebalance(self, node)

    def remove(self, node, value):
        """
        Removes a node from the tree
        :param node: root node
        :param value: value to remove
        :return: root of subtree
        """

        if node is None:
            return None

        if node.value > value:
            # Search to the left
            AVLTree.remove(self, node.left, value)
            AVLTree.rebalance(self, node)
        elif node.value < value:
            # Search right
            AVLTree.remove(self, node.right, value)
            AVLTree.rebalance(self, node)

        else:
            # Not found, keep searching recursivly
            parent = node.parent

            #Case 1, internal node with 2 children
            if node.left is not None and node.right is not None:

                #Find successor
                succ = self.max(node.left)

                node.value = succ.value

                AVLTree.remove(self, succ, succ.value)
                AVLTree.rebalance(self, node)

            elif node.parent is None:

                # Case 2, root node (1 or 0 children)
                if node.left is not None:
                    self.root = node.left
                    self.size -= 1
                else:
                    self.root = node.right
                    self.size -= 1

                if self.root:
                    self.root.parent = None

            elif node.left is not None:
                # Case 3, internal with left child only
                AVLTree.replace_child(parent, node, node.left)
                self.size -= 1

            else:

                # Case 4 internal with right child only OR leaf
                AVLTree.replace_child(parent, node, node.right)
                self.size -= 1

        return self.root

    @staticmethod
    def height(node):
        """
        Function to return height
        :param node: node to find height of
        :return: returns height of node
        """
        if node:
            return node.height
        else:
            return -1


    @staticmethod
    def update_height(node):
        """
        Updates height of a given ndoe
        :param node: node to update height
        :return: does not or not
        """

        if node is None:
            return None

        left_height = -1
        if node.left is not None:
            left_height = node.left.height

        right_height = -1
        if node.right is not None:
            right_height = node.right.height

        max = -1
        if left_height < right_height:
            max = right_height
        elif left_height >= right_height:
            max = left_height

        node.height = max + 1

    def depth(self, value):
        """
        Finds depth of a given value in the tree
        :param value: Value to look for in tree
        :return: height of given value found, -1 otherwise
        """

        # Check for empty tree
        #if self.size == 0:
         #   return -1

        node = self.root
        depth = 0

        while node:

            if value < node.value:
                node = node.left
                depth += 1
            elif value > node.value:
                node = node.right
                depth += 1
            elif value == node.value:
                return depth

        return -1



    def search(self, node, value):
        """
        Finds given node with value, or possible parent node if not found
        :param node: root of subtree
        :param value: value to search for
        :return: The node if value found, otherwise possible parent node
        """
        if node is not None:

            if value == node.value:
                return node
            if value < node.value:
                if node.left is None:
                    return node
                else:
                    return AVLTree.search(self, node.left, value)
            elif value > node.value:
                if node.right is None:
                    return node
                else:
                    return AVLTree.search(self, node.right, value)




    def inorder(self, node):
        """
        Function to traverse tree in order
        :param node: Root to traverse from
        :return: Generator Function
        """
        if node is None:
            return

        if node.left:
            yield from self.inorder(node.left)

        yield node

        if node.right:
            yield from self.inorder(node.right)


    def preorder(self, node):
        """
        Function to traverse tree preorder style
        :param node: Node to traverse from
        :return: Function Generator object
        """
        if node is None:
            return

        yield node

        if node.left:
            yield from self.preorder(node.left)

        if node.right:
            yield from self.preorder(node.right)

    def postorder(self, node):
        """
        Function to traverse in Postorder style
        :param node: root node to traverse from
        :return: Funciton generator object
        """

        if node is not None:

            yield from self.postorder(node.left)
            yield from self.postorder(node.right)
            yield node

    def bfs(self):
        """
        Function to travserse BFS style
        :param self: Node to traverse from as root
        :return: None
        """
        queue = [self.root]

        while queue:
            popped = queue.pop(0)
            yield popped

            if popped.left:
                queue.append(popped.left)

            if popped.right:
                queue.append(popped.right)

    def min(self, node):
        """
        Finds smallest element in tree
        :param node: Root node to start at
        :return: Returns smallest node found, or none
        """

        if node is None:
            return None

        if node.left is None:
            print(node.value)
            return node
        else:
            return self.min(node.left)

    def max(self, node):
        """
        Finds max value in tree
        :param node: Root node
        :return: Max value or none
        """

        if node is None:
            return None

        if node.right is None:
            return node
        else:
            return self.max(node.right)

    def get_size(self):
        """
        Returns size of tree
        :return: tree size
        """
        return self.size

    @staticmethod
    def get_balance(node):
        """
        Returns balance factor or node
        BF = Left subtree height - right subtree height, which is 1, 0, or -1
        :param node: node to find BF for
        :return: the BF
        """
        if node is None:
            return 0

        left = -1
        right = -1

        if node.left:
            left = node.left.height

        if node.right:
            right = node.right.height

        return left - right


    @staticmethod
    def set_child(parent, child, is_left):
        """
        Set child node for given parent
        :param parent: Node to set child for
        :param child: child to set
        :param is_left: if needs to be placed to left
        :return:
        """

        if is_left is not True and is_left is not False:
            return None

        if is_left:
            parent.left = child
        else:
            parent.right = child

        if child is not None:
            child.parent = parent

        #a = AVLTree()
        #a.root = parent
        AVLTree.update_height(parent)

    @staticmethod
    def replace_child(parent, current_child, new_child):
        """
        Method to replace child node
        :param parent: parent to swap childen
        :param current_child: old child
        :param new_child: new child
        :return: None
        """

        if parent.left == current_child:
            return AVLTree.set_child(parent, new_child, True)
        elif parent.right == current_child:
            return AVLTree.set_child(parent, new_child, False)

        return None


    def left_rotate(self, node):
        """
        Method to left rotate tree
        :param node: Node to rotate around
        :return: new root of tree
        """
        right_left_child = node.right.left

        if node.parent is not None:
            self.replace_child(node.parent, node, node.right)
        else:
            self.root = node.right
            self.root.parent = None

        self.set_child(node.right, node, True)
        self.set_child(node, right_left_child, False)

        return node.parent

    def right_rotate(self, node):
        """
        Method to right rotate
        :param node: node to rotate around
        :return: new root of tree
        """

        left_right_child = node.left.right

        if node.parent is not None:
            self.replace_child(node.parent, node, node.left)
        else:
            self.root = node.left
            self.root.parent = None

        self.set_child(node.left, node, False)
        self.set_child(node, left_right_child, True)

        return node.parent

    def rebalance(self, node):
        """
        Rebalances tree based on balance factors
        :param node:  Root node to check for rebalance at
        :return: new root node
        """

        self.update_height(node)

        if self.get_balance(node) == -2:

            if self.get_balance(node.right) == 1:
                # Double Rotation case, Right-Left (-2, 1)
                self.right_rotate(node.right)

            self.left_rotate(node)
            AVLTree.update_height(node.parent)
            return node.parent

        elif self.get_balance(node) == 2:

            if self.get_balance(node.left) == -1:
                # Double Rotation
                self.left_rotate(node.left)

            self.right_rotate(node)
            AVLTree.update_height(node.parent)
            return node.parent

        return node


# ------- Application Problem ------- #
def is_avl_tree(node):

    if node is None:
        return True

    left = check_height(node.left)
    right = check_height(node.right)

    if 1 >= abs(left - right) and is_avl_tree(node.left) and is_avl_tree(node.right):
        return True

    return False



def check_height(node):

    if node is None:
        return 0

    return max(check_height(node.left), check_height(node.right)) + 1







