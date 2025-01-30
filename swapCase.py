def swap_case(s):
    ans = ""
    for char in s:
        if char.islower():
            ans += char.upper()
        elif char.isupper():
            ans += char.lower()
        else:
            ans += char
    return ans
