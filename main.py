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
        self._next._data = value

    def getNextNode(self):
        return self._next._data
    
    def setPreviousNode(self, value):
        self._previous._data = value

    def getPreviousNode(self):
        return self._previous._data
    
def main():
    # creating instances
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(40)

    # creating bidirectional linked list
    node1._next = node2
    node2._previous = node1
    node2._next = node3
    node3._previous = node2
    node3._next = node4
    node4._previous = node3

    # printing list before altering data
    current = node1
    while current:
        print(current._data, end=" -> ")
        current = current._next
    print("None")
    print()

    # demonstrating example of setting/getting value methods working
    print(node2.getNodeValue())
    node2.setNodeValue(15)
    print(node2.getNodeValue())
    print()

    # demonstrating example of set/get-previous methods working
    print(node2.getPreviousNode())
    node2.setPreviousNode(45)
    print(node1._data)
    print()

    # demonstrating example of set/get-next methods working
    print(node4._data)
    node3.setNextNode(60)
    print(node3.getNextNode())
    node4.setNodeValue(90)
    print(node3.getNextNode())
    print()

    # printing list after altering data
    current = node1
    while current != None:
        print(current._data, end=" -> ")
        current = current._next
    print("None")

main()