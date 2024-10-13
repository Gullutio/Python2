try:
    long_word = 0
    max_len = 0

    with open('ex150.txt', 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word_len = len(word)
                if word_len > max_len:
                    max_len = word_len
                    long_word = word
                elif word_len == max_len:
                    long_word.append(word)
    print(f'Length: {max_len}, Word: {long_word}')

except:
    print('sorry there was an error with your file')