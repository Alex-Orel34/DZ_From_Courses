def Ispalindrome(st):
    if st == st[::-1]:
        return True
    return False


ls=['abacaba','mama','papa']
for word in ls:
  if Ispalindrome(word):
    print(word)