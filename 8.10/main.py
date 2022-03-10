# Nam Doan
# PSID: 1847037

def aPalindrome(string):
    string = string.replace(" ", "")
    return string == string[::-1]


palinword = str(input())
testPalindrome = aPalindrome(palinword)


if testPalindrome:
    print(palinword, "is a palindrome")
else:
    print(palinword, "is not a palindrome")
