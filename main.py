
def main():
    counter = 0
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        for words in file_contents.split():
            counter += 1 
    print(f"{counter} words in the file")
    print(count_characters(file_contents))


def count_characters(book):
    book = book.lower()
    count_dictionary = {}
    for char in book:
        if char in count_dictionary:
            count_dictionary[char] = count_dictionary[char] + 1
        else:
            count_dictionary[char] = 1
    return(count_dictionary)
main()
