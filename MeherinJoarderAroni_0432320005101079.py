
full_name = input("Enter your full name: ")
vowels = 0
consonants = 0
for char in full_name:
    if char.isalpha():
        if char.lower() in 'aeiou':
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)


ascii_values = []
for char in full_name:
    ascii_values.append(ord(char))
print("ASCII Values:", ascii_values)


reversed_name = full_name[::-1]
print("Reversed Name:", reversed_name)


cleaned_name = full_name.replace(" ", "").lower()
if cleaned_name == cleaned_name[::-1]:
    print("Is Palindrome: True")
else:
    print("Is Palindrome: False")


unique_letters = []
for char in full_name:
    if char.isalpha() and char not in unique_letters:
        unique_letters.append(char)
unique_letters.sort()
print("Unique Letters (sorted):", unique_letters)


found = False
for char in full_name:
    if full_name.count(char) == 1 and char != " ":
        print("First Non-Repeating Character:", char)
        found = True
        break
if not found:
    print("First Non-Repeating Character: None")
