
import re

def word_count(s):
    # Your code here
    output = {}

    words = s.lower().replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').split(" ")

    for w in words:
        word = w
        word = re.sub('[\"\:\;\,\.\-\+\=\/\\\|\[\]\{\}\(\)\*\^\&]', '', word)
        if len(word) > 0:
            if word not in output:
                output[word] = 1
            else:
                output[word] += 1

    return output


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
