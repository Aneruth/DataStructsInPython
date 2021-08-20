from LinkedList import LinkedList

class priorityQueue():
    def __init__(self,element=None,priority=None):
        self.element = element
        self.priority = priority

    LL = LinkedList()

    def push(self,data,priority):
        newPriorityPair = (data,priority)
        LL.addFirst(newPriorityPair)
    
    def toString(self):
        # output = []
        # current = self.head
        # while(current):
        #     output.append(current.data)
        #     # print(current.data)
        #     current = current.next
        return 

if __name__ == '__main__':
    pq = priorityQueue()
    pq.push(23,1)
    print(pq)