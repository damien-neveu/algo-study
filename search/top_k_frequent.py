from typing import Dict, List
import random


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_frequencies = self.build_map_frequencies(nums)
        unique_numbers = list(map_frequencies.keys())
        if k >= len(unique_numbers):
            return unique_numbers
        pivot_index = random.randint(0, len(unique_numbers)-1)
        pivot_rightful_index = self.partition_around_pivot(pivot_index, unique_numbers, map_frequencies)
        target_pivot_index = len(unique_numbers) - k
        min_index_incl, max_index_incl = 0, len(unique_numbers) - 1
        while pivot_rightful_index != target_pivot_index:
            # old_pivot_index = pivot_rightful_index
            if pivot_rightful_index > target_pivot_index:
                max_index_incl = min(max_index_incl, pivot_rightful_index - 1)
            else:
                min_index_incl = max(min_index_incl, pivot_rightful_index + 1)
            pivot_index = random.randint(min_index_incl, max_index_incl)
            # print("target={}, prev={}, new={}, possible-range={}, nums={}".format(target_pivot_index, old_pivot_index,
            #                                                    pivot_index, [min_index_incl, max_index_incl], unique_numbers))
            pivot_rightful_index = self.partition_around_pivot(pivot_index, unique_numbers, map_frequencies)
        return unique_numbers[pivot_rightful_index:]

    def build_map_frequencies(self, nums: List[int]) -> Dict[int, int]:
        map_frequencies = {}
        for num in nums:
            if num in map_frequencies:
                map_frequencies[num] = map_frequencies[num] + 1
            else:
                map_frequencies[num] = 1
        return map_frequencies

    def partition_around_pivot(self, index: int, nums: List[int], map_frequencies: Dict[int, int]) -> int:
        i, j = 0, 1
        if len(nums) > 1:
            pivot_value = nums[index]
            pivot_frequency = map_frequencies[pivot_value]
            nums[0], nums[index] = nums[index], nums[0]
            while j < len(nums):
                if map_frequencies[nums[j]] < pivot_frequency or map_frequencies[nums[j]] == pivot_frequency and nums[j] < pivot_value:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
            nums[0], nums[i] = nums[i], nums[0]
        return i
