
import os

class Node:
    def __init__(self, data, color="RED"):
        self.data = data
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, color="BLACK")
        self.root = self.NIL
        self.size = 0

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def insert(self, key):
        if self.search(key) != self.NIL:
            return False

        new_node = Node(key)
        new_node.left = self.NIL
        new_node.right = self.NIL

        y = None
        x = self.root

        while x != self.NIL:
            y = x
            if new_node.data < x.data:
                x = x.left
            else:
                x = x.right

        new_node.parent = y
        if y == None:
            self.root = new_node
        elif new_node.data < y.data:
            y.left = new_node
        else:
            y.right = new_node

        self.size += 1
        self._fix_insert(new_node)
        return True

    def _fix_insert(self, k):
        while k.parent and k.parent.color == "RED":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == "RED":
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self._left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == "RED":
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self._right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "BLACK"

    def search(self, key):
        curr = self.root
        while curr != self.NIL and key != curr.data:
            if key < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def get_height(self, node):
        if node == self.NIL:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_black_height(self, node):
        height = 0
        curr = node
        while curr != self.NIL:
            if curr.color == "BLACK":
                height += 1
            curr = curr.left  
        return height