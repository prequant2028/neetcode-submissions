class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def get(self, index: int) -> int:
        if 0 <= index < self.size:
            cur = self.head

            for i in range(index):
                cur = cur.next

            return cur.val

        return -1


    def addAtHead(self, val: int) -> None:
        node = Node(val)

        if self.head:
            node.next = self.head
            self.head.prev = node
        else:
            self.tail = node

        self.head = node
        self.size += 1


    def addAtTail(self, val: int) -> None:
        node = Node(val)

        if self.tail:
            node.prev = self.tail
            self.tail.next = node
        else:
            self.head = node

        self.tail = node
        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)

        elif index == self.size:
            self.addAtTail(val)

        else:
            cur = self.head

            # Move to the node before the insertion position
            for i in range(index - 1):
                cur = cur.next

            node = Node(val)
            cur2 = cur.next

            cur.next = node
            node.prev = cur

            node.next = cur2
            cur2.prev = node

            self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        # Delete head
        if index == 0:
            self.head = self.head.next

            if self.head:
                self.head.prev = None
            else:
                self.tail = None

        # Delete tail
        elif index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None

        # Delete middle node
        else:
            cur = self.head

            for i in range(index):
                cur = cur.next

            cur.prev.next = cur.next
            cur.next.prev = cur.prev

        self.size -= 1