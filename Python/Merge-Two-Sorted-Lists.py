"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

def MergeTwoLists(l1,l2):
    l1.extend(l2)
    sorted_list = sorted(l1)
    return sorted_list

print(MergeTwoLists([1,2,4],[1,3,4]))


