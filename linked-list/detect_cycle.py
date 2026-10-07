"""
Problem: Linked List Cycle (Floyd's Cycle Detection)
Given head, the head of a linked list, determine if the linked list has a cycle in it.

Approach (Floyd's Tortoise and Hare):
- Use two pointers traversing at different velocities:
  - `slow` advances 1 step at a time.
  - `fast` advances 2 steps at a time.
- If there is no cycle, `fast` or `fast.next` reaches the end (None) and we return False.
- If a cycle exists, `fast` loops around and eventually meets `slow` at the same node.

Time Complexity: O(n) - The fast pointer travels at most 2 * n steps before meeting slow or terminating.
Space Complexity: O(1) - Only two pointer variables used.
"""
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    if not head or not head.next:
        return False
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


if __name__ == "__main__":
    # Test 1: List with cycle (3 -> 2 -> 0 -> -4 -> points back to 2)
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2
    print(f"Cycle list has_cycle: {has_cycle(n1)}")
    assert has_cycle(n1) is True

    # Test 2: List without cycle (1 -> 2 -> None)
    n_linear = ListNode(1, ListNode(2))
    print(f"Acyclic list has_cycle: {has_cycle(n_linear)}")
    assert has_cycle(n_linear) is False
