class Node:
    # Nodes that are inserted in the tree
    def __init__(self, data):
        self.data = data
        self.color = "Black"
        self.parent = None
        self.right = None
        self.left = None


class Rbtree:
    # root of tree initial settings
    def __init__(self):
        self.nil = Node(None)
        self.root = self.nil

    # search for a Node with the same data
    def search(self, node, data):
        if node.data == data or node == self.nil:
            return node
        elif node.data > data:
            return self.search(node.left, data)
        else:
            return self.search(node.right, data)

    # get min from a given node
    def min(self, node):
        if node == self.nil:
            return node
        elif node.data is not None and node.left == self.nil:
            return node
        else:
            return self.min(node.left)

    # insert a new_node to the tree
    def insert(self, data):
        new_node = Node(data)
        new_node.color = "Red"
        new_node.left = self.nil
        new_node.right = self.nil
        current = self.root
        parent = None

        while current != self.nil:
            parent = current
            if current.data < new_node.data:
                current = current.right

            elif current.data > new_node.data:
                current = current.left

            else:
                return "Data is iqual to a existing Node"

        new_node.parent = parent
        if parent is None:
            self.root = new_node
            self.root.color = "Black"

        elif new_node.data > parent.data:
            parent.right = new_node

        else:
            parent.left = new_node

    # fix the new node inserted
    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.color == "Red":
            parent = new_node.parent
            grandparent = parent.parent
            if parent == grandparent.right:
                uncle = grandparent.left
                if uncle.color == "Red":
                    uncle.color = "Black"
                    parent.color = "Black"
                    grandparent.color = "Red"
                    new_node = grandparent

                elif uncle.color == "Black":
                    if new_node == parent.left:
                        new_node = parent
                        self.right_rotation(new_node)
                        parent = new_node.parent

                    parent.color = "Black"
                    grandparent.color = "Red"
                    self.left_rotation(grandparent)

            elif parent == grandparent.left:
                uncle = grandparent.right
                if uncle.color == "Red":
                    parent.color = "Black"
                    uncle.color = "Black"
                    grandparent.color = "Red"
                    new_node = grandparent

                elif uncle.color == "Black":
                    if new_node == parent.right:
                        new_node = parent
                        self.left_rotation(new_node)
                        parent = new_node.parent

                    parent.color = "Black"
                    grandparent.color = "Red"
                    self.right_rotation(grandparent)

        self.root.color = "Black"

    # rotate left a node
    def left_rotation(self, new_node):
        if new_node == self.nil or new_node.right == self.nil:
            return

        new_node_child = new_node.right
        new_node.right = new_node_child.left

        if new_node_child.left != self.nil:
            new_node_child.left.parent = new_node

        new_node_child = new_node.parent

        if new_node.parent is None:
            self.root = new_node_child

        elif new_node == new_node.parent.left:
            new_node.parent.left = new_node_child

        else:
            new_node.parent.right = new_node_child

        new_node.parent = new_node_child
        new_node_child.left = new_node

    # rotate right a node
    def right_rotation(self, new_node):
        if new_node == self.nil or new_node.left == self.nil:
            return

        new_node_child = new_node.left
        new_node.left = new_node_child.right

        if new_node_child.right != self.nil:
            new_node_child.right.parent = new_node

        new_node_child.parent = new_node.parent

        if new_node.parent is None:
            self.root = new_node_child

        elif new_node == new_node.parent.left:
            new_node.parent.left = new_node_child

        else:
            new_node.parent.right = new_node_child

        new_node.parent = new_node_child
        new_node_child.right = new_node
