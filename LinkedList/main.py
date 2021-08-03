from LinkedList import *

LL = LinkedList()
# for i in range(1,5):
#     LL.insetElement(i)    
LL.addLast(12)
LL.addLast(1)
LL.addLast(23)
LL.addLast(0)
LL.addLast(2)
# LL2 = LinkedList() # Second Linked List
# for j in range(6,13):
#     LL2.insetElement(j)

# print(f'Length of the linked list is: {LL.size()}')
# print(f'First Node in linked list is: {LL.getFirst()}')
# print(f'Fetch value is: {LL.fetch(4)}')
# print(f'Linked List is: {LL.display()}')
# print(f'Last element is: {LL.getLast()}')
# print(f'Second Linked List is: {LL2.display()}')
# LL2.fropple()
# LL.appendLinkedList(LL2)
# print(f'Linked List after appending new list is: {LL.display()}')
# print(f'Linked List after adding new list is: {LL.display()}')
# LL.reverse()
LL.sortList()
print(f'Linked List after appending new list is: {LL.display()}')