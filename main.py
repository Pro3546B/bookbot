import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
from stats import sort_character_frequency
from stats import character_frequency
from stats import wordcount
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    # Word count
    print("----------- Word Count ----------")
    word = wordcount(text)
    print(f"Found {word} total words")

    # Character frequency
    print("--------- Character Count -------")
    characters = character_frequency(text)

    # Sort the characters
    sorted_characters = sort_character_frequency(characters)

    # Print sorted character frequency report
    for item in sorted_characters:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")

    # Print the end
    print("============= END ===============")
main()

