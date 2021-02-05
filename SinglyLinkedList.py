class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def insertFirst(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            self.head = newNode
            newNode.next = temp
            del temp

    def insertAfter(self, newNode, afterNode):
        currNode = self.head
        while True:
            if currNode.data == afterNode.data:
                temp = currNode.next
                currNode.next = newNode
                newNode.next = temp
                del temp
                break
            currNode = currNode.next


    def printList(self):

        if self.head is None:
            print("List is empty")
        else:
            currNode = self.head
            while True:
                if currNode is None:
                    break
                print(currNode.data)
                currNode = currNode.next



firstNode = Node("Shailesh")
linkedList = LinkedList()
linkedList.insertEnd(firstNode)
secondNode = Node("Anuj")
linkedList.insertEnd(secondNode)
thirdNode = Node("Rinky")
linkedList.insertEnd(thirdNode)
linkedList.printList()
print("=================================")
headNode = Node("Head")
linkedList.insertFirst(headNode)
linkedList.printList()
print("=================================")
btwnNode = Node('Between')
linkedList.insertAfter(btwnNode, secondNode)
linkedList.printList()