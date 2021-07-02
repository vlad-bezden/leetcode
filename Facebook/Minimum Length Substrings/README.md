## [Minimum Length Substrings](https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=2237975393164055)

You are given two strings s and t. You can select any substring of string s and rearrange the characters of the selected substring. Determine the minimum length of the substring of s such that string t is a substring of the selected substring.

__Signature__
```
int minLengthSubstring(String s, String t)
```

__Input__
`s` and `t` are non-empty strings that contain less than 1,000,000 characters each

__Output__
Return the minimum length of the substring of `s`. If it is not possible, return -1

__Example__
```
s = "dcbefebce"
t = "fd"
output = 5
```
_Explanation:_

Substring `"dcbef"` can be rearranged to `"cfdeb"`, `"cefdb"`, and so on. String `t` is a substring of `"cfdeb"`. Thus, the minimum length required is 5.
