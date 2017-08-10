#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
546. Remove Boxes

Given several boxes with different colors represented by different positive numbers.
You may experience several rounds to remove boxes until there is no box left.
Each time you can choose some continuous boxes with the same color (composed of k boxes, k >= 1),
remove them and get k*k points.

Find the maximum points you can get.
Example 1:
Input:
[1, 3, 2, 2, 2, 3, 4, 3, 1]
Output:
23
Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1]
----> [1, 3, 3, 4, 3, 1] (3*3=9 points)
----> [1, 3, 3, 3, 1] (1*1=1 points)
----> [1, 1] (3*3=9 points)
----> [] (2*2=4 points)

Note: The number of boxes n would not exceed 100.
"""


# Is that HARD?? Just sum the square of count for each item
def sum_square_of_count(boxes):
    """
    :type boxes: List[int]
    :rtype: int
    """
    return sum([boxes.count(i) ** 2 for i in set(boxes)])


if __name__ == '__main__':
    print(sum_square_of_count([1, 3, 2, 2, 2, 3, 4, 3, 1]))
