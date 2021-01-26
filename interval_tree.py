class Interval:
    def __init__(self, low, high):
        self.low = low
        self.high = high


class Node:
    #TODO nest interval trees in each node for higher dimensions
    def __init__(self, interval):
        self.interval = interval
        self.max = interval.high
        self.left = None
        self.right = None
        self.parent = None


class IntervalTree:
    """
    Can create an tree like this:
    test = IntervalTree([[2,2],[3,6],[1,4],[0,2]])
    """
    def __init__(self, intervals=None):
        self.root = None
        if intervals is None:
            self.root = None
        else:
            for interval in intervals:
                self.root = self.insert(self.root, interval)

    overlaps = []
    def test_overlap(self, root, i):
        """
        Tests if given interval overlaps with any from the tree
        :param root: root of the tree
        :param i: interval
        :return: True if an overlap exists, else returns None
        """
        interval = Interval(i[0], i[1])
        if root is None:
            return False
        if root.interval.low <= interval.high and root.interval.high >= interval.low:
            #self.overlaps.append(root.interval)
            return True

        else:
            if root.left is None:
                    root = self.test_overlap(root.right, i)
            elif interval.low > root.left.max:
                    root = self.test_overlap(root.right, i)
            else:
                root = self.test_overlap(root.left, i)

        return root

    def findall_overlapping_interval(self, root, i):
        """
        ~~Work In Progress~~
        Finds all intervals that overlap with the given interval
        :param root: root of the tree
        :param i: interval
        :return: a list of intervals
        """
        #TODO
        interval = Interval(i[0], i[1])
        if root is None:
            return None
        if root.interval.low <= interval.high and root.interval.high >= interval.low:
            self.overlaps.append(root.interval)
            return True

        if root.left is None and root.right is None:
             return self.overlaps
        else:
            if root.left is None:
                root = self.findall_overlapping_interval(root.right, i)
            elif interval.low > root.left.max:
                root = self.findall_overlapping_interval(root.right, i)
            else:
                root = self.findall_overlapping_interval(root.left, i)
        return root

    def insert(self, root, i):
        """
        Usage:
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
                #root.left.parent=root
                #self.root.left = Node(interval)  # care
            else:
                root.right = self.insert(root.right, i)
                #root.right.parent = root
            if root.max < interval.high:
                root.max = interval.high
            return root

    def delete(self, root, i):
        """
        ~~Work In progress~~
        :param root: root of the tree
        :param i: a pair of intervals
        :return: updated tree
        """
        interval = Interval(i[0], i[1])
        if root is None:
            return root
        #TODO change max value of ancestors
        if root.interval.low > interval.low:
            root.left = self.delete(root.left, i)
        elif root.interval.low < interval.low:
            root.right = self.delete(root.right, i)
        elif root.interval.low == interval.low and root.interval.high == interval.high:
            # no children
            if root.left is None and root.right is None:
                return None
            # 1 children
            elif root.left is None:
                child = root.right
                root = None
                return child
            elif root.right is None:
                child = root.left
                root = None
                return child
            # 2 children
            else:
                child = root.right
                while child.left is not None:
                    child = child.left
                root.interval=child.interval
                root.right=self.delete(root.right, [child.interval.low,child.interval.high])
        if root.interval.high < max(root.left.max, root.right.max):
            root.max = max(root.left.max, root.right.max)
        return root

    def update(self, intervals):
        for interval in intervals:
            self.root = self.insert(self.root, interval)


def printInOrder(root):
    if root is None:
        return
    printInOrder(root.left)
    print(root.interval.low, root.interval.high)
    printInOrder(root.right)


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

#test = IntervalTree()
test = IntervalTree([[2,2],[3,6],[1,4],[0,2]])
#test.root = test.insert(test.root, [7,7])
test.update([[4,4],[5,5]])
test.root =test.delete(test.root, [3,6])
#root = None
#root = test.insert(root, [2, 2])
#root = test.insert(root, [3,6])
#root = test.insert(root, [1,4])
#print(test.root.interval.low)
#root = test.insert(root, [0,2])

print("printing!: ")
#printInOrder(test.root)
printTree(test.root)
result = test.test_overlap(test.root, [5,9])
print(result)
