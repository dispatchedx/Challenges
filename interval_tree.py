import random
import time


class Interval:
    def __init__(self, low, high,):
        self.low = low
        self.high = high


class Node:
    """
    Node on x axis
    """
    def __init__(self, interval, y_interval):
        self.interval = interval
        self.max = interval.high
        self.left = None
        self.right = None
        self.y_tree = IntervalTree()
        self.y_tree.root = self.y_tree.insert(self.y_tree.root, [y_interval.low, y_interval.high])


class YNode:
    """
    Node on y axis
    """
    def __init__(self, interval):
        self.interval = interval
        self.max = interval.high
        self.left = None
        self.right = None


class IntervalTree:
    """
    Can create an tree like this:
    my_tree = IntervalTree([[2,2,3,7],[3,6,5,5],[1,4,1,1],[0,2,1,1]])
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
        obsolete function: only works on 1D tree
        Tests if given interval overlaps with any from the tree
        usage:
        result = my_tree.test_overlap(my_tree.root, [5,10,3,4])
        print(result)
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
        usage: my_tree.findall_overlapping_interval(my_tree.root, [30,500, 1,1000])
        Finds all intervals that overlap with the given interval on x axis
        :param root: root of the tree
        :param i: interval
        :return: a list of intervals
        """
        #TODO maybe make it prettier

        interval = Interval(i[0], i[1],)
        if root is None:
            return root
        if root.interval.low <= interval.high and root.interval.high >= interval.low:
            self.findall_overlapping_y_interval(root.y_tree.root, i, root.interval)  #search for y value
            #self.overlaps.append(root.interval)

        if root.left is None and root.right is None:
            return root
        else:
            if root.left is None:
                self.findall_overlapping_interval(root.right, i)
            elif interval.low > root.left.max:
                self.findall_overlapping_interval(root.right, i)
            else:
                self.findall_overlapping_interval(root.left, i)
                if interval.high > root.interval.low:
                    self.findall_overlapping_interval(root.right, i)
        return root

    def findall_overlapping_y_interval(self, root, i, x_interval):
        """~
        Finds all intervals that overlap with the given interval on y axis
        :param root: root of the tree
        :param i: interval
        :return: a list of intervals
        """
        # TODO maybe make it prettier
        x_interval = x_interval
        interval = Interval(i[2], i[3],)
        if root is None:
            return root
        if root.interval.low <= interval.high and root.interval.high >= interval.low:
            self.overlaps.append([x_interval,root.interval])
            return root
        if root.left is None and root.right is None:
            return root
        else:
            if root.left is None:
                self.findall_overlapping_y_interval(root.right, i,x_interval)
            elif interval.low > root.left.max:
                self.findall_overlapping_y_interval(root.right, i,x_interval)
            else:
                self.findall_overlapping_y_interval(root.left, i,x_interval)
                if interval.high > root.interval.low:
                    self.findall_overlapping_y_interval(root.right, i,x_interval)
        return root

    def insert(self, root, i):
        """
        inserts interval to the tree;
        Usage:
        test_tree = intervalTree()
        test_tree.root = test_tree.insert(test_tree.root, [4, 7, 3, 3])

        :param root: root of the tree
        :param i: interval to be inserted to the tree; a list of 4 integers, [x_low,x_high, y_low, y_high]
        :return: updated tree
        """
        interval = Interval(i[0], i[1])
        # if interval in self:  # ??
        #    return

        if root is None:
            if len(i) > 2:
                y_interval = Interval(i[2], i[3])
                return Node(interval, y_interval)
            else:
                return YNode(interval)
        else:
            if len(i) > 2:
                y_interval = Interval(i[2], i[3])
                root.y_tree.root = root.y_tree.insert(root.y_tree.root, [y_interval.low, y_interval.high])
            if root.interval.low > interval.low:
                #if root.left is not None:
                root.left = self.insert(root.left, i)
            else:
                root.right = self.insert(root.right, i)
            if root.max < interval.high:
                root.max = interval.high
            return root

    def delete(self, root, i):
        """
        deletes interval i from tree and updates ancestors max values
        :param root: root of the tree
        :param i: a pair of intervals xy ex. [x_low, x_high, y_low, y_high]
        :return: updated tree
        """
        interval = Interval(i[0], i[1])
        #y_interval = Interval(i[2],i[3])
        if root is None:
            return root
        if root.interval.low > interval.low:
            root.left = self.delete(root.left, i)
        elif root.interval.low < interval.low:
            root.right = self.delete(root.right, i)
        elif root.interval.low == interval.low and root.interval.high == interval.high:
            if isinstance(root, Node):  #if root is a X node
                og = root.y_tree.root  # remember it
                root.y_tree.root = self.delete(root.y_tree.root, i[2:])  # if y is found, delete it
                if root.y_tree.root == og:  # if y was not found
                    return root  # do nothing
            # if y was found, delete X node and update tree
            # no children
            if root.left is None and root.right is None:
                return None
            # 1 children
            elif root.left is None:
                child = root.right
                #root = None
                return child
            elif root.right is None:
                child = root.left
                #root = None
                return child
            # 2 children
            else:
                child = root.right
                while child.left is not None:
                    child = child.left
                root.interval = child.interval
                if isinstance(child, Node):
                    root.right = self.delete(root.right, [child.interval.low, child.interval.high,
                                                      child.y_tree.root.interval.low, child.y_tree.root.interval.high])
                else:
                    if isinstance(child, Node):
                        root.right = self.delete(root.right, [child.interval.low, child.interval.high,
                                                              child.interval.low,
                                                              child.interval.high])
        if root.left is not None and root.right is not None:
            if root.interval.high < max(root.left.max, root.right.max):
                root.max = max(root.left.max, root.right.max)
        elif root.left is not None:
            if root.interval.high < root.left.max:
                root.max = root.left.max
            else:
                root.max = root.interval.high
        elif root.right is not None:
            if root.interval.high < root.right.max:
                root.max = root.right.max
            else:
                root.max = root.interval.high
        else:
            root.max = root.interval.high
        return root

    def update(self, intervals):
        for interval in intervals:
            self.root = self.insert(self.root, interval)


