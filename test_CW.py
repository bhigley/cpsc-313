from mr_count_words import*

def test_find_words():
    assert find_words('test.txt') == [['word', 1],['dog', 1], 
    ['word', 1], ['hat', 1], ['dog', 1]]

