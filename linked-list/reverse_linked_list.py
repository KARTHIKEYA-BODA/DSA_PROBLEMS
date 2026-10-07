"""
Problem: Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

Approach (Iterative In-Place Pointer Reversal):
- Maintain three pointers:
  - `prev`: references the previous node (initialized to None).
  - `curr`: references the current node being processed (starts at head).
  - `nxt`: temporarily holds the next node (`curr.next`).
- In each iteration:
  1. Save `curr.next` in `nxt`.
  2. Invert pointer: `curr.next = prev`.
  3. Advance `prev = curr`.
  4. Advance `curr = nxt`.
- When `curr` is None, `prev` points to the new head.

Time Complexity: O(n) - Single traversal of n nodes in the list.
Space Complexity: O(1) - Constant space in-place manipulation.
"""
from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev: Optional[ListNode] = None
    curr: Optional[ListNode] = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> List[int]:
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
    print(f"Reversed Linked List: {out}")
    assert out == [5, 4, 3, 2, 1]
