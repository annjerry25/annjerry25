# Step 1: Define the Dictionary
word_dictionary = {}

# Step 2: Add Words and Definitions
word_dictionary["python"] = "A high-level, interpreted programming language."
word_dictionary["variable"] = "A named storage location that can hold data."
word_dictionary["function"] = "A reusable block of code that performs a specific task."

# Step 3: Accessing Definitions
print("Definition of 'python':", word_dictionary["python"])

# Step 4: Updating Definitions
word_dictionary["python"] = "A powerful, high-level, interpreted programming language."

# Step 5: Deleting Words
del word_dictionary["variable"]

# Step 6: Iterating Through the Dictionary
for word, definition in word_dictionary.items():
    print(f"{word}: {definition}")

