from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            self.current.value = item
            self.current = self.current.next
            if self.current == None:
                self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        if len(self.storage) > 0:
            current = self.storage.head
            while current != None:
                list_buffer_contents.append(current.value)
                current = current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.currentIndex = 0
        self.storage = [None for num in range(0, capacity)]

    def append(self, item):
        self.storage[self.currentIndex] = item
        self.currentIndex += 1
        if self.currentIndex >= self.capacity:
            self.currentIndex = 0

    def get(self):
        return [item for item in self.storage if item != None]
