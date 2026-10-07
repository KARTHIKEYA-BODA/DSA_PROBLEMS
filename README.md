# DSA Python

A structured Python repository for Data Structures and Algorithms with clean implementations, time/space complexity analysis, and approach explanations.

---

## 📁 Repository Structure

```
dsa-python/
├── arrays/
│   ├── two_sum.py
│   └── maximum_subarray.py
├── strings/
│   ├── valid_palindrome.py
│   └── valid_anagram.py
├── linked-list/
│   ├── reverse_linked_list.py
│   └── detect_cycle.py
├── sorting/
│   ├── merge_sort.py
│   └── quick_sort.py
└── README.md
```

---

## 🧠 Problems & Complexity Overview

| Category | Problem | Approach | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- | :--- |
| **Arrays** | Two Sum | Hash Map (Complement Lookup) | $O(n)$ | $O(n)$ |
| **Arrays** | Maximum Subarray | Kadane's Algorithm | $O(n)$ | $O(1)$ |
| **Strings** | Valid Palindrome | Two Pointers (Inward Scan) | $O(n)$ | $O(1)$ |
| **Strings** | Valid Anagram | Character Frequency Counter | $O(n)$ | $O(1)$ |
| **Linked List** | Reverse Linked List | Iterative In-Place Pointer Swap | $O(n)$ | $O(1)$ |
| **Linked List** | Detect Cycle | Floyd's Cycle-Finding Algorithm | $O(n)$ | $O(1)$ |
| **Sorting** | Merge Sort | Divide and Conquer | $O(n \log n)$ | $O(n)$ |
| **Sorting** | Quick Sort | Lomuto Partitioning | $O(n \log n)$ avg | $O(\log n)$ stack |

---

## 🚀 Running the Solutions

Each script contains runnable test cases with assertions. You can run any file directly with Python:

```bash
# Run Arrays problems
python arrays/two_sum.py
python arrays/maximum_subarray.py

# Run Strings problems
python strings/valid_palindrome.py
python strings/valid_anagram.py

# Run Linked List problems
python linked-list/reverse_linked_list.py
python linked-list/detect_cycle.py

# Run Sorting algorithms
python sorting/merge_sort.py
python sorting/quick_sort.py
```
