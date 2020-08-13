import random

# Read in all the words in one go
with open("input.txt") as f:
    words_raw = f.read()

# TODO: analyze which words can follow other words
# Your code here
words = words_raw.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').split(" ")
ht = {}

for index, word in enumerate(words):
    if index + 1 < len(words):
        if len(word) > 0 and len(words[index + 1]) > 0:
            next = words[index + 1]
            if word not in ht:
                ht[word] = []
            ht[word].append(next)

def random_word():
    return random.choice(list(ht))

def random_start_word():
    word = random_word()
    while not word[0].isupper() and not (len(word) >= 2 and (word[0] == "\"" or word[1].isupper())):
        word = random_word()
    return word

# TODO: construct 5 random sentences
# Your code here
def sentence(result = "", current_word = "", stop_chars = [".", "!", "?", "\""]):
    if result == "":
        start = random_start_word()
        result = start
        current_word = start

    elif current_word[-1] in stop_chars:
        return result

    words = ht[current_word]
    word_new = random.choice(words)
    result = f"{result} {word_new}"
    current_word = word_new

    return sentence(result, current_word)

print(sentence())
print(sentence())
print(sentence())
print(sentence())
