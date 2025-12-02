def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def get_num_words(file_path):
    with open(file_path) as g:
        words = g.read()
        return len(words.split())

def get_num_characters(file_path)
    with open(file_path) as h:
        letters = h.read()
        dictionary = {}
        for letter in letters:
            for char in list(word):
                if char.lower() not in dictionary:
                    dictionary[char.lower()] = 1
                else:
                    dictionaryf[char.lower()] += 1
        return dictionary


def sort_on(dist):
    return dist["num"]


def sort_dictionary(dictionary):
    sorted_list = []
    for char, count in disctionary.items():
        sorted_list.append({'char': char})
#, 'num': count})
#    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
