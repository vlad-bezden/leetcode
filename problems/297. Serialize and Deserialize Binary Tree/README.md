## [297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
### Hard

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

__Clarification:__

The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

__Example 1:__
```
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
```

__Example 2:__
```
Input: root = []
Output: []
```

__Example 3:__
```
Input: root = [1]
Output: [1]
```

__Example 4:__
```
Input: root = [1,2]
Output: [1,2]
```

__Constraints:__

* The number of nodes in the tree is in the range [0, 104].
* -1000 <= Node.val <= 1000
