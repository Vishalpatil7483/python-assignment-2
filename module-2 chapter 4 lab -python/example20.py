#Example 20. Count Words in a Sentence
print("Name: Rakshitha P \nReg no: 23BTIT145")
sentence = "hello world hello"
words = sentence.split()
word_count = {word: words.count(word) for word in set(words)}
print(word_count)