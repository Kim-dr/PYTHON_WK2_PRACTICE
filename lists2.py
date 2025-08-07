# Task 5: List of words with odd character lengths
words = ["apple", "banana", "kiwi", "grapes", "mango", "fig", "orange"]
odd_words = [word for word in words if len(word) % 2 != 0]

print("Words with an odd number of characters:", odd_words)
