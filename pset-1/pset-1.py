#  Create a loop that iterates through a string and prints the longest substring.
#  If two strings tie, print the last one that would appear if ranked in alphabetical order.

# GLOBAL VARIABLES
s = "zyxwasdgafbkjlbthlabcdefghijk"

longest_substring = ''

#  Logic
for letter in range(len(s)):
    n = 1
    
    while (letter + n < len(s)) and (s[letter + n - 1] <= s[letter + n]):
        n += 1

    if len(s[letter:letter + n]) >= len(longest_substring):
        longest_substring = s[letter : letter + n]
        

print(longest_substring)