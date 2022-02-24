class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

#helper functions to easily insert data
    def insert_left(self, val):
        if self.left is None:
            self.left = Node(val)
        return -1

    def insert_right(self, val):
        if self.right is None:
            self.right = Node(val)
        return -1


def preorder(node):
    yield node.data
    if node.left is not None:
        yield from preorder(node.left)
    if node.right is not None:
        yield from preorder(node.right)


def inorder(node):
    if node.left is not None:
        yield from inorder(node.left)
    yield node.data
    if node.right is not None:
        yield from inorder(node.right)


def postorder(node):
    if node.left is not None:
        yield from postorder(node.left)
    if node.right is not None:
        yield from postorder(node.right)
    yield node.data


def breadth_first(node):
    node_height = height(node)
    for i in range(1, node_height+1):
        yield from yield_curr_level(node, i)


def yield_curr_level(node, level):
    if node is None:
        return
    if level == 1:
        yield node.data
    elif level > 1:
        yield from yield_curr_level(node.left, level-1)
        yield from yield_curr_level(node.right, level-1)


def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
        return lheight+1 if lheight > rheight else rheight+1


#Test Driver-code
N = Node(25)
N.insert_left(15)
N.left.insert_left(10)
N.left.left.insert_left(4)
N.left.left.insert_right(12)
N.left.insert_right(22)
N.left.right.insert_left(18)
N.left.right.insert_right(24)

N.insert_right(50)
N.right.insert_left(35)
N.right.left.insert_left(31)
N.right.left.insert_right(44)
N.right.insert_right(70)
N.right.right.insert_left(66)
N.right.right.insert_right(90)

# Output example
gen = inorder(N)
#gen = breadth_first(N)
for x in gen:
    print(x)
