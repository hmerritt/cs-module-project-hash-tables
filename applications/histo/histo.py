import re
import operator

# Read in all the words in one go
with open("robin.txt") as f:
    words_raw = f.read()

def word_count():
    # Your code here
    output = {}

    words = words_raw.lower().replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').split(" ")

    for w in words:
        word = w
        word = re.sub('[\"\:\;\,\.\-\+\=\/\\\|\[\]\{\}\(\)\*\^\&]', '', word)
        if len(word) > 0:
            if word not in output:
                output[word] = 1
            else:
                output[word] += 1

    return output

output = ""
words_count = word_count()

if len(words_count) > 0:
    sort = sorted(words_count.items(), key=operator.itemgetter(1))
    sort.reverse()
    max = max(len(x) for x in words_count)

    for word in sort:
        spaces = " " * (max + 4 - len(word[0]))
        hashes = "#" * word[1]
        print(f"{word[0]} {spaces} {hashes}")
