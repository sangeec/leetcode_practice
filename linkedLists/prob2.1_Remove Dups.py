class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if not head:
        return

    seen = set()
    previous = None
    current = head

    while current:
        if current.data in seen:
            # Duplicate found, remove the node
            previous.next = current.next
        else:
            seen.add(current.data)
            previous = current
        current = current.next

# Example usage:

# Creating a sample linked list: 1 -> 3 -> 2 -> 1 -> 4 -> 3
head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(1)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(3)

# Removing duplicates with O(N) time complexity
remove_duplicates(head)

# Print the result
current = head
while current:
    print(current.data, end=" ")
    current = current.next
