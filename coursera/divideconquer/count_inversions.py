from typing import List


def sort_and_count_inversions(nums: List) -> (List, int):
    if len(nums) <= 1:
        return nums, 0
    else:
        mid_index = len(nums)//2
        (sorted_left_half, count_left_inversions) = sort_and_count_inversions(nums[:mid_index])
        (sorted_right_half, count_right_inversions) = sort_and_count_inversions(nums[mid_index:])
        (sorted_nums, count_split_inversions) = merge_and_count_split_inversions(sorted_left_half, sorted_right_half)
        return sorted_nums, count_left_inversions + count_right_inversions + count_split_inversions


def merge_and_count_split_inversions(left: List, right: List) -> (List, int):
    left_len, right_len = len(left), len(right)
    total_len = left_len + right_len
    left_index, right_index = 0, 0
    merged_sorted_nums = []
    count_split_inverts = 0
    for _ in range(total_len):
        if right_index >= right_len or left_index < left_len and left[left_index] <= right[right_index]:
            merged_sorted_nums.append(left[left_index])
            left_index += 1
        elif right_index < right_len:
            merged_sorted_nums.append(right[right_index])
            count_split_inverts += left_len - left_index
            right_index += 1
    return merged_sorted_nums, count_split_inverts
