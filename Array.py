class ArrayNode:
    def __init__(self, value):
        self.value = value
        self.next = None

### --- PURE ARRAY IMPLEMENTATION --- ###
class Array:
    """
    This class helps simulate an array by using linked lists.
    """
    def __init__(self, size):
        self.size = size
        self.head = None
        self.count = 0

    def get(self, index):
        """
        The function helps get a value at a specified index given by the input.
        """
        if index < self.size and index >= 0:
            curr = self.head
            for xy in range(index):
                if curr is None:
                    return None
                curr = curr.next # moves to the next node until it gets to the index
            if curr is None:
                return None
            else:
                return curr.value
        else:
            return None

    def set(self, index, value):
        """
        The function helps set a value at an index which is given by the input
        """
        if 0 <= index < self.size:
            if self.head is None:
                # Create first node
                self.head = ArrayNode(value)
                current = self.head
                # Create nodes up to the index
                for xy in range(index):
                    current.next = ArrayNode(None) # it sets empty nodes and goes until the index
                    current = current.next
            else:
                current = self.head
                # Traverse to the index
                for xy in range(index):
                    if current.next is None:
                        current.next = ArrayNode(None) # will make an empty node if that node corresponding to the index isn't there
                    current = current.next
                current.value = value
            return True
        return False