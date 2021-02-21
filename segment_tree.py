intervals = [[1,2],[3,7],[4,5],[6,7],[2,3]]
intervals.sort(key=lambda x: x[1])
mid=intervals[int(len(intervals)//2)]
#intervals= [1,3,5,6,10,12]
intervals=[1,3,5,7,9,11]
print(intervals)
#print(sum(intervals))


class Node:
    """
    Node on x axis
    """
    def __init__(self, intervalz, index):
        self.sum = sum(intervalz)
        self.range = [intervalz[0], intervalz[len(intervalz)-1]]
        self.index = index
        self.low = index[0]
        self.high = index[1]
        self.left = None
        self.right = None


def build(intervals, index=[0, len(intervals)-1]):

    if not intervals:
        return None
    mid = len(intervals) // 2
    root = Node(intervals, index)
    #root.sum=sum(intervals)
    if mid == 0:
        root = Node(intervals, [root.high, root.high])
        return root
    if mid == 1:
        #possibly the most stupid solution
        root.left = Node(intervals[:mid+1], [root.low, root.high-1])
        #root.left.sum=sum(intervals[:mid+1])

        root.left.left = Node([intervals[0]], [root.left.low, root.left.low])
        root.left.right = Node([intervals[1]], [root.left.high, root.left.high])

        root.right = build(intervals[mid+1:], [mid, root.high])
    else:
        root.left = build(intervals[:mid], [root.low, len(intervals[:mid])-1])
        root.right = build(intervals[mid:], [mid, root.high])
    return root

def stabbingQuery()

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
        print(' ' * 4 * level + f'-> {root.range} x[{root.low}-{root.high}]')
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
#sum=sumQuery(root,[0,6])
print(sum)
#printInOrder(root)
x=1