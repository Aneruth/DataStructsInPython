class Stack:

    def __init__(self):
        self.empty_list = []
    
    # Push an element to stack
    def push(self,data):
        self.empty_list.append(data)

    # Pop an element from stack
    def pop(self):
        if self.empty_list is None:
            return 'Elements Not present in stack table'
        return f'Popped Eleemnt is {self.empty_list.pop()}'
    
    # To pop an element based on index position
    def popElementBasedOnIndex(self,idx):
        if self.empty_list is None:
            return 'Elements Not present in stack table'
        return f'Popped Element based on index is {self.empty_list.pop(idx)}'
    
    # To check if stack is empty or not which returns boolean value
    def to_check(self):
        if self.empty_list == []:
            return True
        return False
    
    # To check for a specfic element present in our stack table return boolean value.
    def lookUp(self,data):
        for i in range(len(self.empty_list)):
            if data == self.empty_list[i]:
                return True
        return False
    
    # To check for a specfic element present in our stack table returns index values of target element.
    def getIndex(self,data):
        for i in range(len(self.empty_list)):
            if data == self.empty_list[i]:
                return self.empty_list.index(data)
        return f'{data} not present in Stack Table.'
    
    # To sort the data present in our stack table. (used Bubble sort to implement sorting)
    def sort(self):
        for i in range(len(self.empty_list)):
            for j in range(len(self.empty_list)-1):
                if self.empty_list[i] > self.empty_list[j]:
                    self.empty_list[i],self.empty_list[j] = self.empty_list[j],self.empty_list[i]
        return self.empty_list[::-1]
    
    # To get the minimum element from our stack table.
    def getMin(self):
        return min(self.empty_list)
    
    # Increment element in certain range with desired value in our stack table.
    def incerementVal(self,k,val):
        for i in range(k,len(self.empty_list)):
            self.empty_list[i] += val
        return self.empty_list
    
    # Change position of list elements 
    def positionChange(self,n):
        return self.empty_list[n:] + self.empty_list[:n]
    
    # To check if stack table consist of repeated value.
    def checkDuplicates(self):
        if len(self.empty_list) == len(set(self.empty_list)):
            return False
        return True
    
    # Sorting the list based on odd and even list. 
    def sortOddEven(self):
       return list(sorted(self.empty_list, key=lambda x: [x % 2, x]))
            
            
    # To dispaly the stack elements
    def display(self):
        if self.empty_list is None:
            return None
        return self.empty_list


if __name__ == "__main__":
    stack_table = Stack()
    stack_table.push(5)
    stack_table.push(8)
    stack_table.push(1)
    stack_table.push(10)
    stack_table.push(41)
    stack_table.push(24)
    stack_table.push(2)
    print(f'Actual Stack {stack_table.display()}')
    # print(stack_table.popElementBasedOnIndex(3))
    # print(stack_table.to_check())
    # print(stack_table.lookUp(4))
    # print(stack_table.getIndex(2))
    # print(f'Sorted Stack is {stack_table.sort()}')
    # print(f'Incremented Stack is {stack_table.incerementVal(3,12)}')
    # print(f'Changed position of list is {stack_table.positionChange(1)}')
    # print(f'Is there any duplicate value {stack_table.checkDuplicates()}')
    # print(stack_table.sortOddEven())