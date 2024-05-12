def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    num_words = words_in_text(text)
    print(f"{num_words} words found in the document")

    letter_counts = count_letters(text)

    generate_report(num_words, letter_counts)

    
def words_in_text(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_letters(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts

def generate_report(num_words, letter_counts):
    print("--- Frankenstein.txt report ---")
    print("-------------------------------")

    sorted_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

    for letter, count in sorted_counts:
        print(f"The '{letter}' character was found {count} times")

    print("--- End report ---")


main()