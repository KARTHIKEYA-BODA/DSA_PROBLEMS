# Reverse a singly linked list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


# helper to create linked list from normal python list
def build_linked_list(values):
    dummy = ListNode(0)
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


# helper to convert linked list back to python list for display
def to_list(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


if __name__ == "__main__":
    head = build_linked_list([1, 2, 3, 4, 5])
    reversed_head = reverse_list(head)
    out = to_list(reversed_head)
    print("Reversed list:", out)
    assert out == [5, 4, 3, 2, 1]
