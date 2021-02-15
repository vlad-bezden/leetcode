## [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
### Easy

<br/>
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach,
which is more subtle.

__Example 1:__<br/>
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]<br/>
Output: 6<br/>
Explanation: [4,-1,2,1] has the largest sum = 6.<br/>

__Example 2:__<br/>
Input: nums = [1]<br/>
Output: 1<br/>

__Example 3:__<br/>
Input: nums = [0]<br/>
Output: 0<br/>

__Example 4:__<br/>
Input 4:<br/>
nums = [-1]<br/>
Output: -1<br/>

__Example 5__:<br/>
Input 5:<br/>
nums = [-2147483647]<br/>
Output: -2147483647<br/>


__Constraints:__<br/>
1 <= nums.length <= 2 * 104<br/>
-231 <= nums[i] <= 231 - 1<br/>
