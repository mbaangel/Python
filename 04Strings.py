""" Operations """

s1 = "Hi"
s2 = "Python"

# String Concatenation
print(s1 + ", " + s2 + "!")

# Repetition
print(s1 * 3)

# Indexation
print(s1[0] + s1[1] + s1[2] + s1[3])

# Longitude
print(len(s2))

# Slicing (portion)
print(s2[2:6])
print(s2[2:])
print(s2[0:2])
print(s2[:2])

# Search
print("a" in s1)
print("i" in s1)

# Replace
print(s1.replace("o", "a"))
print(s2.replace("o", "a"))

# Division
print(s2.split("t"))

# Uppercase, lowercase, capital letters
print(s1.upper())
print(s2.lower())
print("angel morales dev".title())
print("angel morales dev".capitalize())

# Methods to Trim Space a String in Python
print(" angel morales ".strip())

# Search from beginning to end
print(s1.startswith("Hi"))
print(s1.startswith("Py"))
print(s1.endswith("Hi"))
print(s2.endswith("on"))

# Search position
s3 ="angel morales @moredev"

print(s3.find("more"))
print(s3.find("More"))
print(s3.find("M"))
print(s3.lower().find("m"))

# Ocurrence Search
print(s3.lower().count("m"))

# Format 
print("Greet: {}, Language: {}!".format(s1, s2))

# Interpolation
print(f"Greet: {s1}, Language: {s2}!")

# Convert List of Strings and Character
print(list(s3))

# Convert String into list
l1 = [s1, ", ", s2, "!"]
print("".join(l1))

# Numerical Conversion
s4 = "123456"
s4 = int(s4)
print(s4)

s5 = "123456.123"
s5 = float(s5)
print(s5)

# Check If String is Number
print(s1.isalnum())
print(s1.isalpha())
print(s4.isalpha())
print(s4.isnumeric())

"""
 * EXERCISE:
 * Shows examples of all the operations you can perform with character strings
 * in your language. Some of those operations could be (search as many as you can):
 * - Access to specific characters, substrings, length, concatenation, repetition, traversal,
 * case conversion, replacement, division, union, interpolation, verification...
 *
 * EXTRA DIFFICULTY (optional):
 * Create a program that analyzes two different words and performs checks
 * to find out if they are:
 * - Palindromes
 * - Anagrams
 * - Isograms
 """
def check(word1: str, word2: str):

    # Palindrome
    print(f"¿{word1} is a palindrome?: {word1 == word1[::-1]}")
    print(f"¿{word2} is a palindrome?: {word2 == word2[::-1]}")

    # Anagram
    print(f"¿{word1} is an anagram of {word2}?: {sorted(word1) == sorted(word2)}")

    # Isogram
    def isogram(word: str) -> bool:

        word_dict = dict()
        for character in word:
            word_dict[character] = word_dict.get(character, 0) + 1
        
        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break

        return isogram
    
    print(f"¿{word1} is an isogram?: {isogram(word1)}")
    print(f"¿{word2} is an isogram?: {isogram(word2)}")

check("radar", "pythonpythonpythonpython")
