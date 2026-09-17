class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        new = sorted(numbers)
        i, j = 0, len(new)-1
        while(i < j):
            curr_sum = new[i] + new[j]
            if curr_sum < target:
                i += 1
            elif curr_sum > target:
                j -= 1
            elif curr_sum == target:
                return[i+1,j+1]
        return []