from LinkedList import *

LL = LinkedList()
LL.addLast(12)
LL.addLast(1)
LL.addLast(23)
LL.addLast(0)
LL.addLast(2)

# LL2 = LinkedList() # Second Linked List
# LL.addLast(14)
# LL.addLast(22)
# LL.addLast(3)

print(f'\nLength of the linked list is: {LL.size()}')
# print(f'\nFirst Node in linked list is: {LL.getFirst()}')
# print(f'\nFetch value is: {LL.fetch(4)}')
# print(f'\nLinked List is: {LL.display()}')
# print(f'\nLast element is: {LL.getLast()}')
# print(f'\nSecond Linked List is: {LL2.display()}')
# LL2.fropple()
# LL.appendLinkedList(LL2)
# print(f'\nLinked List after appending new list is: {LL.display()}')
# print(f'\nLinked List after adding new list is: {LL.display()}')
# LL.reverse()
# LL.sortList()
# print(f'\nLinked List after sorting is: {LL.display()}')
LL.insertElements(5)
print(f'\nLinked List is: {LL.display()}')