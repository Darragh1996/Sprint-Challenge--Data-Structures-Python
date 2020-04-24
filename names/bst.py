class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        newTree = BinarySearchTree(value)
        currentTree = self
        inserted = False
        while not inserted:
            if value >= currentTree.value:
                if currentTree.right == None:
                    currentTree.right = newTree
                    inserted = True
                else:
                    currentTree = currentTree.right
            else:
                if currentTree.left == None:
                    currentTree.left = newTree
                    inserted = True
                else:
                    currentTree = currentTree.left

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target > self.value and self.right != None:
            return self.right.contains(target)
        elif target <= self.value and self.left != None:
            return self.left.contains(target)
        else:
            return False
