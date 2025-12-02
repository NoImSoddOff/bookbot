from stats import *

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(book_path)
#    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")


main()

