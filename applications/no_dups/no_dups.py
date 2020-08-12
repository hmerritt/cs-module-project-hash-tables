def no_dups(s):
    # Your code here
    output = ""
    cache = {}
    split = s.split(" ")

    for word in split:
        if len(word) > 0:
            if word not in cache:
                output = f"{output} {word}"
                cache[word] = 1
            else:
                cache[word] += 1

    if len(output) > 0:
        if output[0] == " ":
            output = output[1:]
        if output[-1] == " ":
            output = output[:-1]

    return output



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
