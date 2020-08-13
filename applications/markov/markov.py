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


# TODO: construct 5 random sentences
# Your code here
def sentence(start, length):
    words = ht[start]
    result = start
    for i in range(0, length):
        word_new = random.choice(words)
        result += f" {word_new}"
        words = ht[word_new]
    return result

print(sentence("The", 10))
print(sentence("\"Do", 10))
# print(sentence("\"Oh,", 10))
# print(sentence("\"Do", 10))
