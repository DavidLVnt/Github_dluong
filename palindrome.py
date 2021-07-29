myString = str(input("Enter your word: "))
reverse = myString[::-1]
print("The reverse word: ", reverse)
if myString == reverse:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")

