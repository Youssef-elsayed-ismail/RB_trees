Red-Black Tree Implementation in PythonThis repository contains a clean, efficient implementation of a Red-Black Tree in Python. 
A Red-Black Tree is a type of self-balancing binary search tree (BST) that ensures O(log n) time complexity for search, insertion, and deletion operations by maintaining specific balancing properties during updates.
FeaturesSelf-Balancing: Automatically maintains balance through color-flipping and tree rotations.Standard Operations: Full support for insert, delete, and search.
Educational: Designed with readability in mind, making it a great resource for understanding how balancing algorithms work under the hood.
How It WorksRed-Black Trees maintain balance by enforcing these core rules:Every node is either Red or Black.The root node is always Black.
Red nodes cannot have red children (no two reds in a row).Every path from a node to its descendant NULL nodes contains the same number of black nodes
.UsageSimply import the class into your Python project:Pythonfrom red_black_tree import RedBlackTree

# Initialize the tree
rbt = RedBlackTree()

# Insert values
rbt.insert(10)
rbt.insert(20)
rbt.insert(5)

# Search for a value
node = rbt.search(20)
if node:
    print("Found!")
PerformanceOperationAverage CaseWorst CaseSearch$O(\log n)$$O(\log n)$Insert$O(\log n)$$O(\log n)$Delete$O(\log n)$$O(\log n)$