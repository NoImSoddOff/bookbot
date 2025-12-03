import sys
from stats import *

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dist = count_letters(text)
    char_list = sort_dictionary(char_dist)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Letter Count ----------")
    for char_dist in char_list:
        if char_dist["char"].isalpha():
            print(f"{char_dist['char']}: {char_dist['num']}")
    print("============= END ===============")

main()