def printInOrder(root):
    """
    obsolete in-order print function for 1D tree
    :param root: root of the tree
    """
    if root is None:
        return
    printInOrder(root.left)
    print(root.interval.low, root.interval.high)
    printInOrder(root.right)


def print_tree(root, ext_interval=0, level=0):
    """
    Prints a visualization of the x tree
    usage: print_tree(my_tree.root)
    :param root: root of tree
    :param ext_interval is the x interval of the ynode
    :param level: starting level
    """
    if root is not None:
        if isinstance(root, YNode):
            x_interval = ext_interval
            y_interval = root.interval
        else:
            x_interval = root.interval
            y_interval = root.y_tree.root.interval
        print_tree(root.left, x_interval,level + 1)
        print(' ' * 4 * level + f'-> x({x_interval.low} {x_interval.high}) y({y_interval.low}'
                                f' {y_interval.high}) ({root.max})')
        print_tree(root.right, x_interval,level + 1)


def y_print_tree(root):
    """
    Prints a visualization of the y trees
    usage: y_print_tree(my_tree.root)
    :param root: root of tree
    """
    if root is not None:
        y_print_tree(root.left,)
        print_tree(root.y_tree.root,root.interval,)
        y_print_tree(root.right,)


def test_function(test_size, search_range):
    """
    Prints time elapsed for build, update and search range of tree of test_size size
    usage: test_function(10000)
    :param search_range [x_low, x_high, y_low, y_high]
    :param test_size: n size of intervals to be stored
    """
    test_size = test_size
    intervals = []
    for i in range(test_size):
        if i % 2 == 0:
            x_low = random.randint(0,1000)
            x_high = random.randint(x_low,1000)
            y_low = y_high = random.randint(1,1000)
        else:
            y_low = random.randint(0,1000)
            y_high = random.randint(y_low,1000)
            x_low = x_high = random.randint(1, 1000)
        intervals.append([x_low, x_high, y_low, y_high])

    start = time.time()
    my_tree = IntervalTree(intervals)
    end = time.time()
    print(f'build time for {test_size}: {end - start}')

    my_tree = IntervalTree()
    start = time.time()
    my_tree.update(intervals)
    end = time.time()
    print(f'update  time for {test_size}: {end - start}')

    start = time.time()
    my_tree.findall_overlapping_interval(my_tree.root, search_range)
    end = time.time()
    print(f'search the whole tree for overlaps: {end - start}')
    return my_tree


if __name__=="__main__":
    # Initialize tree
    my_tree = IntervalTree()

    my_tree.update([[7,8, 1,1],[3,5, 6,6],[8,12, 1,1],[5,5, 2,5],[4,7, 1,3]])

    my_tree=test_function(10000,[1,1000,1,1000])
    #test_function(100000)
    #my_tree.root=my_tree.insert(my_tree.root, [10,12,3,4])
    my_tree.root=my_tree.insert(my_tree.root, [1,5999,6,6])
    #my_tree.root =my_tree.delete(my_tree.root, [1,5999,6,6])

    #print("printing xtree: ")
    #print_tree(my_tree.root)
    """
    print("printing ytrees:")
    y_print_tree(my_tree.root)
    """

    """
    to print found intervals that overlap
    
    for x_interval, y_interval in my_tree.overlaps:
        print(f'x({x_interval.low} {x_interval.high}) y({y_interval.low} {y_interval.high})')
    print(len(my_tree.overlaps))
    """
