
class Acc:
    last_known_max = 0
    last_candidate_max = 0

    def get_max(self):
        return max(self.last_known_max, self.last_candidate_max)


def brute_calc_max_subarray_sum(arr):
    max_sum = 0
    for i, el in enumerate(arr):
        starting_index = i + 1
        ending_index = starting_index
        while ending_index <= len(arr):
            tentative_sum = el + sum(arr[starting_index:ending_index])
            if tentative_sum > max_sum:
                max_sum = tentative_sum
            ending_index += 1
    return max_sum


def calc_max_subarray_sum(arr):
    acc = Acc()
    for el in arr:
        new_max = acc.last_candidate_max + el
        if new_max <= 0:
            acc.last_candidate_max = 0
        else:
            acc.last_candidate_max = new_max
            if new_max > acc.last_known_max:
                acc.last_known_max = new_max
    return acc.get_max()
