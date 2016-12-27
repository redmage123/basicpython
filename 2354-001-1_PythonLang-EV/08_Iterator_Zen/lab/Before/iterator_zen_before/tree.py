class TreeNode:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        return "[left={0}\tdata={1}\tright={2}]".format(self.left, self.data, self.right)


# TODO: Add custom iteration to Tree
class Tree:
    def __init__(self):
        # initializes the root member
        self.root = None

    def addNode(self, data):
        # creates a new node and returns it
        return TreeNode(data)

    def insert(self, data):
        self.root = self.__internal_insert(data, self.root)

    def __internal_insert(self, data, node):
        # inserts a new data
        if node == None:
            # store data in current (new) node
            return self.addNode(data)
        else:
            # recurse into the tree
            if data <= node.data:
                # branch to the left
                node.left = self.__internal_insert(data, node.left)
            else:
                # branch to the right
                node.right = self.__internal_insert(data, node.right)
            return node

    def __str__(self):
        return self.root.__str__()

    # TODO: Part of __iter_ is already written
    def __iter__(self):
        return self.items_in_order(self.root)

    def items_in_order(self, node = None):
        # TODO: Implement algorithm using
        # * yield keyword
        # * recursion on this method

        # Here is a sketch of the algorithm for ordered traversal
        # 1. return all items recusing into left node if it exists.
        # 2. return this node's data
        # 3. return all items recusing into right node if it exists.

        raise NotImplementedError("Tree.items_in_order not implemented")