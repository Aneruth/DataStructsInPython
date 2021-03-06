class Node:
    def __init__(self,data=None,next=None,position = 0):
        self.data = data
        self.next = next
        self.position = position
    
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
        # if our nexted list is empty we create a new node
        if self.head is None:
                self.head = new_node
                return
        # if our nexted list is not empty we traverse and insert at last
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
        # As we know the first data is head so we just returning the head of our nexted list
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

    '''  Method 2 
    def swapNodes(self):
        cur = self.head
        while cur and cur.next:
            cur.data, cur.next.data = cur.next.data, cur.data
            cur = cur.next.next
        
        return head
    '''
    
    def swapElement(self):
        current = self.head
        if self.size() == 0: return 'No element in the list'
        for i in range(self.size()):
            if i % 2 == 0:
                current.data,current.next.data = current.next.data,current.data
        return current.data
    
    def appendLinkedList(self,newList):
        current = self.head
        # if our head is null so we assign the head as new list
        if current is None: current = newList

        # dummy head 
        last = self.head
        while last.next != None: last = last.next
        # adding the new list at last using addLast method
        last.next = self.addLast(Node(newList))

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
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            nextElement = current.next
            current.next = prev
            prev = current
            current = nextElement
        self.head = prev 

    def sortList(self):
        swap = 0
        current = self.head
        if current != None:
            while(1):
                swap = 0
                tmp = current
                while(tmp.next != None):
                    if tmp.data > tmp.next.data:
                        # swap them
                        swap += 1
                        p = tmp.data
                        tmp.data = tmp.next.data
                        tmp.next.data = p
                        tmp = tmp.next
                    else:
                        tmp = tmp.next
                if swap == 0:
                    break
                else:
                    continue
            return current
        return current
    
    def index(self,item):
        current = self.head
        while current != None:
            if current.data == item:
                return current.position
            current = current.next
        # return 

    def InsertNth(self, data, position):
        start = self.head
        if position == 0:
            return Node(data, self.head)
        while position > 1:
            self.head = self.head.next
            position -= 1
        self.head.next = Node(data, self.head.next)
        return start
    
    def insertElements(self,newData):
        current = self.head
        # if the data not in linked list add at first
        if newData != current.data: self.addFirst(newData)
        while current != None:
            if current.data == newData:
                self.InsertNth(newData,self.index(current.data)+1)
            current = current.next
        # return self.sortList()

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