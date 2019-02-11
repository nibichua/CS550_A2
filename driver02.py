'''
driver for graph search problem
Created on Feb 10, 2018

@author: mroch

    Name: Tony La and Shawn Nehemiah Chua
    RedID: 817862169, 817662151
    Class Information: CS550: Artificial Intelligence, Spring 2018
    Professor: Professor Marie Roch
    Assignment 2: N-Puzzle with Solving (Depth-First,Breadth-First, and A*)
    Due Date: 2/27/2018
    Filename: driver02.py

'''

from statistics import (mean, stdev)  # Only available in Python 3.4 and newer

from npuzzle import NPuzzle
from basicsearch_lib02.tileboard import TileBoard
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)
from problemsearch import graph_search
import collections
import time
import searchstrategies

def tic():
    "Return current time representation"
    return time.time()

def tock(t):
    "Return time elapsed in sec since t where t is the output of tic()"
    return time.time() - t
    
def driver():
    manTime = [] 
    manLength = []
    manNodes = []
    depTime = []
    depLength = []
    depNodes = []
    breadTime = []
    breadLength = []
    breadNodes = []
    
    for i in range(0,31):
        tb = TileBoard(8)
        #starting with manhattan
        manprobs = NPuzzle(8,tb.state_tuple(),g=Manhattan.g,h=Manhattan.h)
        curTime = tic() #current time
        manList = graph_search(manprobs) #CONSIDER OTHER PARAMETERS LATER
        manTime.append(tock(curTime))
        manLength.append(len(manList[0]))
        manNodes.append(manList[1])
        
        #depth_first search
        depprobs = NPuzzle(8,tb.state_tuple(),g=DepthFirst.g,h=DepthFirst.h)
        curTime = tic() #current time
        depList = graph_search(depprobs) #CONSIDER OTHER PARAMETERS LATER
        depTime.append(tock(curTime))
        depLength.append(len(depList[0]))
        depNodes.append(depList[1])
        
        #breadth_first search
        breadprobs = NPuzzle(8,tb.state_tuple(),g=BreadthFirst.g,h=BreadthFirst.h)
        curTime = tic() #current time
        breadList = graph_search(breadprobs) #CONSIDER OTHER PARAMETERS LATER
        breadTime.append(tock(curTime))
        breadLength.append(len(breadList[0]))
        breadNodes.append(breadList[1])
    #calculate mean and stdevs for each list generated at beginning
    
    #manhattan statistics
    meanmantime = mean(manTime)
    stdmantime = stdev(manTime,meanmantime)
    meanmanlength = mean(manLength)
    stdmanlength = stdev(manLength,meanmanlength)
    meanmannodes = mean(manNodes)
    stdmannodes = stdev(manNodes,meanmannodes)

    #depth-first statistics
    meandeptime = mean(depTime)
    stddeptime = stdev(depTime)
    meandeplength = mean(depLength)
    stddeplength = stdev(depLength)
    meandepnodes = mean(depNodes)
    stddepnodes = stdev(depNodes)
    
    #breadth-first statistics
    meanbreadtime = mean(breadTime)
    stdbreadtime = stdev(breadTime)
    meanbreadlength = mean(breadLength)
    stdbreadlength = stdev(breadLength)
    meanbreadnodes = mean(breadNodes)
    stdbreadnodes = stdev(breadNodes)
    
    print("Manhattan Statistics - Mean Time: ", meanmantime, "StDev Time: ", stdmantime)
    print("Manhattan Statistics - Mean Length: ", meanmanlength, "StDev Length: ", stdmanlength)
    print("Manhattan Statistics - Mean Nodes: ", meanmannodes, "StDev Nodes: ", stdmannodes)

    print("Depth-First Statistics - Mean Time: ", meandeptime, "StDev Time: ", stddeptime)
    print("Depth-First Statistics - Mean Length: ", meandeplength, "StDev Length: ", stddeplength)
    print("Depth-First Statistics - Mean Nodes: ", meandepnodes, "StDev Nodes: ", stddepnodes)
    
    print("Breadth-First Statistics - Mean Time: ", meanbreadtime, "StDev Time: ", stdbreadtime)
    print("Breadth-First Statistics - Mean Length: ", meanbreadlength, "StDev Length: ", stdbreadlength)
    print("Breadth-First Statistics - Mean Nodes: ", meanbreadnodes, "StDev Nodes: ", stdbreadnodes)    
    
    
if __name__ == '__main__':
    driver()
