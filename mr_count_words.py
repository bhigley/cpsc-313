import logging
import multiprocessing
#import string
import operator
import glob
import time

from basicMR import SimpleMapReduce


logging.basicConfig(filename='count_words.log', level= logging.INFO)

def find_words(file_name):
    STOP_WORDS = set([
            'a', 'an', 'and', 'are', 'as', 'be', 'by', 'for', 'if', 'in', 
            'is', 'it', 'of', 'or', 'py', 'rst', 'that', 'the', 'to', 'with',
            ])

    print(multiprocessing.current_process().name, 'reading', file_name)
    output = []

    with open(file_name, 'rt') as f:
        for line in f:
            if line.lstrip().startswith('..'): # Skip rst comment lines
                continue
            for word in line.split():
                word = word.lower()
                if word.isalpha() and word not in STOP_WORDS:
                    output.append( (word, 1) )
    return output

def count_words(item):
    logging.info('Starting count words function')
    start_time = time.perf_counter()

    word, occurances = item
    return (word, sum(occurances))

def main():
    
    logging.basicConfig(filename='count_words.log', level=logging.DEBUG)
    logging.info('Starting count words main program')

   # input_files = glob.glob('/Users/benhigley/Desktop/CPSC_313/test.txt')
    input_files = glob.glob('*.txt', recursive=True)
    
    mapper = SimpleMapReduce(find_words, count_words)
    word_counts = mapper(input_files)
    print(word_counts)
    word_counts.sort(key=operator.itemgetter(1))
    word_counts.reverse()

# delete later
def create_file(source_words, filename, max_file_size):
    with open(filename, 'w') as current_file:
        word_counts = {}
        cur_file_size = 0
        while cur_file_size < max_file_size:
            source_words_size = len(source_words)
            random_index = randint(0, source_words_size - 1)
            random_word = source_words[random_index]
            current_file.write(random_word + ' ')
            cur_file_size += len(random_word) + 1
            word_counts[random_word] = word_counts.get(random_word, 0) + 1

def create_source_words(count_words):
    # Call a simple dictionary service (found by searching) to get the random word list
    resp = requests.get(f"https://random-word-api.herokuapp.com/word?number={count_words}")
    return list(resp.json())

if __name__ == '__main__':
    main()