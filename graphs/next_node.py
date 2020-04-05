from math import inf
from operator import itemgetter

def set_current_node(visited, currentDistances: dict):
    # visited is a set that contains the names of the nodes marked as visited. E.g. {'A', 'C'}.
    # currentDistances is a dictionary that contains the current minimum distance of each node. E.g. {'A': 0, 'B': 3, 'C': 5}
    minimum = [x for x in currentDistances.items() if x[1] not in (0, inf) and x[0] not in visited]
    # fix me: return the label of the node that should be set as "current node".
    result = min(minimum, key=itemgetter(1))
    return result[0]

set_current_node({"A"}, {"A":0, "B":5, "C":inf, "D":inf, "E":4, "F":3, "G":5})