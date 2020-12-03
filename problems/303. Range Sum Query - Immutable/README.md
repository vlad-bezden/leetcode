## [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)
### easy


Given an integer array nums, find the sum of the elements between
indices i and j (i ≤ j), inclusive.

Implement the NumArray class:

* NumArray(int[] nums) Initializes the object with the integer array nums.
* int sumRange(int i, int j) Return the sum of the elements of the nums
array in the range [i, j] inclusive (i.e., sum(nums[i], nums[i + 1], ... , nums[j]))

__Example 1:__<br/>
__Input__<br/>
["NumArray", "sumRange", "sumRange", "sumRange"]<br/>
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]<br/>
__Output__<br/>
[null, 1, -1, -3]

__Explanation__<br/>
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1])<br/>
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)<br/>
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))<br/>
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))

__Constraints:__<br/>
0 <= nums.length <= 104<br/>
-105 <= nums[i] <= 105<br/>
0 <= i <= j < nums.length<br/>
At most 104 calls will be made to sumRange.
