# https://leetcode.com/problems/longest-absolute-file-path/description/
# Given a string, find the longest path length

# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

# dir
#    subdir1
#        file1.ext
#        subsubdir1
#    subdir2
#        subsubdir2
#            file2.ext
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty
# second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
# Note:
# The name of a file contains at least a . and an extension.
# The name of a directory or sub-directory will not contain a ..

# Suppose we abstract our file system by a string in the following manner:
# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
#
# dir
#     subdir1
#     subdir2
#         file.ext
#
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
#
# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
#
# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
#
# We are interested in finding the longest (number of characters) absolute path to a file within our file system.
# Here the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).
#
# Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system.
# If there is no file in the system, return 0.
#
# Notes:
# The name of a file contains at least a . and an extension
# The name of a directory or sub-directory will not contain a .
# Time complexity required: O(n) where n is the size of the input string
# Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.


def lengthLongestPath(self, input):
    elems = input.split("\n")
    stack = []
    max_length, stack_length = 0, 0
    stack_level = 0
    for elem in elems:
        level, path = extract_level_and_path(elem)
        path_length = len(path) + 1
        # print("level = {}, path = {}, path_length = {}".format(str(level), path, str(path_length)))
        while stack_level >= level and len(stack) > 0:
            pre_path_length = stack.pop()
            stack_level -= 1
            stack_length -= pre_path_length
        # print("stack_level = {}, stack_length = {}".format(str(stack_level), str(stack_length)))
        stack.append(path_length)
        stack_level += 1
        stack_length += path_length
        max_length = max(max_length, stack_length) if self.is_file(path) else max_length
        # print("stack = {}".format(str(stack)[1:-1]))
    return max_length - 1 if max_length > 0 else 0


def extract_level_and_path(self, s):
    level = 1
    while s.startswith("\t"):
        level += 1
        s = s[1:]
    return level, s


def is_file(self, s):
    for c in s:
        if c == ".":
            return True
    return False
