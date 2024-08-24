import string

def word_frequency(text: str) -> dict:
    # Remove punctuation and convert text to lowercase
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = text.split()  # Split the text into words
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

print(word_frequency("Hello world! Hello everyone."))  # Output: {'hello': 2, 'world': 1, 'everyone': 1}
print(word_frequency("This is a test. This test is easy."))  # Output: {'this': 2, 'is': 2, 'a': 1, 'test': 2, 'easy': 1}
print(word_frequency("Python is fun. Fun fun fun!"))  # Output: {'python': 1, 'is': 1, 'fun': 4}
print(word_frequency("One word, one word."))  # Output: {'one': 2, 'word': 2}