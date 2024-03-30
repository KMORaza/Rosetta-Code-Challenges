# Longest common subsequence
def lcs_case_sensitive(str1, str2):
    def lcs_helper(s1, s2, m, n):
        if m == 0 or n == 0:
            return ''
        elif s1[m - 1] == s2[n - 1]:
            return lcs_helper(s1, s2, m - 1, n - 1) + s1[m - 1]
        else:
            lcs1 = lcs_helper(s1, s2, m, n - 1)
            lcs2 = lcs_helper(s1, s2, m - 1, n)
            return lcs1 if len(lcs1) > len(lcs2) else lcs2
    return lcs_helper(str1, str2, len(str1), len(str2))
str1 = "ABCD"
str2 = "BD"
print("Longest Common Subsequence:", lcs_case_sensitive(str1, str2))