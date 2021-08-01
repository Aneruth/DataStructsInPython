# Creating a Node
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None # Initialising the head as None
    
    def insetElement(self,data):
        newNode = Node(data) # Creates a new node
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else: self.head = newNode
    
    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.next
        return count
    
    def addLast(self,data):
        new_node = Node(data)
        # if our linked list is empty we create a new node
        if self.head is None:
                self.head = new_node
                return
        # if our linked list is not empty we traverse and insert at last
        last = self.head
        while (last.next):
            last = last.next
        last.next =  new_node
    
    def addFirst(self,data):
        # Create a new node with the data
        newNode = Node(data)
        # Swap our head as new node and rest of the element as next
        newNode.next,self.head = self.head,newNode
    
    def getFirst(self):
        # As we know the first data is head so we just returning the head of our linked list
        return self.head.data

    def fetch(self,index):
        current = self.head
        count = 0
        # traversing the node and if our count matches the index then we return the data
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        return 0

    # Method to display the list
    def display(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next


if __name__ == '__main__':
    LL = LinkedList()
    for i in range(1,11):
        LL.insetElement(i)    
    # LL.addFirst(11)
    # print(f'Length of the linked list is: {LL.size()}')
    # print(f'First Node in linked list is: {LL.getFirst()}')
    # LL.addLast(32)
    print(LL.fetch(4))
    LL.display()
