from fileinput import filename
import logging
import multiprocessing
import string
import operator
import glob
import time

from basicMR import SimpleMapReduce


logging.basicConfig(filename='count_words.log', level= logging.INFO)

def find_words(file_name):
    logging.info("Starting find_words function")
    start_time = time.perf_counter()
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
                else:
                    logging.info('(' + word + ')' + " is a stop word or not alphabetical")
    end_time = time.perf_counter()
    logging.info("Time to create uncounted list: " + str(end_time - start_time))
    logging.info("List of uncounted words: " + str(output))
    return output

def count_words(item):
    logging.info('Starting count words function')

    start_time = time.perf_counter()
    word, occurances = item
    end_time = time.perf_counter()

    logging.info(word + ' count completed, time: ' + str(end_time - start_time))

    return (word, sum(occurances))

def main():
    logging.basicConfig(filename='count_words.log', level=logging.DEBUG)
    logging.info('Starting count words main program')
    start_time = time.perf_counter()

    input_files = glob.glob('*.txt', recursive=True)
    mapper = SimpleMapReduce(find_words, count_words)
    word_counts = mapper(input_files) # calls __call__
    print(word_counts)
    logging.info("Final word counts: " + str(word_counts))
    #word_counts.sort(key=operator.itemgetter(1))
    #word_counts.reverse()

    end_time = time.perf_counter()
    logging.info("Total map reduce time: " + str(end_time - start_time))

if __name__ == '__main__':
    main()