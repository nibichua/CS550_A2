'''
Created on Feb 10, 2018

@author: mroch
    Name: Tony La and Shawn Nehemiah Chua
    RedID: 817862169, 817662151
    Class Information: CS550: Artificial Intelligence, Spring 2018
    Professor: Professor Marie Roch
    Assignment 2: N-Puzzle with Solving (Depth-First,Breadth-First, and A*)
    Due Date: 2/27/2018
    Filename: problemsearch.py

'''

from basicsearch_lib02.searchrep import (Node, print_nodes)
from basicsearch_lib02.queues import PriorityQueue 
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)
from explored import Explored
import time
from platform import node
        
def graph_search(problem, verbose=False, debug=False):
    """graph_search(problem, verbose, debug) - Given a problem representation
    (instance of basicsearch_lib02.representation.Problem or derived class),
    attempt to solve the problem.
    
    If debug is True, debugging information will be displayed.
    
    if verbose is True, the following information will be displayed:
        
        Number of moves to solution
        List of moves and resulting puzzle states
        Example:
        
            Solution in 25 moves        
            Initial state
                  0        1        2    
            0     4        8        7    
            1     5        .        2    
            2     3        6        1    
            Move 1 -  [0, -1]
                  0        1        2    
            0     4        8        7    
            1     .        5        2    
            2     3        6        1    
            Move 2 -  [1, 0]
                  0        1        2    
            0     4        8        7    
            1     3        5        2    
            2     .        6        1    
            
            ... more moves ...
            
                  0        1        2    
            0     1        3        5    
            1     4        2        .    
            2     6        7        8    
            Move 22 -  [-1, 0]
                  0        1        2    
            0     1        3        .    
            1     4        2        5    
            2     6        7        8    
            Move 23 -  [0, -1]
                  0        1        2    
            0     1        .        3    
            1     4        2        5    
            2     6        7        8    
            Move 24 -  [1, 0]
                  0        1        2    
            0     1        2        3    
            1     4        .        5    
            2     6        7        8    
        
        If no solution were found (not possible with the puzzles we
        are using), we would display:
        
            No solution found
    
    Returns a tuple (path, nodes_explored) where:
    path - list of actions to solve the problem or None if no solution was found
    nodes_explored - Number of nodes explored (dequeued from frontier)
    """
    
    #generate initial state, no parent/actions
    #based off of graph search example on slides
    node = Node(problem, problem.initial)
    if(problem.g==DepthFirst.g and problem.h == DepthFirst.h):
        frontierset = PriorityQueue(node.get_f())
    else:
        frontierset = PriorityQueue()
    frontierset.append(node)
    done = False
    exploredset = Explored()
    expanded = 0 #number of expansions
    while not done:
        node = frontierset.pop()
        #print(node.__repr__())
        exploredset.add(node.state)
        if problem.goal_test(node.state):
            done = True
        else:
            for nextaction in node.expand(problem):
                expanded+=1
                if not exploredset.exists(nextaction.state):
                    frontierset.append(nextaction)
                done = frontierset.__len__() == 0
    if verbose:
        if(len(node.solution()) == 0): #No solutions found
            print("No solution found")
        else:
            print("Solution in ", len(node.solution()), " moves")
            print("Initial State")
            print(problem.initial)
            tempboard = problem.initial
            for i in range(0, len(node.solution())):
                print("Move ",i+1," - ",node.solution()[i])
                tempboard = tempboard.move(node.solution()[i])
                print(tempboard.__repr__())
    return (node.solution(),expanded)
