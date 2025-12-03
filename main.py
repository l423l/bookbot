import sys
from stats import get_num_words, get_chars_dict, get_counted

def main():
    if len(sys.argv) != 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)

    book_path = sys.argv[1]

    with open(book_path) as book_file:
        text = book_file.read()

    num_words = get_num_words(text)
    chars = get_chars_dict(text)
    sorted_chars = get_counted(chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        char = item["char"]
        count = item["num"]

        if not char.isalpha():
            continue

        print(f"{char}: {count}")

    print("============= END ===============")

main()
