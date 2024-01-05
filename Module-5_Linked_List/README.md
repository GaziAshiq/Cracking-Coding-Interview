# Assignment on Linked List
## Task 1:
Write a function that does the following task.
### Given the head of a singly linked list, reverse the list, and return the reversed list.
(You must create the linked list and pass the head to the function you created.)
Also, mention the Time and Space Complexity of your solution.
Constraints: 
#### The number of nodes in the list is the range [0, 5000].
#### -5000 <= Node.val <= 5000


#### Example 1:
Input: head = [1,2,3,4,5] 
Output: [5,4,3,2,1]


Explanation:
Given linked list: head -> 1 -> 2 -> 3 -> 4 -> 5
Output linked list: head -> 5 -> 4 -> 3 -> 2 -> 1


#### Example 2:
Input: head = [1,2]
Output: [2,1]


Explanation:
Given linked list: head -> 1 -> 2
Output linked list: head ->2 -> 1


#### Example 3:
Input: head = []
Output: []


 


## Task 2:


Write a function that does the following task.


### You are given the heads of two sorted linked lists list1 and list2.


### Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.


### Return the head of the merged linked list.


(You must create the linked lists and pass the head to the function you created.)


Also, mention the Time and Space Complexity of your solution


Constraints: 
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
#### Both list1 and list2 are sorted in non-decreasing order.



#### Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]


Explanation:
Given linked lists
list1: head -> 1 -> 2 -> 4
list2: head -> 1 -> 3 -> 4
Output linked list: head -> 1 -> 1 -> 2 -> 3 -> 4 -> 4


#### Example 2:
Input: list1 = [], list2 = []
Output: []


#### Example 3:
Input: list1 = [], list2 = [0]
Output: [0]


Explanation:
Given linked lists
list1: head ->
list2: head -> 0
Output linked list: head -> 0

