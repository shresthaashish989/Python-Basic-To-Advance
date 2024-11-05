user_input = input("Enter the characters: ")
first_char = user_input[0].lower()  
if first_char in ('a', 'e', 'i', 'o', 'u'):
     print(f"Your string '{user_input}' is a vowel string")
else:
     print(f"Your string '{user_input}' is a consonant string")





