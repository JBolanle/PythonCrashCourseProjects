def count_words(filename):
    """Count approx. number of words in the file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()

    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file '" + filename + "' has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'bomb.txt', 'moby_dick.txt']
for filename in filenames:
    count_words(filename)