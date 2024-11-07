class Node:
    # initializing attributes
    def __init__(self, data):
        self._data = data
        self._next = None
        self._previous = None

    # setting and geting values for previous, current, and next node
    def setNodeValue(self, value):
        self._data = value

    def getNodeValue(self):
        return self._data
    
    def setNextNode(self, value):
        self._next = value

    def getNextNode(self):
        return self._next
    
    def setPreviousNode(self, value):
        self._previous = value

    def getPreviousNode(self):
        return self._previous
    
def main():
    # creating instances
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(40)

    # creating bidirectional linked list
    node1._next = node2._data
    node2._previous = node1._data
    node2._next = node3._data
    node3._previous = node2._data
    node3._next = node4._data
    node4._previous = node3._data

    # demonstrating example of setting/getting value methods working
    print(node2.getNodeValue())
    node2.setNodeValue(15)
    print(node2.getNodeValue())
    print()

    # demonstarting example of node management methods working
    print(node2.getPreviousNode())
    print(node2.setPreviousNode(45))
    node1._data = node2._previous
    print(node1._data)

main()