## [18. 4Sum](https://leetcode.com/problems/4sum/)
### Medium

Given an array `nums` of `n` integers, return an _array of all the **unique**
quadruplets_ `[nums[a], nums[b], nums[c], nums[d]]` such that:

* 0 <= a, b, c, d < n
* a, b, c, and d are distinct.
* nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

__Example 1:__
```
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

__Example 2:__
```
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
```

__Constraints:__
* 1 <= nums.length <= 200
* -109 <= nums[i] <= 109
* -109 <= target <= 109
