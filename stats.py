#Open and return the file contents 
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


#Open and return the number of works in file
def get_num_words(text):
    words = text.split()
    return len(words)

#Convert files characters to lower case. Add character to dictionary and count each instance 
def count_letters(text):
    word_list = text.split()
    dictionary = {}
    for words in word_list:
        for char in list(words):
            if char.lower() not in dictionary:
                dictionary[char.lower()] = 1
            else:
                dictionary[char.lower()] += 1
    return dictionary


def sort_chars(sorted):
    return sorted["num"]


#Sort the dictionary output
def sort_dictionary(dictionary):
    sorted_list = []
    for char, count in dictionary.items():
        sorted_list.append({'char': char, 'num': count})
    sorted_list.sort(reverse=True, key=sort_chars)
    return sorted_list
