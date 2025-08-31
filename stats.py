def get_book_words_number(content):
    words = content.split()
    return len(words)

def get_times_appeared(content):
    content = content.lower()
    #content = content.sort()
    dict = {}
    for i in content:
        if i in dict.keys():
            dict[i] += 1
            continue
        dict[i] =1
    return dict           

def sort_on(dict):
    return dict[1]

def dict_sort(content):
    dict = get_times_appeared(content)
    dict = sorted(dict.items(),reverse = True , key = sort_on) 
    return dict