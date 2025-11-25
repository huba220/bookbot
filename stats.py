def get_num_words(text) :
   return len(text.split())



def number_of_characters(text) :
    lower_text = text.lower()
    char_counts = {}

    for char in lower_text :
        if char in char_counts :
            char_counts[char] = char_counts[char] + 1 
        else : 
            char_counts[char] = 1 

    return char_counts



def convert_to_list(char_counts):
    result = []
    for key in char_counts:
        value = char_counts[key]
        lista = {"char": key, "num": value}
        result.append(lista)
     
    result.sort(reverse=True, key=sort_on)
    return result
    

def sort_on(items) :
    return items["num"]





        
