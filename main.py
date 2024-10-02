
def main():
    counter = 0
    file = "books/frankenstein.txt"
    with open(file) as f:
        file_contents = f.read()
        for words in file_contents.split():
            counter += 1 
    print(f"--- Begin report of {file} ---")
    print(f"{counter} words in the file")
    count_dict = count_characters(file_contents)
    count_dict.sort(reverse=False, value=sort_on)
    for i in count_dict:
        print(f"The '{i}' character was found f{count_dict[i]} times")

def count_characters(book):
    book = book.lower()
    count_dictionary = {}
    for char in book:
        if char in count_dictionary:
            count_dictionary[char] = count_dictionary[char] + 1
        elif char.isalpha() == True:
            count_dictionary[char] = 1
    return(count_dictionary)
main()
