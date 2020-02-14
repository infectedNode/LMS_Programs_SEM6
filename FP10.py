def check_pal(s):
    return s[0] == s[-1] and (len(s) < 3 or check_pal(s[1:-1]))
print(check_pal(input()))
