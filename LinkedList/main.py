from LinkedList import *

LL = LinkedList()
for i in range(1,5):
    LL.insetElement(i)    

LL2 = LinkedList() # Second Linked List
for j in range(6,11):
    LL2.insetElement(j)

print(f'Length of the linked list is: {LL.size()}')
print(f'First Node in linked list is: {LL.getFirst()}')
print(f'Fetch value is: {LL.fetch(4)}')
print(f'Linked List is: {LL.display()}')
print(f'Last element is: {LL.getLast()}')
LL.swapElement()
print(f'Linked List after swapping is: {LL.display()}')
print(f'Linked List First element after swapping is: {LL.getFirst()}')
