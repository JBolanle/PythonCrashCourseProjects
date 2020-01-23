hammock = 'text_files/hammock.txt'
christmas = 'text_files/christmas.txt'

def word_count(filename, word):
    """Analyzes file and checks how many times a word, 'word', comes up in the file"""
    with open(filename) as f_obj:
       book = f_obj.read()
       print("The word, '" + word.title() + "' appears " + str(book.count(word)) + " times in " + filename + ".")

word_count(hammock, 'the')
word_count(christmas, 'the')