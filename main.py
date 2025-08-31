from stats import get_book_words_number,get_times_appeared , dict_sort
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    

#/home/ahmed/firstproject/bookbot/books
    
def main():
    path = sys.argv[-1]
    file_content = get_book_text(path)
    print(f"{get_book_words_number(file_content)} words found in the book")
    print(f"the character count ")
    dict = dict_sort(file_content)
    for i in dict :
        print(i)
    print("#####################END####################")
    return

main()
    