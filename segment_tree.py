import time
import random

class Node:
    """
    Node on x axis
    """
    def __init__(self, intervalz, index):
        self.intervalz = intervalz
        interval_endpoints = [interval[1] for interval in intervalz]
        self.sum = sum(interval_endpoints)
        self.rangelow=min([interval[0] for interval in intervalz] )
        self.range = [self.rangelow, interval_endpoints[len(intervalz)-1]]
        self.index_low = index[0]
        self.index_high = index[1]
        # For 2 dimensions, create a y segment tree for each node in x segment tree
        #self.y_tree= build(intervalz, index)
        self.left = None
        self.right = None

intervals=[]


def build(intervals, index=[]):
    """
    Builds a segment tree from given list of intervals
    :param intervals: a list of intervals
    :param index: is used to remember index on elements in recursion
    :return: the segment tree
    """
    if not intervals:
        return None
    mid = len(intervals) // 2
    if not index:
        index = [0, len(intervals)-1]
    root = Node(intervals, index)
    if mid == 0:
        root = Node(intervals, [root.index_low, root.index_low])
        return root
    else:
        # build left array
        root.left = build(intervals[:mid], [root.index_low, (root.index_low+root.index_high)//2])

        # build right array
        root.right = build(intervals[mid:], [(root.index_low+root.index_high+1)//2, root.index_high])
    return root


overlaps=[]


def stabbingQuery(root, point):
    """
    Finds all segments that overlap with point
    :param root: root of the tree
    :param point: integer x to search overlaps
    :return: list of segments that overlap with point
    """
    if root is None:
        return root
    # node is not a leaf
    if root.left is not None and root.right is not None:

        # if point is contained in left child, do a query in left child
        if root.left.range[1] >= point and root.left.range[0]<=point:
            stabbingQuery(root.left, point)

        # if point is contained in right child, do a query in right child
        if root.right.range[1] >= point and root.right.range[0]<=point:
            stabbingQuery(root.right, point)
    else:
        # if interval.low <= point <=interval.high
        if root.range[0] <= point <= root.range[1]:
            overlaps.append(root.intervalz[0])
    return root


def update(root, old_segment, new_segment):
    """

    :param root: root of the tree
    :param old_segment: [x_low, x_high]
    :param new_segment: [x_low, x_high]
    :return: updated tree
    """
    #TODO update parent ranges
    if root is None:
        return root

    if root.left is not None and root.right is not None:
        if root.left.range[0] > root.range[0]:
            root.range[0] = root.left.range[0]
        if root.right.range[1] > root.range[1]:
            root.range[1] = root.range[1]
        if root.right.range[0] <= old_segment[1]:
            root.right = update(root.right, old_segment, new_segment)
        if root.left.range[0] <= old_segment[1]:
            root.left = update(root.left, old_segment, new_segment)
    else:
        if root.intervalz[0] == old_segment and len(root.intervalz) == 1:
            root.intervalz = new_segment
            root.range = [new_segment[0], new_segment[1]]
    return root


"""
def sumQuery(root, query):
    query_low = query[0]
    query_high = query[1]
    sum=0
    if root.low > query_high or root.high < query_low:
        return 0
    elif root.low <= query_low and root.high >= query_high:
        return root.sum
    else:
        sum = sum+ sumQuery(root.left, query)
        sum = sum+ sumQuery(root.right, query)
    return sum
"""


def print_tree(root, level=0):
    """
    Prints a visualization of the x tree
    usage: print_tree(root)
    :param root: root of tree
    :param level: starting level
    """
    if root is not None:
        print_tree(root.left, level + 1)
        print(' ' * 4 * level + f'-> {root.range} x_index[{root.index_low}-{root.index_high}]')
        print_tree(root.right, level + 1)


def printInOrder(root):
    """
    obsolete in-order print function for 1D tree
    :param root: root of the tree
    """
    if root is None:
        return
    printInOrder(root.left)
    print(root.sum)
    printInOrder(root.right)


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
        x_low = random.randint(0, 1000)
        x_high = random.randint(x_low, 1000)
        intervals.append([x_low, x_high])

    # Sort segments by endpoints
    intervals.sort(key=lambda x: x[1])
    index = [0, len(intervals) - 1]

    start = time.time()
    root = build(intervals, index)
    end = time.time()
    print(f'build time for {test_size}: {end - start}')

    root = build(intervals, index)
    start = time.time()
    update(root, [500, 600], [1, 2])
    end = time.time()
    print(f'update  time for {test_size}: {end - start}')

    start = time.time()
    stabbingQuery(root, search_range)
    end = time.time()
    print(f'search the whole tree for overlaps: {end - start}')
    return root

"""
intervals = [[1,1],[3,3],[4,5],[6,7],[2,9],[8,11],[9,10],[3,12],[5,8],[3,34]]
# Sort segments by endpoints
intervals.sort(key=lambda x: x[1])
print(intervals)
# To keep track of indexes, no need to ever change it
index = [0, len(intervals)-1]

# Build tree
root = build(intervals, index)

# Update tree
root=update(root,[8,11],[2,2])
#print_tree(root)
"""
if __name__=="__main__":


    segments = [[1,1],[3,3],[4,5],[6,7],[2,9],[8,11],[9,10],[3,12],[5,8],[3,34]]

    # Sort segments by endpoints
    segments.sort(key=lambda x: x[1])
    #print(intervals)
    # To keep track of indexes, no need to ever change it
    #index = [0, len(intervals)-1]

    # Build tree
    root = build(segments)

    # Update tree
    root = update(root, [4, 5], [2, 2])

    root = test_function(10000,50)
    #root = test_function(1000000, 50)

    # Perform a stabbing query
    stabbingQuery(root, 4)

    #print_tree(root)
    # Print the results of query
    #for x in overlaps:
    #    print(x)
