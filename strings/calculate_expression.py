
def calculate(s, i=0):
    res = 0
    sign_stack = [1]
    while i < len(s):
        c = s[i]
        if c == "(":
            inner_sum, inner_sum_end_index = calculate(s, i+1)
            res += inner_sum * sign_stack.pop()
            i = inner_sum_end_index
        elif c.isdigit():
            (num, end_index) = extract_num(s, i)
            res += num * sign_stack.pop()
            i = end_index
        elif c == "+":
            sign_stack.append(1)
            i += 1
        elif c == "-":
            sign_stack.append(-1)
            i += 1
        else: # c == ")"
            return res, i+1
    return res


def extract_num(string, starting_index):
    i = starting_index
    str_num = ""
    while i < len(string) and string[i].isdigit():
        str_num += string[i]
        i += 1
    return int(str_num), i



