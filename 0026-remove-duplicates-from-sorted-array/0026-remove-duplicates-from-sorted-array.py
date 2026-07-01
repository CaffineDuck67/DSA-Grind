from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Pointer for the position of the next unique element
        k = 1

        # Start from the second element
        for i in range(1, len(nums)):
            # If current element is different, keep it
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        # Return the number of unique elements
        return k