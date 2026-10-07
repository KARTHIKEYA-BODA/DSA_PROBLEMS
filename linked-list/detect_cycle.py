# Check if a linked list has a cycle using fast and slow pointers


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # if both pointers meet, there is a cycle
        if slow == fast:
            return True

    return False


if __name__ == "__main__":
    # list with cycle: 3 -> 2 -> 0 -> -4 -> back to 2
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2

    print("Has cycle:", has_cycle(n1))
    assert has_cycle(n1) is True

    # list without cycle: 1 -> 2
    linear = ListNode(1, ListNode(2))
    print("Has cycle:", has_cycle(linear))
    assert has_cycle(linear) is False
