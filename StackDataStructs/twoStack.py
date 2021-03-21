class Stack:

    def __init__(self):
        self.stackOne = []
        self.stackTwo = []

    
    # Push an element to stack
    def push(self,data):
        self.stackOne.append(data)

    # Pop an element from stack 1 and push it to stack two.
    def pop(self):
        if self.stackOne is None:
            return 'Elements Not present in stack table'
        # Push the poped element from stack 1 to stack 2
        self.stackTwo.append(self.stackOne.pop())
        return self.stackTwo
    
    def display(self):
        if self.stackOne and self.stackTwo is None:
            return None
        return self.stackTwo


if __name__ == '__main':
    stack = Stack()
    stack.push(3)
    stack.push(1)
    stack.push(6)
    stack.push(10)
    stack.pop()
    print(stack.display())
    