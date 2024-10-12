try:
    file = open('ex149.txt')
    for i in range(10):
        print(file.readline())
    file.close()

except FileNotFoundError:
    print(f'are you sure that the file exists?')
