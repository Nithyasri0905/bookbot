#count total how many words are present in the whole book 
def count_words(text):
    num_words = text.split()
    length = len(num_words)
    return length

#count how many times each letter appears in a dictionary form (letter:frequency) 
def character_frequency(text):
    freq = {}
    text = text.lower()

    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq

def sorted_list(char_frequency):
    char_list = []

    for char,count in char_frequency.items():

        char_list.append({"char": char, "num": count })

    char_list.sort(reverse = True, key = sort_on)
    return char_list

def sort_on(items):
    return items["num"]

def print_result(result):
    for item in result:
       if item['char'].isalpha():
        print(f"{item['char']} : {item['num']}")
    
        







    




