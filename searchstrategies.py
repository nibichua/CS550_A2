"""
searchstrategies

Module to provide implementations of g and h for various search strategies.
In each case, the functions are class methods as we don't need an instance
of the class.  

If you are unfamiliar with Python class methods, Python uses a function
decorator (indicated by an @ to indicate that the next method is a class
method).  Example:

class SomeClass:
    @classmethod
    def foobar(cls, arg1, arg2):
        "foobar(arg1, arg2) - does ..."
        
        code... class variables are accessed as cls.var (if needed)
        return computed value

A caller would import SomeClass and then call, e.g. :  
    SomeClass.foobar("hola","amigos")

Contains g and h functions for:
BreadFirst - breadth first search
DepthFirst - depth first search
Manhattan - city block heuristic search.  To restrict the complexity of
    this, you only need handle heuristics for puzzles of an odd length
    with solutions that contain the blank in the middle and numbers going
    from left to right in each row, e.g.:
        123
        4 5
        678
    When mulitple solutions are allowed, the heuristic becomes a little more
    complex as the city block distance must be estimated to each possible solution
    state. 
    
    Name: Tony La and Shawn Nehemiah Chua
    RedID: 817862169, 817662151
    Class Information: CS550: Artificial Intelligence, Spring 2018
    Professor: Professor Marie Roch
    Assignment 2: N-Puzzle with Solving (Depth-First,Breadth-First, and A*)
    Due Date: 2/27/2018
    Filename: searchstrategies.py

"""

import math
from builtins import classmethod
from basicsearch_lib02.board import *
from basicsearch_lib02.queues import *
from basicsearch_lib02.searchrep import *
from basicsearch_lib02.tileboard import *
from basicsearch_lib02.utilsdontneed import *

# For each of the following classes, create classmethods g and h
# with the following signatures
#       @classmethod
#       def g(cls, parentnode, action, childnode):
#               return appropritate g value
#       @classmethod
#        def h(cls, state):
#               return appropriate h value
 

class BreadthFirst(object):
    "BredthFirst - breadthfirst search"
    @classmethod
    def g(cls, parentnode, action, childnode):
        return childnode.depth
    @classmethod
    def h(cls, state):
        return 0

class DepthFirst(object):
    "DepthFirst - depth first search"
    @classmethod
    def g(cls, parentnode, action, childnode):
        return childnode.depth * -1
    @classmethod
    def h(cls, state):
        return 0
        
class Manhattan(object):
    "Manhattan Block Distance heuristic"
    @classmethod
    def g(cls, parentnode, action, childnode):
        return childnode.depth + 1
    @classmethod
    def h(cls, state):
        r = c = cost = 0
        #Look at each tile, look at the numerical value and
        #determine exactly where that tile should be via 
        #modulo and divisive algebra
        for row in range (state.boardsize):
            for col in range (state.boardsize):
                curTile = state.board[row][col]
                if state.board[row][col] != None:
                    #to get the rows with the special cases
                    if (curTile % state.boardsize == 0 and curTile < (state.boardsize**2)/2):
                        r = (int)((curTile/state.boardsize)-1)
                    else:
                        r = (int)(curTile / state.boardsize)
                    #to get the columns with the special cases
                    if (curTile % state.boardsize == 0 and curTile <= (state.boardsize**2)/2):
                        c = state.boardsize-1
                    elif (curTile % state.boardsize != 0 and curTile <= (state.boardsize**2)/2):
                        c = (curTile % state.boardsize) - 1
                    else:
                        c = curTile % state.boardsize
                else:
                    c = r = (int)(state.boardsize/2)
                
                cost += abs((r -row) + (c - col))
        return cost
                