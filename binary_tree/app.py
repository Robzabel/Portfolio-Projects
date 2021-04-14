from node import Node
from binary_tree import BinaryTree

tree = BinaryTree(Node(6))
nodes = [5,3,9,7,8,7.5,12,11]

for n in nodes:
    tree.add(Node(n))


tree.inorder()
tree.delete(9)
tree.inorder()

