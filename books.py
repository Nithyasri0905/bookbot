from stats import count_words
from stats import character_frequency
from stats import sorted_list
from stats import print_result

def get_book_text(path):
   with open(path, encoding = "utf-8") as f:
    return f.read()

import sys 
def main():
    print("========BOOKBOT========")
    
    length = len(sys.argv)
    if length != 2:
        print("Usage: python3 books.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print(f"book path: {book_path}")
    text = get_book_text(book_path)
    print(f"Analyzing book found at {book_path}....")
   

    
    print("--------Word Count---------")
    word_count = count_words(text)
    print(f"Found {word_count} total words")

    print("---------Character Count----------")
    character_count = character_frequency(text)
    

    result = sorted_list(character_count)
    
    print_result(result)
    


main()

