class Interval:
    def __init__(self, low, high):
        self.low = low
        self.high = high


class Node:
    def __init__(self, interval):
        self.interval = interval
        self.max = interval.high
        self.left = None
        self.right = None

# print(x.right.low)


class IntervalTree:

    def __init__(self, intervals=None):
        self.root = None
        if intervals is None:
            self.root = None
        else:
            for interval in intervals:
                """
                Can create an tree like this:
                test = IntervalTree([[2,2],[3,6],[1,4],[0,2]])
                """
                self.root = self.insert(self.root, interval)

    overlaps = []
    def search_overlapping_interval(self, root, i):
        interval = Interval(i[0], i[1])

        if root is None:
            return self.overlaps
        if root.interval.low <= interval.high and root.interval.high >= interval.low:
            self.overlaps.append(root.interval)

        if root.left is None and root.right is None:
            return self.overlaps
        else:
            if root.left is None:
                    root = self.search_overlapping_interval(root.right, i)
            elif interval.low > root.left.max:
                    root = self.search_overlapping_interval(root.right, i)
            else:
                root = self.search_overlapping_interval(root.left, i)

        return root

    def insert(self, root, i):
        """
        usage:
        test_tree = intervalTree()
        test_tree.root = test_tree.insert(test_tree.root, [4,7])
        :param root: root of the tree
        :param i: interval to be inserted a list of 2 integers, [low,high] ex. [1,5]
        :return: updated tree
        """
        interval = Interval(i[0], i[1])
        # if interval in self:  # ??
        #    return
        if root is None:

            return Node(interval)
        else:
            if root.interval.low > interval.low:
                root.left = self.insert(root.left, i)
                #self.root.left = Node(interval)  # care
            else:
                root.right = self.insert(root.right, i)
            if root.max < interval.high:
                root.max = interval.high
            return root



#test = IntervalTree()
test = IntervalTree([[2,2],[3,6],[1,4],[0,2]])
test.root = test.insert(test.root, [4,7])
#root = None
#root = test.insert(root, [2, 2])
#root = test.insert(root, [3,6])
#root = test.insert(root, [1,4])
#print(test.root.interval.low)
#root = test.insert(root, [0,2])


def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print(root.interval.low, root.interval.high)
    printInorder(root.right)


def printTree(root, level=0):
    """
    Prints a visualization of the tree
    :param root: root of tree
    :param level: starting level
    """
    if root is not None:
        printTree(root.left, level + 1)
        print(' ' * 4 * level + f'-> [{root.interval.low} {root.interval.high}] ({root.max})')
        printTree(root.right, level + 1)

print("printing!: ")
printInorder(test.root)
printTree(test.root)
result = test.search_overlapping_interval(test.root,[1,8])
print(result, )
