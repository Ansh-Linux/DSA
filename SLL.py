#Creating a class that creates a node which contains a value and pointer for the node
class Node:
    #This is a function that is called whenever a node is introduced
    def __init__(self, data, next=None):
        #This contains the node's value
        self.info = data
        #This contains the node's pointer
        self.next = next

#This is a class that assigns a node as the head of the SLL
class SLL:
    def __init__(self, head=None):
        self.head = head
    
    def endInsert(self, value):
        temp = Node(value)
        if(self.head != None):
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def frontInsert(self,value):
        temp = Node(value)
        head1 = self.head
        if(self.head != None):
            temp.next = head1
            self.head = temp
        else:
            self.head = temp
    
    def midInsert(self, value, next_node):
        temp = Node(value, next_node)
        if(temp.next == self.head):
            self.frontInsert(value)
        elif(temp.next == None):
            self.endInsert(value)
        else:
            t1 = self.head
            while(t1.next != next_node):
                t1 = t1.next
            t1.next = temp
            temp.next = next_node

    def delNode(self, value):
        t1 = self.head
        prev = Node(0)
        if(t1.info == value):
            self.head = t1.next
        else:
            while(t1.info != value):
                prev = t1
                t1 = t1.next
            if(t1.next != None):
                prev.next = t1.next
            else:
                prev.next = None

    def printSLL(self):
        t1 = self.head
        while(t1 != None):
            print(t1.info)
            t1 = t1.next

#Creating a Singly Linked list
Node3 = Node(200)
Node2 = Node(175, Node3)
Node1 = Node(150, Node2)

#Assigning the head of the Singly Linked List
obj = SLL(Node1)

#Testing the functions on the Singly Linked List
print(f'Printing the original SLL')
obj.printSLL()

print(f'Printing the list with the front insert')
obj.frontInsert(125)
obj.printSLL()

print(f'Printing the list with the front and the end insert')
obj.endInsert(225)
obj.printSLL()

print(f'Printing the lisr with front end and middle insert')
obj.midInsert(177, Node3)
obj.printSLL()

print(f'Printing the list with mulitple inserts and a deletion')
obj.delNode(177)
obj.printSLL()