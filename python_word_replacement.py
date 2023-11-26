original_sentence = input("Enter a sentence: ")
def replace_word(sentence, old_word, new_word):
    return sentence.replace(old_word, new_word)
word_to_replace = input("Enter the word to replace: ")
replacement_word = input("Enter the replacement word: ")
modified_sentence = replace_word(original_sentence, word_to_replace, replacement_word)
print("Original Sentence:", original_sentence)
print("Modified Sentence:", modified_sentence)


