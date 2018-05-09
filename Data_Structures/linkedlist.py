class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

    def traverse(self):
        node = self  # start from head node
        while node != None:
            print(node.value)
            node = node.next


node1 = Node(12)
node2 = Node(14)
node3 = Node(14)
node4 = Node(15)

node1.next = node3
node2.next = node1
node3.next = node4
node2.traverse()
