from mr_count_words import*
import logging



"""
Constants for testing
"""
# FILE NAMES
SMALL_FILE = 'smallFile.txt'
MEDIUM_FILE = 'mediumFile.txt'
LARGE_FILE = 'largeFile.txt'
GIANT_FILE = 'giantFile.txt'
FILE_LIST = [SMALL_FILE, MEDIUM_FILE, LARGE_FILE]

# FILE SIZES
SMALL_FILE_SOURCE = 10
MEDIUM_FILE_SOURCE = 100
LARGE_FILE_SOURCE = 1000
GIANT_FILE_SOURCE = 10000

class BasicTest(unittest.TestCase):
    """
    Basic testing class using unittest library base class
    """    

    def setUp(self):
        """
        Setup testing by creating the log file. Yes the name is funny, but it's intended to be this from the base class implementation
        """    
        logging.basicConfig(filename='count_words_test.log', level=logging.DEBUG)
        logging.info('Starting count words testing')

    def test_word_count(self):
        """
        Testing the word count function.
        First, do the hard-coded simple tests
        Next, create random files of words by calling create_source_words for the corpus, then the create_random_files function to create the test file
            Note: create_random_files returns the counts as a dictionary, so you can easily compare the counts
        Call the count_words to get the word counts, and compare what we got back from creating the file vs reading and counting the file
        We do this same routine for increasingly large files with different source words to try and find errors
    """




def test_find_words():
    assert find_words('test1.txt') == [('word', 1),('dog', 1), 
    ('word', 1), ('hat', 1), ('dog', 1)]

