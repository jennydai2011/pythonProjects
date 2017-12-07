from linkedlistdemo.LinkedList import LinkedList

linkedList = LinkedList()
linkedList.insertStart(12)
linkedList.insertStart(22)
linkedList.insertStart(32)
linkedList.insertEnd(122)

print('print after add all elements')
linkedList.traverseList()


linkedList.remove(12)
print('print after remove from start')
linkedList.traverseList()

linkedList.remove(122)
print('print after remove from end')
linkedList.traverseList()
