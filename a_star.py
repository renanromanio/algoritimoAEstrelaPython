import dists
from queue import PriorityQueue

class Neighbor:
    def __init__(self, indexPosition, neighborDistance):
        self.indexPosition = indexPosition
        self.NeighborDistance = neighborDistance
        
    def IndexPosition(self):
        return self.IndexPosition
    def NeighborDistance(self):
        return self.NeighborDistance()

class Node:
    def __init__(self, name, distanceFromBucharest):
        self.Neighbors = []
        self.Name = name
        self.DistanceFromBucharest = distanceFromBucharest
    
    def Name(self):
        return self.Name
    
    def DistanceFromBucharest(self):
        return self.distanceFromBucharest
    
    def Neighbors(self):
        return self.neighbors
    

# goal sempre sera 'bucharest'
def a_star(start, goal='Bucharest'):

    cities = dists.dists
    nodesList = []
    for city in cities.keys():
        cityObject = Node(city, dists.straight_line_dists_from_bucharest[city])
        nodesList.append(cityObject)
    
    for node in nodesList:
        for neighbor in cities[node.Name]:
            neighborIndex = next((i for i, n in enumerate(nodesList) if n.Name == neighbor[0]), None)
            neighborDistance = neighbor[1]
            neighborObj = Neighbor(neighborIndex, neighborDistance)
            node.Neighbors.append(neighborObj)
    inicialNode = next(n for n in nodesList if n.Name == start)
    actualNode = inicialNode
    border = PriorityQueue()
    border.put((inicialNode.DistanceFromBucharest, inicialNode.Name))
    exploredList = []
    custoPercorrido = {}
    custoPercorrido[inicialNode.Name] = 0
    totalCoast = custoPercorrido[inicialNode.Name]
    nextNode = ""
    while not border.empty() and nextNode != "Bucharest":
        _, nextNode = border.get()
        actualNode = next(filter(lambda x: x.Name == nextNode, nodesList), "")
        if (actualNode != ""):
            totalCoast = custoPercorrido[actualNode.Name]
            print("Cidade atual: " + actualNode.Name + "\n")
            print("g(n) = " + str(totalCoast) + "\n")
            print("h(n) = " + str(actualNode.DistanceFromBucharest) + "\n")
            exploredList.append(actualNode)
            for neighbor in actualNode.Neighbors:
                possibleNode = nodesList[neighbor.indexPosition]
                if not any(x == possibleNode for x in exploredList):
                    border.put((totalCoast + neighbor.NeighborDistance + possibleNode.DistanceFromBucharest, possibleNode.Name))
                    custoPercorrido[possibleNode.Name] = totalCoast + neighbor.NeighborDistance
    print("Fim")

a_star("Arad")
                
        
    
    
    
        
