
def next_permutation(nums):
    if len(nums) < 2:
        return nums
    p = index_first_num_lesser_than_its_follower(nums)
    q = index_right_num_greater_and_closer_to(p, nums)
    if p == 0 and q == 0:
        return sorted(nums)
    nums[p], nums[q] = nums[q], nums[p]
    if p < len(nums) - 1:
        nums[p+1:] = sorted(nums[p+1:])
    return nums


def index_first_num_lesser_than_its_follower(nums):
    for i in range(len(nums) - 1, 0, -1):
        if nums[i - 1] < nums[i]:
            return i - 1
    return 0


def index_right_num_greater_and_closer_to(p, nums):
    p_val = nums[p]
    greater_index, greater_val = None, None
    for i in range(p, len(nums)):
        if nums[i] > p_val and (greater_val is None or nums[i] < greater_val):
            greater_val = nums[i]
            greater_index = i
    return p if greater_index is None else greater_index



