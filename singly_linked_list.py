class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list.
    """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        """ Show a string representation of the data object. """

        return "<Node data: %s>" % self.data


class LinkedList:
    """
    Singly linked list.
    """

    def __init__(self):
        self.head = None

    def size(self):
        """
        Return the numbers of nodes in the list.
        Takes - 0(n) or linear - time.
        """

        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next_node

        return count

    def is_empty(self):
        return self.head is None

    def add(self, data):
        """
        Adds new Node containing data at head of the list.
        Takes - O(1) or constant - time.
        """

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        current = self.head

        while current:
            """
            Search for the first node containing data that matches the key.
            Return the node or 'None' if not found
            Takes - O(n) or lineal - time.
            """
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position.
        Insertion takes - O(1) or constant - time, but finding
        the node at the insertion point takes - O(n) or lineal - time.
        Takes overall - O(n) or lineal - time.
        """

        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = Node.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.net_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        Removes Node containing data that matches the key.
        Returns the Node or None if key doesn't exist.
        Takes O(n)
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current

    def __repr__(self):
        """
        Return a string representation of the list object.
        Takes - O(n) or lineal - time.
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s}" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return ' -> '.join(nodes)


linked_list = LinkedList()
linked_list.add(5)
linked_list.add(4)
linked_list.add(3)
linked_list.add(2)
linked_list.add(1)
print(linked_list)
print(linked_list.search(5))
print(linked_list.search(50))