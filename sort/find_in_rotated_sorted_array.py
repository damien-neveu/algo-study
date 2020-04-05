

def find_elem(arr, elem):
    next_move_length = len(arr)
    curr_index = next_move_length // 2
    while next_move_length > 0:
        next_move_length = next_move_length // 2
        print("curr_index={}, next_move_length={}".format(curr_index, next_move_length))
        if arr[curr_index] == elem:
            return len(arr) + curr_index if curr_index < 0 else curr_index
        elif arr[curr_index] < elem:
            curr_index = (curr_index + next_move_length) % (len(arr) - 1)
        else:
            curr_index -= next_move_length
    return None
