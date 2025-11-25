from stats import get_num_words
from stats import number_of_characters
from stats import convert_to_list
import sys 




def get_book_text(path_to_file) :
    with open(path_to_file) as f :   
        return f.read()
    







def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    num_char = number_of_characters(text)
    sorted_list = convert_to_list(num_char)
    message = f"Found {word_count} total words"
    analize = f"Analyzing book found at {book_path}..."
    print ("============ BOOKBOT ============")
    print (analize)
    print ("----------- Word Count ----------")
    print (message)
    print ("--------- Character Count -------")
    for item in sorted_list:
        char = item["char"]
        count = item["num"]
        if char.isalpha():
            print (f"{char}: {count}")
    print ("============= END ===============")
    

main()



















