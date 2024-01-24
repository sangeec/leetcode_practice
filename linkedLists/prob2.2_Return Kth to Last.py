class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def kth_to_last_recursive(node, k, index):
    if not node:
        return None, 0
    
    result, current_index = kth_to_last_recursive(node.next, k, index + 1)

    if current_index == k:
        return node.value, current_index

    return result, current_index + 1

def find_kth_to_last(head, k):
    result, _ = kth_to_last_recursive(head, k, 0)
    return result

# Creating a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

k = 2
result = find_kth_to_last(head, k)
print(f"The {k}th to last element is: {result}")
