# binary tree have logn complexity for operation like insertion, remove and search
#
#


class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.color = False
        self.left = None
        self.right = None


class BTSRB:
    def __init__(self):
        self.nil = Node(None)
        self.root = self.nil

    # check if a node exists
    def exists(self, data):
        current = self.root
        while current != self.nil or current.data != data:
            if data < current.data:
                current = current.left
            else:
                current = current.right
        return current

    def insert(self, data):
        new_node = Node(data)
        new_node.color = True
        new_node.left = self.nil
        new_node.right = self.nil
        parent = None
        current = self.nil
        while current != self.nil:
            parent = current
            if current.data > new_node.data:
                current = current.left
            elif current.data < new_node.data:
                current = current.right
            else:
                return "Value is iqual to a node in tree"
        new_node.parent = parent
        if parent is None:
            self.root = new_node
            new_node.color = False
        else:
            if new_node.data < parent.data:
                parent.left = new_node
            else:
                parent.right = new_node

        self.insert_fixup(new_node)

    def insert_fixup(self, new_node):
        while new_node != self.root and new_node.parent.color:
            parent = new_node.parent
            grand_parent = parent.parent
            if parent == grand_parent.right:
                uncle = grand_parent.left
                if uncle.color:
                    uncle.color = False
                    parent.color = False
                    grand_parent.color = True
                    new_node = grand_parent
                elif not uncle.color:
                    if new_node == parent.left:
                        new_node = parent
                        self.rotate_right(new_node)
                        parent = new_node.parent
                    parent.color = False
                    grand_parent.color = True
                    self.rotate_left(grand_parent)
            elif parent == grand_parent.left:
                uncle = grand_parent.right
                if uncle.color:
                    uncle.color = False
                    parent.color = False
                    grand_parent.color = True
                    new_node = grand_parent
                elif not uncle.color:
                    if new_node == parent.right:
                        new_node = parent
                        self.rotate_left(new_node)
                        parent = new_node.parent
                    parent.color = False
                    grand_parent.color = True
                    self.rotate_right(grand_parent)
        self.root.color = False

    # rotate right the node
    def rotate_right(self, x):
        if (
            x == self.nil or x.left == self.nil
        ):  # you cant rotate a nil node or nil child
            return

        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x.parent == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # rotate left the node
    def rotate_left(self, x):
        if (
            x == self.nil or x.right == self.nil
        ):  # you cant rotate a nil node or a nil child
            return
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x.parent == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
