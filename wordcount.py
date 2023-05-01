"""Count words in file."""

def load_data(filename):

    result = []
    csv_file = open(filename)
    for row in csv_file:
        data = row.rstrip().split()
        # result = result + data # create a new copy
        result.extend(data) # mutate the original list
    csv_file.close()

    return result

words_list_test = load_data('test.txt')
words_list_twain = load_data('twain.txt')

def count_words(words_list):
    word_count = {}
    for word in words_list_test:

        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] = word_count[word] + 1

    for key in word_count:
        # print(key + " " + str(word_count[key]))
        print(f"{key} {word_count[key]}")

print(count_words(words_list_test))