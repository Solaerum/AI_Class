# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
        state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    print(w)
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))
   
    "*** YOUR CODE HERE ***"
    #Bring in legal directions 
    from util import Stack
    start = problem.getStartState() 

    visitedNodes = {start}
    if problem.isGoalState(start) == True:
        return []
    else:
        s = Stack()
        
        s.push([start, list()]) # push on the start state and empty list

    
        while s.isEmpty != True:
            curr = s.pop() #take off stack
            currCoordinates = curr[0] #coordinates at node
            pathTillNow = curr[1] #traversal until this point
            if problem.isGoalState(currCoordinates):
                return pathTillNow #check if curr is right
                
            else:
                
                currList = problem.getSuccessors(currCoordinates)
                for (coord, action, price) in currList:

                    newPath = pathTillNow + [action]
                    # used for this syntax https://www.geeksforgeeks.org/python-append-string-to-list/ CDT Robert Obrien F4 '25 Assistance to the athor, he showed me in class (after showing you) that I had added to the front instead of back. 

                    if (coord in visitedNodes) == False:
                        visitedNodes.add(coord)
                        s.push([ coord, newPath ]) #pushes on new coordinate + path till now and list of how we got there

            



#Exact same as depth except uses a queue instead of a stack (changed convention naming too)
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
       #Bring in legal directions 
    from util import Queue
    start = problem.getStartState() 
    
    visitedNodes = {start}
    if problem.isGoalState(start) == True:
        return []
    else:
        q = Queue()
        
        q.push([start, list()]) # push on the start state and empty list

    
        while q.isEmpty != True:
            curr = q.pop() #take off stack
            currCoordinates = curr[0] #coordinates at node
            pathTillNow = curr[1] #traversal until this point
            if problem.isGoalState(currCoordinates):
                return pathTillNow #check if curr is right
                
            else:
                
                currList = problem.getSuccessors(currCoordinates)
                for (coord, action, price) in currList:

                    newPath = pathTillNow + [action]
                    # used for this syntax https://www.geeksforgeeks.org/python-append-string-to-list/ CDT Robert Obrien F4 '25 Assistance to the athor, he showed me in class (after showing you) that I had added to the front instead of back. 

                    if (coord in visitedNodes) == False:
                        visitedNodes.add(coord)
                        q.push([ coord, newPath ]) #pushes on new coordinate + path till now and list of how we got there

def uniformCostSearch(problem):
    """Search the node of least total cost first.
    Pseudocode 
    function UNIFORM-COST-SEARCH(problem) returns a solution, or failure
 if problem's initial state is a goal then return empty path to initial state
 frontier ← a priority queue ordered by pathCost, with a node for the initial state
 reached ← a table of {state: the best path that reached state}; initially empty
 solution ← failure
 while frontier is not empty and top(frontier) is cheaper than solution do
   parent ← pop(frontier)
   for child in successors(parent) dos ← child.state
     if s is not in reached or child is a cheaper path than reached[s] then
       reached[s] ← child
       add child to the frontier
       if child is a goal and is cheaper than solution then
         solution = child
 return solution
"""

    "*** YOUR CODE HERE ***"
    from util import PriorityQueue

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

four corners --> make list of falses for each of four corners
[false,false,false,false] use self.corner, when full list is true u have hit all corners