def longestPalindrome(s: str) -> str:
    if len(s) < 2 or s[0] == s[-1]:
        return s
    reserve = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) - 1):
            if s[i] == s[j] and s[i] != s[j + 1]:
                reserve = s[i : j + 1] if len(reserve) < len(s[i : j + 1]) else reserve
                return reserve
            elif s[i] == s[-1]:
                return s
    return s[0]


sr = "abb"
res = longestPalindrome(sr)
print(res)
