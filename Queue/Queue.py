# Implement Queue
class Queue:
    def __init__(self):
      self.queue = []

    def enQueue(self, value: int):
        return self.queue.append(value)

    def deQueue(self):
      return f'deQueue element is {self.queue.pop(-1)}'
        
    def Front(self):
      return f'Front element is {self.queue[-1]}'  # Returns bottom most element present

    def Rear(self):
        return f'Bottom element is {self.queue[0]}' # Returns top most element present

    def isEmpty(self):
        if self.queue is None:
          return f"Is Queue is empty {True}"
        return f"Is Queue is empty {False}"

    def isFull(self):
      if self.queue:
        return f"Is Queue is full {True}"
      return f"Is Queue is full {False}"
    
    def display(self):
      return self.queue
    
q = Queue()
for i in range(1,15):
  q.enQueue(i)
print(q.deQueue())
print(q.Front())
print(q.Rear())
print(q.isEmpty())
print(q.isFull())
print(q.display())