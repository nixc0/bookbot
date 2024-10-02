
def main():
    counter = 0
    file = "books/frankenstein.txt"
    with open(file) as f:
        file_contents = f.read()
        for words in file_contents.split():
            counter += 1 
    print(f"--- Begin report of {file} ---")
    print(f"{counter} words in the file") 
    print()
    count_dict = count_characters(file_contents)
    list_of_count_dict = []
    for i in count_dict:
        list_of_count_dict.append({"letter":i, "count":count_dict[i]})
    list_of_count_dict.sort(reverse=True, key=sort_on)
    for i in list_of_count_dict:
        print(f"The '{i["letter"]}' character was found {i["count"]} times")
        print(i["count"])


def sort_on(dict):
    return dict["count"]

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
