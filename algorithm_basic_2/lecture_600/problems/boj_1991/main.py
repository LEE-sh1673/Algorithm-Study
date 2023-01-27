"""
1991. 트리 순회
"""
from sys import stdin

tree = dict()


class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right


def preorder(x):
    if not x:
        return

    print(x, end='')
    preorder(tree[x].left)
    preorder(tree[x].right)


def inorder(x):
    if not x:
        return

    inorder(tree[x].left)
    print(x, end='')
    inorder(tree[x].right)


def postorder(x):
    if not x:
        return

    postorder(tree[x].left)
    postorder(tree[x].right)
    print(x, end='')


for nodes in stdin.readlines()[1:]:
    node, left, right = nodes.rstrip().split()
    left = '' if left == '.' else left
    right = '' if right == '.' else right
    tree[node] = Node(left, right)

preorder('A')
print()
inorder('A')
print()
postorder('A')
