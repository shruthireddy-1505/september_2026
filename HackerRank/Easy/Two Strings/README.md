# Two Strings

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Two Strings](https://www.hackerrank.com/challenges/two-strings/problem)

## Problem Description

Given two strings, determine if they share a common substring.  A substring may be as small as one character.

**Example** **

These share the common substring .

These do not share a substring.

Function Description**

Complete the function *twoStrings* in the editor below.

twoStrings has the following parameter(s):

* *string s1:* a string

* *string s2:* another string

**Returns**

* *string:* either `YES` or `NO`

**Input Format**

The first line contains a single integer , the number of test cases.

The following  pairs of lines are as follows:

* The first line contains string .

* The second line contains string .

**Constraints**

*  and  consist of characters in the range ascii[a-z].

*

*

**Output Format**

For each pair of strings, return `YES` or `NO`.

**Sample Input**

```
2
hello
world
hi
world

```

**Sample Output**

```
YES
NO

```

**Explanation**

We have  pairs to check:

* , . The substrings  and  are common to both strings.

* , .  and  share no common substrings.

## Examples



## Constraints



## Solution

```python3
# HackerRank Problem: Two Strings
# Link: https://www.hackerrank.com/challenges/two-strings/problem
# Difficulty: Easy
# Language: python3

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    for i in s1:
        if i in s2:
            return "YES"
    return "NO"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
