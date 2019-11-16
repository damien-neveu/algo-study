
# Given a sorted array of numbers and a target value, return a range in an array that has the starting and ending indexes of the target value.
# For example, given the following inputs
#
# array: [1,2,2,2,2,2,2,2,5,6,7]
# target: 2
#
#
# The output is
#
# [1, 7]
# This is because the target value, 2, appears starting from index 1 to index 7 in the input array.
#
# try to do it in Olog(n)


def find_target_indexes(arr, target):
    print("hullo")
    if len(arr) == 0:
        return []
    s1, s2 = -1, -1
    start_i, end_i = 0, len(arr) - 1
    while start_i <= end_i:
        if arr[start_i] < target:
            start_i = int((end_i + start_i) / 2)
        elif arr[start_i] == target:
            s1 = start_i
            if arr[end_i] > target:
                end_i = int((end_i + start_i) / 2)
            elif arr[end_i] == target:
                s2 = end_i
            else:
                end_i = int((len(arr) + end_i) / 2)
        else:
            start_i = int(start_i / 2)
        print("start_i={}, end_i={}".format(str(start_i), str(end_i)))
    if s1 != -1 and s2 != -1:
        return [s1, s2]
    else:
        return []

# solution :
# function findRange(numbers, target) {
#   if (!numbers.length) {
#     return [];
#   }
#   let left = 0, right = numbers.length - 1;
#   let leftIndex = -1;
#   while (left <= right) {
#     const middle = Math.floor((left + right) / 2);
#     if (numbers[middle] >= target) {
#       if (numbers[middle] === target) {
#         leftIndex = middle;
#       }
#       right = middle - 1;
#     } else {
#       left = middle + 1;
#     }
#   }
#   left = 0, right = numbers.length - 1;
#   let rightIndex = -1;
#   while (left <= right) {
#     const middle = Math.floor((left + right) / 2);
#     if (numers[middle] <= target) {
#       if (numbers[middle] === target) {
#         rightIndex = middle;
#       }
#       left = middle + 1;
#     } else {
#       right = middle - 1;
#     }
#   }
#   return [leftIndex, rightIndex];
# }

if __name__ == "__main__":
    res = find_target_indexes([1,2,2,2,2,2,2,2,5,6,7], 2)
    print("res={}".format(str(res)))

