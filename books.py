from stats import count_words
from stats import character_frequency
from stats import sorted_list
from stats import print_result

def get_book_text(path):
   with open(path, encoding = "utf-8") as f:
    return f.read()

def main():
    print("========BOOKBOT========")
    book_path = "books/frankestein.txt"
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

