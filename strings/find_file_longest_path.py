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
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
# Note:
# The name of a file contains at least a . and an extension.
# The name of a directory or sub-directory will not contain a ..


def length_longest_path(input):
    elems = input.split('\n')
    paths = []
    for elem in elems[::-1]:
        print("TODO")
    return


def is_file(str):
    return "." in str