text =input("Enter a word you think is a palindrome: ")
#remove spaces and convert to lowercase for case insensitivity 
cleaned_text = text.replace(" ","").lower()
#reverse the cleaned text
reversed_text = cleaned_text[::-1]
#check if the cleaned text is equal to its reverse
if cleaned_text == reversed_text:
    print("Yes,",text,"is a palindrome!")
else:
    print("No,",text,"is not a palindrome.")