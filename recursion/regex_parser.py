
def is_match(text: str, pattern: str):
    letters = list(text)
    rx = list(pattern)

    def inner(t, r):
        if not t:
            if not r or r == ".*" or r == "*":
                return True
            else:
                return False


    return inner(letters, rx)
