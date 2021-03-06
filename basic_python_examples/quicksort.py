#!/usr/bin/env python

# Example implementation of quicksort
# This is laughably slower than the built in sort algorithm for the list data type and far uglier
# Purely intended as an exercise to ensure my brain didn't fully atrophy decades after university ;-)

'''
Python 2.7.3 (default, Apr 20 2012, 22:44:07) 
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> execfile('quicksort.py')
>>> quicksort
<function quicksort at 0xb72901b4>
>>> quicksort([random.randint(1,10) for i in range(10)])
[2, 3, 4, 6, 6, 6, 8, 9, 9, 10]
>>> quicksort([random.randint(1,10) for i in range(10)])
[4, 4, 4, 5, 6, 7, 7, 7, 9, 10]
>>> quicksort([random.randint(1,10) for i in range(10)])
[1, 2, 2, 4, 5, 6, 6, 7, 9, 9]
>>> 
'''

import random

def quicksort(l):
    '''quicksort(l) - sort a list l using the infamous quicksort algorithm'''
    # if the list is of length less than 2 you're done, so return the list
    if len(l) < 2:
        return l
    # if the list is of length 2, determine the proper order of the elements and return the list
    if len(l) == 2:
        if l[0] > l[1]:
            return [l[1],l[0]]
        else:
            return l
    # if the list is of length 3 or more, pick the pivot and recurse
    pivot = len(l) / 2
    # everything less than the pivot value goes left
    pivot_val = l[pivot]
    left = list()
    right = list()
    tmp = l[0:pivot]
    tmp.extend(l[pivot+1:])
    for i in tmp:
        if i < pivot_val:
            left.append(i)
        else:
            right.append(i)
    l=quicksort(left)
    l.append(pivot_val)
    l.extend(quicksort(right))
    return l

'''
While looking at my poorly written implementation I came across the interesting
idea of utilizing list comprehensions.  I had incorrectly assumed it would be
even slower, however it turns out that taking advantage of list comprehensions
allows us a signifigant performance gain.  It also looks much, much cleaner!

>>> qsort([random.randint(1,10) for i in range(10)])
[1, 2, 6, 6, 6, 7, 7, 8, 8, 10]
'''

def qsort(l):
    if l == []:
        return []
    else:
        pivot = l[0] # Another interesting approach, simply using the head of
                     # the list as the pivot instead of partitioning
        left  = qsort([i for i in l[1:] if i < pivot])
        right = qsort([i for i in l[1:] if i >= pivot])
        return left + [pivot] + right
