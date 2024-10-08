# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util
import math as m

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.
      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        '''
        print("SuccessorGameState Is: ", successorGameState)
        print("newPos is: ", newPos)
        print("NewFood is: ", newFood)
        print("NewGhostStates is: ", newGhostStates)
        print("newScaredTime is: ", newScaredTimes)
        #successorGameState.getScore()
        '''
        newFood = list(newFood)
        return_score = successorGameState.getScore()
        # Check to see if I will be eaten by ghost on next turn and make -infinite if so
        for i in newGhostStates:
            #print(type(i.getPosition()))
            if manhattanDistance(i.getPosition(),newPos) < 2:
                return_score = -m.inf
                break
        # Check to see closest food
        closest_food = (0,0)
        d2ClosestFood = 1
        for w in range(len(newFood)):
          for h in range(len(newFood[0])):
              if (h,w) == True:
                  if manhattanDistance((h,w),newPos) < d2ClosestFood:
                      d2ClosestFood = manhattanDistance((h,w),newPos)
                      closest_food = (h,w)
              else:
                  continue
        
        return_score += (1 / d2ClosestFood)
                  
        return return_score

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """
    import math as m
    

    
    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        #print (gameState.getLegalActions(0))
        #print("LOOOK RIGHT HERE ASDKOJHASLKJDHASLKJDH\n ASDKJHASKDLJHASLDKJHASLKDH\nasdkjhASDKLJhASDLKJHASDLJKH")
        #print(self.maxValue(gameState, 0,0))
        #return self.maxValue(gameState, 0,0)[0]

        def maxValue(gameState, inDepth, agentID): #This is pacman taking a turn
          #CDT Huchun Walker told me that I need to check the win or lose states as well, I was only checking for the depth being reached
          if (inDepth == self.depth) or gameState.isWin() or gameState.isLose(): #Base state for the recursion (stops if the self.depth is arbitrarily met)
            return self.evaluationFunction(gameState)
          
          else:
            
            v = -m.inf
            for action in gameState.getLegalActions(agentID):
              
              v = max(v, minValue( gameState.generateSuccessor(agentID, action), inDepth, agentID + 1 )) #CDT Robert Obrien assisted me by saying that I could use self. to access other functions below
              #print("tmp at this call is",tmp)
              
            return v
        
        
        def minValue(gameState, inDepth, agentID ): #This is a ghost making a turn
          
          if (inDepth == self.depth) or gameState.isWin() or gameState.isLose(): #Base state for the recursion (stops if the self.depth is arbitrarily met)
            return self.evaluationFunction(gameState)
          
          
          else:
            #print(self.evaluationFunction(gameState))
            v = m.inf
            actionDecision = ""
            for action in gameState.getLegalActions(agentID) :
              tmp = 0
              if agentID == ( gameState.getNumAgents() -1 ):
                #agentID = 0 #pacman turn
                v = min(v, maxValue( gameState.generateSuccessor(agentID, action), inDepth + 1, 0  ) ) # Going back to pacman and starting a new depth
              else:
                #agentID += 1 # Move to next ghost
                v = min(v, minValue( gameState.generateSuccessor(agentID, action), inDepth, agentID+1)  ) # Staying at a ghost and moving ALONG the level
              
            return v
      
        retVal = -m.inf

        bestAction = ""

        for action in gameState.getLegalActions(0):
          nextState = gameState.generateSuccessor(0, action)
          minChecker = minValue(nextState, 0, 1)
          if retVal < minChecker:
            bestAction = action
            retVal = minChecker

            
        return bestAction

        

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        # A lot of this is copied directly from the above minimax
        def maxValue(gameState, inDepth, agentID, alpha, beta): #This is pacman taking a turn
          #CDT Huchun Walker told me that I need to check the win or lose states as well, I was only checking for the depth being reached
          if (inDepth +1 == self.depth) or gameState.isWin() or gameState.isLose(): #Base state for the recursion (stops if the self.depth is arbitrarily met)
            return self.evaluationFunction(gameState)
          
          else:
            
            v = -m.inf
            for action in gameState.getLegalActions(agentID):
              
              v = max(v, minValue( gameState.generateSuccessor(agentID, action), inDepth+1, agentID + 1, alpha, beta )) #CDT Robert Obrien assisted me by saying that I could use self. to access other functions below
              if v > beta: return v
              else: alpha = max(alpha, v)
            return v
        
        
        def minValue(gameState, inDepth, agentID, alpha, beta ): #This is a ghost making a turn
          
          if (inDepth == self.depth) or gameState.isWin() or gameState.isLose(): #Base state for the recursion (stops if the self.depth is arbitrarily met)
            return self.evaluationFunction(gameState)
          
          
          else:
            #print(self.evaluationFunction(gameState))
            v = m.inf
            for action in gameState.getLegalActions(agentID) :
              
              if agentID == ( gameState.getNumAgents() -1 ):
                #agentID = 0 #pacman turn
                v = min(v, maxValue( gameState.generateSuccessor(agentID, action), inDepth, 0, alpha, beta  ) ) # Going back to pacman and starting a new depth
                if v < alpha: return v
                else: beta = min(beta,v)

              else:
                #agentID += 1 # Move to next ghost
                v = min(v, minValue( gameState.generateSuccessor(agentID, action), inDepth, agentID+1, alpha, beta)  ) # Staying at a ghost and moving ALONG the level
                if v < alpha: return v
                else: beta = min(beta,v)

            return v
      
        retVal = -m.inf

        bestAction = ""
        alpha = -m.inf 
        beta = m.inf

        for action in gameState.getLegalActions(0):
          nextState = gameState.generateSuccessor(0, action)
          minChecker = minValue(nextState, 0, 1, alpha, beta)
          if retVal < minChecker:
            bestAction = action
            retVal = minChecker
          if beta < minChecker: return bestAction
          
          alpha = max(alpha, retVal)
            
        return bestAction

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        def maxValue(gameState, inDepth, agentID): #This is pacman taking a turn
          #CDT Huchun Walker told me that I need to check the win or lose states as well, I was only checking for the depth being reached
          if (inDepth == self.depth) or gameState.isWin() or gameState.isLose(): #Base state for the recursion (stops if the self.depth is arbitrarily met)
            return self.evaluationFunction(gameState)
          
          else:
            
            v = -m.inf
            for action in gameState.getLegalActions(agentID):
              
              v = max(v, expectValue( gameState.generateSuccessor(agentID, action), inDepth, agentID + 1 )) #CDT Robert Obrien assisted me by saying that I could use self. to access other functions below
              #print("tmp at this call is",tmp)
              
            return v
        
        
        def expectValue(gameState, inDepth, agentID ): #This is a ghost making a turn
          
          if (inDepth == self.depth) or gameState.isWin() or gameState.isLose(): #Base state for the recursion (stops if the self.depth is arbitrarily met)
            return self.evaluationFunction(gameState)
          
          
          else:
            #print(self.evaluationFunction(gameState))
            v = m.inf
            actionDecision = ""
            expectSum = 0
            for action in gameState.getLegalActions(agentID) :
              tmp = 0
              if agentID == ( gameState.getNumAgents() -1 ):
                #agentID = 0 #pacman turn
                v = maxValue( gameState.generateSuccessor(agentID, action), inDepth + 1, 0  ) # Going back to pacman and starting a new depth
              else:
                #agentID += 1 # Move to next ghost
                v = expectValue( gameState.generateSuccessor(agentID, action), inDepth, agentID+1)  # Staying at a ghost and moving ALONG the level
              expectSum += v * (1/len(gameState.getLegalActions(agentID)))

            return expectSum
      
        retVal = -m.inf

        bestAction = ""

        for action in gameState.getLegalActions(0):
          nextState = gameState.generateSuccessor(0, action)
          minChecker = expectValue(nextState, 0, 1)
          if retVal < minChecker:
            bestAction = action
            retVal = minChecker

            
        return bestAction
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"


# Abbreviation
#


    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    newGhostStates = currentGameState.getGhostStates()      
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    "*** YOUR CODE HERE ***"
    '''
    print("SuccessorGameState Is: ", successorGameState)
    print("newPos is: ", newPos)
    print("NewFood is: ", newFood)
    print("NewGhostStates is: ", newGhostStates)
    print("newScaredTime is: ", newScaredTimes)
    #successorGameState.getScore()
    '''
    newFood = list(newFood)
    return_score = currentGameState.getScore()
    # Check to see if I will be eaten by ghost on next turn and make -infinite if so
    for i in newGhostStates:
        #print(type(i.getPosition()))
        if manhattanDistance(i.getPosition(),newPos) < 2:
            return_score = -m.inf
            break
    # Check to see closest food
    closest_food = (0,0)
    d2ClosestFood = 1
    for w in range(len(newFood)):
      for h in range(len(newFood[0])):
          if (h,w) == True:
              if manhattanDistance((h,w),newPos) < d2ClosestFood:
                  d2ClosestFood = manhattanDistance((h,w),newPos)
                  closest_food = (h,w)
          else:
              continue
    
    return_score += (1 / d2ClosestFood) 
              
    return return_score

better = betterEvaluationFunction