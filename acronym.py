a, user_input = "", input("Enter a phrase: ")
phrase = (user_input.replace("of", "")).split()
for word in phrase:
    a += word[0].upper()
print(f'Acronym of {user_input} is {a}')