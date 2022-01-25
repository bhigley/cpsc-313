import logging

logging.basicConfig(filename='count_words.log', level= logging.INFO)

def find_words(file_name):
    words_list = []

    with open(file_name,'r') as file:
        for line in file:
            for word in line.split():
                item = [word, 1]
                words_list.append(item)

    return words_list

def main():
    print(find_words('test.txt'))

if __name__ == '__main__':
    main()
