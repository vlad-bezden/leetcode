## [Balance Brackets](https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=211548593612944)

A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].
We consider two brackets to be matching if the first element is an open-bracket, e.g., (, {, or [, and the second bracket is a close-bracket of the same type, e.g., ( and ), [ and ], and { and } are the only pairs of matching brackets.

Furthermore, a sequence of brackets is said to be balanced if the following conditions are met:
1. The sequence is empty, or
2. The sequence is composed of two, non-empty, sequences both of which are balanced, or
3. The first and last brackets of the sequence are matching, and the portion of the sequence without the first and last elements is balanced.

You are given a string of brackets. Your task is to determine whether each sequence of brackets is balanced. If a string is balanced, return true, otherwise, return false

__Signature__
```
bool isBalanced(String s)
```

__Input__
* String s with length between 1 and 1000

__Output__
* A boolean representing if the string is balanced or not

__Example 1__
```
s = {[()]}
output: true
```

__Example 2__
```
s = {}()
output: true
```

__Example 3__
```
s = {(})
output: false
```

__Example 4__
```
s = )
output: false
```
