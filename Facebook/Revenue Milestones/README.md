## [Revenue Milestones](https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=192049171861831)

We keep track of the revenue Facebook makes every day, and we want to know on what days Facebook hits certain revenue milestones. Given an array of the revenue on each day, and an array of milestones Facebook wants to reach, return an array containing the days on which Facebook reached every milestone.

__Signature__
```
int[] getMilestoneDays(int[] revenues, int[] milestones)
```

__Input__
* revenues is a length-N array representing how much revenue FB made on each day (from day 1 to day N). milestones is a length-K array of total revenue milestones.

__Output__
Return a length-K array where K_i is the day on which FB first had milestones[i] total revenue. If the milestone is never met, return -1.

__Example__
```
revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
milestones = [100, 200, 500]
output = [4, 6, 10]
```
__Explanation__
On days 4, 5, and 6, FB has total revenue of $100, $150, and $210 respectively. Day 6 is the first time that FB has >= $200 of total revenue.
