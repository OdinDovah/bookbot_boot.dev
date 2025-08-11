from stats import *
import sys


def main():
    file_path = sys.argv[1]
    if len(sys.argv) < 2:
        print("missing argument. usage: python3 main.py <path/to/book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(file_path)} total words")
    print("--------- Character Count -------")
    for count in sorted_count(get_char_count(file_path)):
        print(f"{count['char']}: {count['num']}")
    print("============= END ===============")


main()
