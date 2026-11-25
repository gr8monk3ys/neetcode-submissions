"""
1. Two Sum
https://leetcode.com/problems/two-sum/

Difficulty: Easy

Problem:
    Given an array of integers `nums` and an integer `target`, return the
    indices of the two numbers that add up to `target`. Exactly one solution
    exists and the same element may not be used twice.

Approach:
    Single pass with a hash map from value -> index. For each number, check
    whether its complement (target - num) has already been seen.

Complexity:
    Time:  O(n)
    Space: O(n)
"""
from __future__ import annotations


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []  # unreachable given the problem's constraints
