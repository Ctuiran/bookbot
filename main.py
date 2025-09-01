from stats import count_words, count_letters, sorted_dict
import sys

def get_book_text(path_to_file):
    with open(str(path_to_file)) as f:
        file_contents = f.read()
    
    return file_contents

if __name__ == "__main__":
    #path="./books/frankenstein.txt"
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_text=get_book_text(sys.argv[1])
    words_in_book=count_words(book_text)
    dict_let=count_letters(book_text)
    dict_sort=sorted_dict(dict_let)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words_in_book} total words")
    print("--------- Character Count -------")
    for letter in dict_sort:
        if letter["char"].isalpha():
            print(letter["char"]+": "+str(letter["num"]))
    print("============= END ===============")
