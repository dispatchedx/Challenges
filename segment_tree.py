intervals = [[0,1],[3,3],[4,5],[6,7],[2,9],[8,11]]
intervals.sort(key=lambda x: x[1])
mid=intervals[int(len(intervals)//2)]
#intervals=[1,3,5,7,9,11]
print(intervals)



class Node:
    """
    Node on x axis
    """
    def __init__(self, intervalz, index):
        self.intervalz = intervalz
        interval_endpoints = [interval[1] for interval in intervalz]
        self.sum = sum(interval_endpoints)
        self.range = [interval_endpoints[0], interval_endpoints[len(intervalz)-1]]
        #self.index = index
        self.index_low = index[0]
        self.index_high = index[1]
        self.left = None
        self.right = None


def build(intervals, index=[0, len(intervals)-1]):

    if not intervals:
        return None
    mid = len(intervals) // 2
    root = Node(intervals, index)
    if mid == 0:
        root = Node(intervals, [root.index_high, root.index_high])
        return root
    if mid == 1:
        # possibly the most stupid solution to rotate inverse leaf nodes
        root.left = Node(intervals[:mid+1], [root.index_low, root.index_high-1])
        #root.left.sum=sum(intervals[:mid+1])

        root.left.left = Node([intervals[0]], [root.left.index_low, root.left.index_low])
        root.left.right = Node([intervals[1]], [root.left.index_high, root.left.index_high])

        root.right = build(intervals[mid+1:], [mid, root.index_high])
    else:
        # build left array
        root.left = build(intervals[:mid], [root.index_low, len(intervals[:mid])-1])

        # build right array
        root.right = build(intervals[mid:], [mid, root.index_high])
    return root


overlaps=[]


def stabbingQuery(root, point):
    if root is None:
        return root
    # node is not a leaf
    if root.left is not None and root.right is not None:

        # if point is contained in left child, do a query in left child
        if root.left.range[1] >= point:
            stabbingQuery(root.left, point)

        # if point is contained in right child, do a query in right child
        if root.right.range[1] >= point:
            stabbingQuery(root.right, point)
    else:
        # if interval.low <= point <=interval.high
        if intervals[root.index_low][0] <= point <= intervals[root.index_low][1]:
            overlaps.append(intervals[root.index_low])
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
    usage: print_tree(my_tree.root)
    :param root: root of tree
    :param level: starting level
    """
    if root is not None:
        print_tree(root.left, level + 1)
        print(' ' * 4 * level + f'-> {root.range} x[{root.index_low}-{root.index_high}]')
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

root=build(intervals)
print_tree(root)
stabbingQuery(root, 8)
for x in overlaps:
    print(x)
#sum=sumQuery(root,[0,6])
print(sum)
#printInOrder(root)
x=1