# Node
class Node():
    def __init__(self, data):
        # data, next -> pointer
        self.data = data
        self.next = None

    def __str__(self):
        return f"Node: {self.data} \n Pointer -> {self.next}"


# test
node_one = Node(7)
print(node_one)

# Linked List


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        return f"Linked List\n Head -> {self.head}\n Tail -> {self.tail}\n Length -> {self.length}"

    # add_to_tail
    def add_to_tail(self, data):
        # create a new node and set data to the node
        new_node = Node(data)

        # check to see if there is not a head in the linked list
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.length += 1
        return self

    # add_to_head
    def add_to_head(self, data):
        # create a new node and set data to the node
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return self

    def remove_head(self):
        if not self.head:
            return None
        current_head = self.head
        self.head = current_head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return current_head


list_one = LinkedList()  # makes a new linkedlist and is set to variable list_one
list_one.add_to_tail('Amir')
list_one.add_to_head(8)
list_one.add_to_head(77)
print(list_one)

# List contains the nodes and the nodes contain the data and the pointer
# All of the different data structures are some form of an OBJECT
# data base
# table (collection) -> Node
# table (collection) -> Linked List
# association
# Node belong to a Linked List
'''
{
    id: ObjectId,
    data: node.data
}
'''
# Linked List will have many nodes
'''
{
    id: ObjectId,
    list: list_one,
    nodes: [NodeId, NodeId]
}
'''
# We want to build an app
# Make an API
# How am I going to handle the data efficiently
# - What data is coming in...
# - How much data is coming in...
# - How you want to handle the data
# - access data
# - add data
# - update data
# - remove data
# - search for data
