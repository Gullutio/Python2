try:
    file = open("ex150.txt", "r")
    index = 0
    long_word = ''
    last_len = 0

    for char in file:
        index += 1
        if last_len < len(char):
            long_word = char
            last_len = len(char)

        if last_len == len(char):
             long_word.join(char)

    print(f'Longest words: {long_word}Length: {last_len}')

except:
    print('sorry there was an error with your file')