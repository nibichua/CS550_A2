'''
Created on Feb 8, 2018

@author: mroch
'''
from multiprocessing.managers import State
class Explored(object):
    "Maintain an explored set.  Assumes that states are hashable"

    def __init__(self):
        "__init__() - Create an empty explored set"
        #creating a dictionary using python's dictionary
        self.statehashtable = dict()
        
    def exists(self, state):
        """exists(state) - Has this state already been explored?
        Returns True or False, state must be hashable
        """
        #generate the hashcode for the current state
        hashedstate = hash(state) 
        
        #instantiate exists, a boolean for the return value,
        #assuming false initially.
        exists = False
        
        try:
            #determine is state already exists in hashtable
            
            #instantiate a list of elements corresponding to the hash
            hashedstatelist = self.statehashtable[hashedstate]
            for states in hashedstatelist:
                if states == state: #if already exists in hashtable
                    exists = True
                    break
        except KeyError:
            exists = False
            #Only false because if the element was not found in the
            #hashtable, the dict() would return a KeyError
        return exists
            
        
    
    def add(self, state):
        """add(state) - add given state to the explored set.  
        state must be hashable and we asssume that it is not already in set
        """
        
        # The hash function is a Python builtin that generates
        # a hash value from its argument.  Use this to create
        # a dictionary key.  Handle collisions by storing 
        # states that hash to the same key in a bucket list.
        # Note that when you access a Python dictionary by a
        # non existant key, it throws a KeyError
        hashedstate = hash(state)
        #insert state into hashtable
        try:
            #derive a list, corresponding to the hash value
            hashedstatelist = self.statehashtable[hashedstate]
            #if this hashcode exists in the hashtable, it is 
            #possible to just append the state
            hashedstatelist.append(state)
        except KeyError:
            self.statehashtable[hashedstate] = [state]
            
        
            
