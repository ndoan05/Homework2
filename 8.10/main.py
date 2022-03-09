# Nam Doan
# PSID: 1847037

def isPalindrome(string):
    string = string.replace(" ","")
    return string == string[::-1]


palintest = str(input())
test = isPalindrome(palintest)


if test:
    print(palintest, "is a palindrome")
else:
    print(palintest, "is not a palindrome")
