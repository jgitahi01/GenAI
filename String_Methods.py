text = " hello, python world! "
#using strip to remove extra spaces 
stripped_text = text.strip()
print("Stripped text:",stripped_text)
#capitalize() to capitalize the first letter 
capitalized_text = stripped_text.capitalize()
print("Capitalized text:",capitalized_text)
#replace() the "world" with "universe"
replaced_text = capitalized_text.replace("world","universe")
print("Replaced text:",replaced_text)
#upper() to convert to uppercase
uppercase_text = replaced_text.upper()
print("Uppercase text:",uppercase_text)

