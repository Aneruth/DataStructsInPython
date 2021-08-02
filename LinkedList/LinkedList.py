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
        if self.size() == 0: return 'No element in list'
        # As we know the first data is head so we just returning the head of our linked list
        return self.head.data
    
    def getLast(self):
        if self.size() == 0: return 'No element in list'
        return self.display()[-1]

    def fetch(self,index):
        current = self.head
        count = 0
        if self.size() == 0: return 'No element in list'
        # traversing the node and if our count matches the index then we return the data
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        return 'List Index outbound'
    
    '''
    # Method 1 using while loop
    def fropple(self):
        current = self.head
        while current and current.next:
            if current.data != current.next.data:
                current.data,current.next.data = current.next.data,current.data
            current = current.next.next
        return current.data
    '''
    
    def swapElement(self):
        current = self.head
        if self.size() == 0: return 'No element in the list'
        for i in range(self.size()):
            if i % 2 == 0:
                current.data,current.next.data = current.next.data,current.data
        return current.data
    
    def appendLinkedList(self,item):
        new_node = Node(item)
        current = self.head
        
        if current is None: current = new_node

        last = self.head
        while last.next != None:
            last = last.next
        last.next = new_node
        return new_node.data

    '''
    def mergeAlternate(self, q):
        p_curr = self.head
        q_curr = q.head
 
        # While there are available positions in p;
        while p_curr != None and q_curr != None:
 
            # Save next pointers
            p_next = p_curr.next
            q_next = q_curr.next
 
            # make q_curr as next of p_curr
            q_curr.next = p_next # change next pointer of q_curr
            p_curr.next = q_curr # change next pointer of p_curr
 
            # update current pointers for next iteration
            p_curr = p_next
            q_curr = q_next
        q.head = q_curr
    '''
    # Method to display the list
    def display(self):
        if self.size() == 0: return 'No element in list'
        output = []
        current = self.head
        while(current):
            output.append(current.data)
            # print(current.data)
            current = current.next
        return output