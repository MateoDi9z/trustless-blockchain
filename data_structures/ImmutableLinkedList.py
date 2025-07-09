class ImmutableLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

        def __repr__(self):
            return str(self.data)

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def getLast(self) -> Node | None:
        if self.is_empty():
            return None
        return self.head

    def append(self, data) -> None:
        if self.is_empty():
            self.head = self.Node(data)
            self.tail = self.head
            self.size += 1
            return

        node = self.Node(data)
        node.next = self.head
        self.head = node
        self.size += 1

    def at(self, idx):
        if self.is_empty() or idx < 0 or idx >= self.size:
            return None

        ptr = self.head
        for i in range(0, self.size)[::-1]:
            if i == idx:
                return ptr.data
            ptr = ptr.next

    def __repr__(self) -> str:
        if self.is_empty():
            return "Empty List"

        t = ""
        ptr = self.head
        while ptr is not None:
            t += f"{ptr.data} => "
            ptr = ptr.next
        return t

    def __iter__(self):
        return ImmutableLinkedListIterator(self.head)


class ImmutableLinkedListIterator:
    def __init__(self, node):
        self.current = node

    def __iter__(self):
        return self

    def __next__(self) -> ImmutableLinkedList.Node:
        if not self.current:
            raise StopIteration
        node = self.current
        self.current = self.current.next
        return node
