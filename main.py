from stats import word_count, letter_count, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    book = sys.argv[1]
    print(f'Analyzing book found at {book}')
    text = get_book_text(book)
    num_words = word_count(text)
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    letter_dict = letter_count(text)
    letter_dict_sorted = sort_dict(letter_dict)
    print("--------- Character Count -------")
    for entry in letter_dict_sorted:
        if entry.isalpha():
            print(f'{entry}: {letter_dict_sorted[entry]}')
    print("============= END ===============")

main()