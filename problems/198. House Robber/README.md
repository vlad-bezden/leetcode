## 198. House Robber
### easy

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint
stopping you from robbing each of them is that adjacent houses have
security system connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money
of each house, determine the maximum amount of money you can rob
tonight without alerting the police.



__Example 1:__

Input: nums = [1,2,3,1]<br/>
Output: 4<br/>
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).<br/>
Total amount you can rob = 1 + 3 = 4.

__Example 2:__

Input: nums = [2,7,9,3,1]<br/>
Output: 12<br/>
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and
rob house 5 (money = 1).<br/>
Total amount you can rob = 2 + 9 + 1 = 12.

__Example 3:__

Input: nums = [2,1,1,2]<br/>
Output: 4<br/>
Explanation: Rob house 1 (money = 2), rob house 4 (money = 2).<br/>
Total amount you can rob = 2 + 2 = 4

Constraints:

0 <= nums.length <= 100<br/>
0 <= nums[i] <= 400
