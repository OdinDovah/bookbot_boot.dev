from stats import get_word_count
from stats import get_char_count
from stats import sorted_count
import sys

def main():
    if len(sys.argv) < 2:
        print("Missing argument. Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(file_path)} total words")
    print("--------- Character Count -------")
    for count in sorted_count(get_char_count(file_path)):
        print(f"{count["char"]}: {count["num"]}")
    print("============= END ===============")

main()
