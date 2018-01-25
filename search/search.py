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
from util import *

DEBUG = False


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


class SearchNode:

    def __init__(self, state, parentNode = None, action = None, cost = 0):
        self.state = state
        self.parentNode = parentNode
        self.action = action
        self.cost = cost

    def getState(self):
        return self.state

    def getParentNode(self):
        return self.parentNode

    def getAction(self):
        return self.action

    def getCost(self):
        return self.cost


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    stack = Stack()                                 # DFS requires a stack
    initNode = SearchNode(problem.getStartState())  # Get the initial state and save it in a Search Node
    stack.push(initNode)                            # Put the initial node onto the stack
    visited = []                                    # Create a visited list

    while not stack.isEmpty():                      # Until the stack is empty (and we fail to find the goal)
        nextStateNode = stack.pop()                 # Get the next node off of the stack
        nextState = nextStateNode.getState()        # Save its state in a local variable
        if nextState not in visited:                # If the state has not been visited previously
            visited.append(nextState)               # Add it to the visited list
            if problem.isGoalState(nextState):      # If the state is a goal state
                plan = getPlan(nextStateNode)       # Get the plan that takes pacman to the goal state

                if DEBUG is True:                   # Some debug statements
                    print "Plan: ", plan            # Print the plan
                    print "Visited List: ", visited # Print the visited list

                return plan                         # Return the plan (and exit the DFS)

            # If we have reached this part of the DFS, then the current state is not a goal state
            for successor in problem.getSuccessors(nextState):  # For every possible action and potential new state

                if DEBUG is True:                               # Some debug statements
                    print "This is a successor: ", successor    # Print the successor (in a for loop)

                successorNode = SearchNode(successor[0], nextStateNode, successor[1])   # Convert to Search Node
                stack.push(successorNode)                                               # Push onto stack

    return None                                                                         # If we get here, DFS failed

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    queue = Queue()                                 # DFS requires a queue
    initNode = SearchNode(problem.getStartState())  # Get the initial state and save it in a Search Node
    queue.push(initNode)                            # Put the initial node onto the queue
    visited = []                                    # Create a visited list

    while not queue.isEmpty():                      # Until the queue is empty (and we fail to find the goal)
        nextStateNode = queue.pop()                 # Get the next node off of the queue
        nextState = nextStateNode.getState()        # Save its state in a local variable
        if nextState not in visited:                # If the state has not been visited previously
            visited.append(nextState)               # Add it to the visited list
            if problem.isGoalState(nextState):      # If the state is a goal state
                plan = getPlan(nextStateNode)       # Get the plan that takes pacman to the goal state

                if DEBUG is True:                   # Some debug statements
                    print "Plan: ", plan            # Print the plan
                    print "Visited List: ", visited # Print the visited list

                return plan                         # Return the plan (and exit the DFS)

            # If we have reached this part of the DFS, then the current state is not a goal state
            for successor in problem.getSuccessors(nextState):  # For every possible action and potential new state

                if DEBUG is True:                               # Some debug statements
                    print "This is a successor: ", successor    # Print the successor (in a for loop)

                successorNode = SearchNode(successor[0], nextStateNode, successor[1])  # Convert to Search Node
                queue.push(successorNode)                                              # Push onto queue

    return None                                                                         # If we get here, DFS failed

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    p_queue = PriorityQueue()  # DFS requires a p_queue
    initNode = SearchNode(problem.getStartState())  # Get the initial state and save it in a Search Node
    p_queue.push(initNode,0)  # Put the initial node onto the p_queue
    visited = []  # Create a visited list

    while not p_queue.isEmpty():  # Until the p_queue is empty (and we fail to find the goal)
        nextStateNode = p_queue.pop()  # Get the next node off of the p_queue
        nextState = nextStateNode.getState()  # Save its state in a local variable
        if nextState not in visited:  # If the state has not been visited previously
            visited.append(nextState)  # Add it to the visited list
            if problem.isGoalState(nextState):  # If the state is a goal state
                plan = getPlan(nextStateNode)  # Get the plan that takes pacman to the goal state

                if DEBUG is True:  # Some debug statements
                    print "Plan: ", plan  # Print the plan
                    print "Visited List: ", visited  # Print the visited list

                return plan  # Return the plan (and exit the DFS)

            # If we have reached this part of the DFS, then the current state is not a goal state
            for successor in problem.getSuccessors(nextState):  # For every possible action and potential new state

                if DEBUG is True:  # Some debug statements
                    print "This is a successor: ", successor  # Print the successor (in a for loop)

                successorNode = SearchNode(successor[0], nextStateNode, successor[1], successor[2] + nextStateNode.getCost())  # Convert to Search Node
                p_queue.update(successorNode, successorNode.getCost())  # Push onto p_queue

    return None  # If we get here, DFS failed

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    p_queue = PriorityQueue()  # DFS requires a p_queue
    initNode = SearchNode(problem.getStartState())  # Get the initial state and save it in a Search Node
    p_queue.push(initNode, 0)  # Put the initial node onto the p_queue
    visited = []  # Create a visited list

    while not p_queue.isEmpty():  # Until the p_queue is empty (and we fail to find the goal)
        nextStateNode = p_queue.pop()  # Get the next node off of the p_queue
        nextState = nextStateNode.getState()  # Save its state in a local variable
        if nextState not in visited:  # If the state has not been visited previously
            visited.append(nextState)  # Add it to the visited list
            if problem.isGoalState(nextState):  # If the state is a goal state
                plan = getPlan(nextStateNode)  # Get the plan that takes pacman to the goal state

                if DEBUG is True:  # Some debug statements
                    print "Plan: ", plan  # Print the plan
                    print "Visited List: ", visited  # Print the visited list

                return plan  # Return the plan (and exit the DFS)

            # If we have reached this part of the DFS, then the current state is not a goal state
            for successor in problem.getSuccessors(nextState):  # For every possible action and potential new state

                if DEBUG is True:  # Some debug statements
                    print "This is a successor: ", successor  # Print the successor (in a for loop)

                successorNode = SearchNode(successor[0], nextStateNode, successor[1],
                                           successor[2] + nextStateNode.getCost())  # Convert to Search Node

                nodeHeur = heuristic(successorNode.getState(), problem);

                p_queue.update(successorNode, successorNode.getCost() + nodeHeur)  # Push onto p_queue

    return None  # If we get here, A* failed


def getPlan(finalNode):
    plan = []
    currNode = finalNode
    while currNode.getParentNode() is not None:
        plan.append(currNode.getAction())
        currNode = currNode.getParentNode()
    # I learned how to reverse a list from https://stackoverflow.com/questions/4280691/list-reverse-does-not-return-list/
    # for some reason, plan.reverse() always returns None, so I am using slicing instead
    reversedPlan = plan[::-1]
    #print "Reversed Plan: ", reversedPlan
    return reversedPlan

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
