s = input("Please type in a string: ")
vowels = ['a', 'e', 'o']

for vowel in vowels:
    if vowel in s:
        print(vowel, "found")
    else:
        print(vowel, "not found")
