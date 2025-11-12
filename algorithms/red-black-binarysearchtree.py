# Red and black search tree have a logn complexity for insertion, remove and insertion
#
#
#

# the nodes inside the tree
class Node:
    def __init__(self, data, color="red"):
        self.data = data
        self.color = color
        self.parent = None
        self.left = None
        self.right = None


# the tree itself with an initial root set to a Node with None data
class RBtree:
    def __init__(self):
        self.nil = Node(data=None, color="black")
        self.root = self.nil

        # method to rotate to the left in the tree any given node
        def left_rotation(self, node_to_rotate):
            node_to_rotate_right_child = node_to_rotate.right  # my child in the right
            node_to_rotate.right = (
                node_to_rotate_right_child.left
            )  # my ex child its left child is now my right child
            if (
                node_to_rotate_right_child != self.nil
            ):  # checking that my ex right child side is not a nil node
                node_to_rotate_right_child.left.parent = node_to_rotate  # if not a nil node changing the parent of my ex child its left child to myself
            node_to_rotate_right_child.parent = (
                node_to_rotate.parent
            )  # changing parent of my ex right child
            if (
                node_to_rotate.parent is None
            ):  # if iam the root change it so my ex child is now the root of the tree
                self.root = node_to_rotate  # now my ex child is the root
            elif (
                node_to_rotate == node_to_rotate.parent.left
            ):  # if am a left or right child of a parent change my parent child to my ex child
                node_to_rotate.parent.left = node_to_rotate_right_child  # if am left child of my parent now its left child will be my ex child
            else:
                node_to_rotate.parent.right = node_to_rotate_right_child  # im a right change my parent right child to my ex child
            node_to_rotate_right_child.left = (
                node_to_rotate  # now my ex child its left is me
            )
            node_to_rotate.parent = (
                node_to_rotate_right_child  # and my new father is my ex child
            )

        # method to rotate to right the node
        def right_rotation(self, node_to_rotate):
            ex_child = node_to_rotate.left
            node_to_rotate.left = ex_child.right
            if ex_child != self.nil:
                ex_child.right.parent = node_to_rotate
            ex_child.parent = node_to_rotate.parent
            if node_to_rotate.parent is None:
                self.root = ex_child
            elif node_to_rotate.parent == node_to_rotate.parent.left:
                node_to_rotate.parent.left = ex_child
            else:
                node_to_rotate.parent.right = ex_child
            node_to_rotate.parent = ex_child
