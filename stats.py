def count_words(text):
    list_words=text.split()
    return len(list_words)

def count_letters(text):
    dic_letters={}
    text=text.lower()
    for letter in text:

        if letter in dic_letters:
            dic_letters[letter] += 1
        else:
            dic_letters[letter] = 1

    return dic_letters

def sort_on(items):
    return items["num"]

def sorted_dict(dict_char):
    sort_dict=[]
    for let in dict_char:
        sort_dict.append({"char": let, "num": dict_char[let]})
    
    sort_dict.sort(reverse=True, key=sort_on)

    return sort_dict