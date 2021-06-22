## [Contiguous Subarrays](https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=226517205173943)

You are given an array arr of N integers.
For each index i, you are required to determine the number of contiguous subarrays that fulfill the following conditions:

* The value at index i must be the maximum element in the contiguous subarrays, and
* These contiguous subarrays must either start from or end on index i.

__Signature__
```
int[] countSubarrays(int[] arr)
```

__Input__
* Array arr is a non-empty list of unique integers that range between 1 to 1,000,000,000
* Size N is between 1 and 1,000,000

__Output__
* An array where each index i contains an integer denoting the maximum number of contiguous subarrays of arr[i]

__Example:__
```
arr = [3, 4, 1, 6, 2]
output = [1, 3, 1, 5, 1]
```

__Explanation:__
```
For index 0 - [3] is the only contiguous subarray that starts (or ends) with 3, and the maximum value in this subarray is 3.
For index 1 - [4], [3, 4], [4, 1]
For index 2 - [1]
For index 3 - [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]
For index 4 - [2]
So, the answer for the above input is [1, 3, 1, 5, 1]
```
