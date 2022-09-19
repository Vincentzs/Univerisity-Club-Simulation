from typing import List, Tuple, Dict, TextIO

def insert_tup(word: str,  dictionary: Dict[str, int]) -> None:
    
    if len(dictionary) == 0:
        list_of_str.append(word)
    else:
        for i in range(len(dictionary)):
            if len(word) < len(dictionary[i]) and word < dictionary[i]:
                dictionary.insert(i, word)
            elif len(word) == len(dictionary[i]) and word < dictionary[i]:
                
    
"""if (len(word) < len(list_of_str)) 
        (len(word) == len(list_of_str))
                (word < list_of_str):
"""
def freq_to_list(dictionary: Dict[str, int]) -> List[Tuple[str, int]]:
    freq_list = []
    for key in dictionary:
        insert_tup((key, dictionary[key]), dictionary)
    return freq_list
        
#({}, {'Eagle Diao': ['Shit Club']})