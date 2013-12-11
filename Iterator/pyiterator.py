# -*- coding: utf-8 -*-

def is_iterable(x):
    try:
        it = iter(x)
        return True
    except TypeError:
        return False

def depth_first_traverse(composite):
    '''depth first traverse generator
       implemented without recursion'''

    iterators = [ iter(composite) ]
    while iterators:
        for item in iterators[-1]:
            # if an element is iterable,
            # iterate it first.
            if is_iterable(item):
                iterators.append(iter(item))
                break
            else:
                yield item
        else:
            iterators.pop()

def breadth_first_traverse(composite):
    '''breadth first traverse generator
       implemented without recursion'''

    iterators = [ iter(composite) ]
    while iterators:
        iterator = iterators.pop(0)
        items = []
        for item in iterator:
            if is_iterable(item):
                # preserve iterators for further iteration
                iterators.append(iter(item))
            else:
                yield item

class DepthFirstSearchIterator(object):
    def __init__(self, composite):
        self.composite = composite
    def __iter__(self):
        self.searchiter = depth_first_traverse(composite)
        return self
    def next(self):
        return self.searchiter.next()
        
class BreadthFirstSearchIterator(object):
    def __init__(self, composite):
        self.composite = composite
    def __iter__(self):
        self.searchiter = breadth_first_traverse(composite)
        return self
    def next(self):
        return self.searchiter.next()


    
if __name__ == '__main__':

    composite = [ 1,2, [3, [4, 5], 6, 7], 8, [ 9, 10 ] ]

    for item in depth_first_traverse(composite):
        print item,
    else:
        print ""

    for item in breadth_first_traverse(composite):
        print item,
    else:
        print ""

    for item in DepthFirstSearchIterator(composite):
        print item,
    else:
        print ""
    for item in BreadthFirstSearchIterator(composite):
        print item,
    else:
        print ""


    # $ python pyiterator.py
    #
    # 1 2 3 4 5 6 7 8 9 10
    # 1 2 8 3 6 7 9 10 4 5
    # 1 2 3 4 5 6 7 8 9 10
    # 1 2 8 3 6 7 9 10 4 5
    #
