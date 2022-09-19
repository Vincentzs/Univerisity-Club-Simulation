""" CSC108 Assignment 3: Club Recommendations - Starter code."""
from typing import List, Tuple, Dict, TextIO


# Sample Data (Used by Doctring examples)

P2F = {'Jesse Katsopolis': ['Danny R Tanner', 'Joey Gladstone',
                            'Rebecca Donaldson-Katsopolis'],
       'Rebecca Donaldson-Katsopolis': ['Kimmy Gibbler'],
       'Stephanie J Tanner': ['Michelle Tanner', 'Kimmy Gibbler'],
       'Danny R Tanner': ['Jesse Katsopolis', 'DJ Tanner-Fuller',
                          'Joey Gladstone']}

P2C = {'Michelle Tanner': ['Comet Club'],
       'Danny R Tanner': ['Parent Council'],
       'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
       'Jesse Katsopolis': ['Parent Council', 'Rock N Rollers'],
       'Joey Gladstone': ['Comics R Us', 'Parent Council']}


# Helper functions 

def update_dict(key: str, value: str,
                key_to_values: Dict[str, List[str]]) -> None:
    """Update key_to_values with key/value. If key is in key_to_values,
    and value is not already in the list associated with key,
    append value to the list. Otherwise, add the pair key/[value] to
    key_to_values.

    >>> d = {'1': ['a', 'b']}
    >>> update_dict('2', 'c', d)
    >>> d == {'1': ['a', 'b'], '2': ['c']}
    True
    
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    """
    if key not in key_to_values:
        key_to_values[key] = []
        
    if value not in key_to_values[key]:
        key_to_values[key].append(value)


def remove_empty(dictionary: Dict[str, List[str]]) -> None:
    """removes the key if the corresponding value is empty from the dictionary
    
    >>> dict = {'a': [], 'b': [' ']}
    >>> remove_empty(dict)
    >>> dict
    {'b': [' ']}
    
    >>> food_to_type= {
    ...    'fruit': ['appple', 'banana'],
    ...    'meat': ['beef'],
    ...    'plastic': []}
    >>> remove_empty(food_to_type)
    >>> food_to_type
    {'fruit': ['appple', 'banana'], 'meat': ['beef']}
    """ 
    removed_empty = []
    for key in dictionary:
        if dictionary[key] == []:
            removed_empty.append(key)
    for key in removed_empty:
        dictionary.pop(key)
    

def sort(dictionary: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Sorts the list of strings in alphabetical order
    
    >>> fruits = {
    ...    'banana': ['yellow' ,'soft'],
    ...    'strawberry': ['red', 'juicy']}
    >>> sort(fruits)
    {'banana': ['soft', 'yellow'], 'strawberry': ['juicy', 'red']}
    
    >>> course = {
    ...    'Math': ['Linear Algebra', 'Calculus'],
    ...    'Language': ['Spanish', 'Chinese']}
    >>> sort(course)
    {'Math': ['Calculus', 'Linear Algebra'], 'Language': ['Chinese', 'Spanish']}
    """
    for key in dictionary:
        dictionary[key].sort()
    return dictionary


def reverse_name(name: str) -> List[str]:
    """Return a name without ',' and with the format 'firstname lastname'
    
    >>> reverse_name('Zhu, Vincent')
    'Vincent Zhu'
    
    >>> reverse_name('Zhu, Vincent Van')
    'Vincent Van Zhu'
    """
    name = name.split(',')
    person = name[1] + ' ' + name[0]
    return person.strip()


def make_unique_list(dictionary: Dict[str, List[str]], mode: int) -> List[str]:
    """Returns a unique list of all elements in dictionary. Excludes any 
       repetition. If mode is 0, include keys. If mode is not 0, exclude keys.
       
    >>> person_to_friends = {
    ...    'Vincent Zhu': ['Linh Zhu', 'Jack Chen'], 
    ...    'Jack Chen': ['Linh Lang']}
    >>> make_unique_list(person_to_friends, 0)
    ['Vincent Zhu', 'Linh Zhu', 'Jack Chen', 'Linh Lang']
    
    >>> person_to_clubs = {
    ...    'Vincent Zhu': ['Swim club'], 
    ...    'Jack Chen': ['Kendo club', 'Swim club']}
    >>> make_unique_list(person_to_clubs, 1)
    ['Swim club', 'Kendo club']
    """
    unique_list = []
    if mode == 0:
        for key in dictionary:
            if key not in unique_list:
                unique_list.append(key)
            for value in dictionary[key]:
                if value not in unique_list:
                    unique_list.append(value)
    else:
        for key in dictionary:
            for value in dictionary[key]:
                if value not in unique_list:
                    unique_list.append(value)            
    return unique_list


def tuple_maker(potential_clubs: List[str]) -> List[Tuple[str, int]]:
    """Returns a dictionary of tuples. Each tuple consist of every distinct
    string and number of time that string occurs. If all multiple string occurs 
    same number of times then those tuples are sorted based on the alphabatical 
    order of strings.

    >>> tuple_maker(['a', 'b', 'b'])
    [('b', 2), ('a', 1)]

    >>> tuple_maker(['a', 'b', 'b', 'd', 'c'])
    [('b', 2), ('a', 1), ('c', 1), ('d', 1)]
    """

    output = []
    potential_clubs.sort()
    for item in potential_clubs:
        if (item, potential_clubs.count(item)) not in output:
            output.append((item, potential_clubs.count(item)))
    for i in range(len(output) - 1):
        if output[i][1] < output[i + 1][1]:
            temp = output[i]
            output[i] = output[i + 1]
            output[i + 1] = temp

    return output


# Required function
def load_profiles(profiles_file: TextIO) -> Tuple[Dict[str, List[str]],
                                                  Dict[str, List[str]]]:
    """Return a two-item tuple containing a "person to friends" dictionary
    and a "person_to_clubs" dictionary with the data from profiles_file.

    NOTE: Functions (including helper functions) that have a parameter of type
          TextIO do not need docstring examples.
    """
    empty_line = None
    person_to_friends = {}
    person_to_clubs = {}
    profiles = profiles_file.readlines()
    for line in profiles:
        line = line.strip()
        if line == '':
            empty_line = None
        elif empty_line is None:
            line = reverse_name(line)
            person_to_friends[line] = []
            person_to_clubs[line] = []
            empty_line = line
        else:
            if ',' in line:
                line = reverse_name(line)
                person_to_friends[empty_line].append(line)
            else:
                person_to_clubs[empty_line].append(line)
    remove_empty(person_to_friends)
    remove_empty(person_to_clubs)
    return (sort(person_to_friends), sort(person_to_clubs))


def get_average_club_count(person_to_clubs: Dict[str, List[str]]) -> float:
    """Return the average number of clubs that a person in person_to_clubs
    belongs to.

    >>> get_average_club_count(P2C)
    1.6
    
    >>> person_to_clubs = {}
    >>> get_average_club_count(person_to_clubs)
    0.0
    """
    total_clubs = 0
    num_people = len(person_to_clubs)
    if num_people != 0:
        for person in person_to_clubs:
            total_clubs += len(person_to_clubs[person])
        return total_clubs / num_people
    return 0.0


def get_last_to_first(person_to_friends: Dict[str, List[str]]) \
    -> Dict[str, List[str]]:
    """Return a "last name to first name(s)" dictionary with the people from the
    "person to friends" dictionary person_to_friends.

    >>> get_last_to_first(P2F) == {
    ...    'Katsopolis': ['Jesse'],
    ...    'Tanner': ['Danny R', 'Michelle', 'Stephanie J'],
    ...    'Gladstone': ['Joey'],
    ...    'Donaldson-Katsopolis': ['Rebecca'],
    ...    'Gibbler': ['Kimmy'],
    ...    'Tanner-Fuller': ['DJ']}
    True
    
    >>> person_to_friends = {
    ...    'Vincent Zhu': ['Linh Zhu', 'Jack Chen'], 
    ...    'Jack Chen': ['Linh Lang']}
    >>> get_last_to_first(person_to_friends) == {
    ...    'Zhu': ['Linh', 'Vincent'],
    ...    'Chen': ['Jack'],
    ...    'Lang': ['Linh']}
    True
    """
    last_to_first = {}
    name = make_unique_list(person_to_friends, 0)
    for person in name:
        first_name = person[:person.rfind(" ")]
        last_name = person[person.rfind(" ") + 1:]
        update_dict(last_name, first_name, last_to_first)
    return sort(last_to_first)
    

def invert_and_sort(key_to_value: Dict[object, object]) -> Dict[object, list]:
    """Return key_to_value inverted so that each key is a value (for
    non-list values) or an item from an iterable value, and each value
    is a list of the corresponding keys from key_to_value.  The value
    lists in the returned dict are sorted.

    >>> invert_and_sort(P2C) == {
    ...  'Comet Club': ['Michelle Tanner'],
    ...  'Parent Council': ['Danny R Tanner', 'Jesse Katsopolis',
    ...                     'Joey Gladstone'],
    ...  'Rock N Rollers': ['Jesse Katsopolis', 'Kimmy Gibbler'],
    ...  'Comics R Us': ['Joey Gladstone'],
    ...  'Smash Club': ['Kimmy Gibbler']}
    True
    
    >>> key_to_value = {"Vincent": ["Zhu"]}
    >>> invert_and_sort(key_to_value) == {"Zhu": ["Vincent"]}
    True
    """
    invert = {}
    for key in key_to_value:
        values = key_to_value[key]
        for value in values:
            update_dict(value, key, invert)
    return sort(invert)


def get_clubs_of_friends(person_to_friends: Dict[str, List[str]],
                         person_to_clubs: Dict[str, List[str]], 
                         person: str) -> List[str]:
    """Return a list, sorted in alphabetical order, of the clubs in
    person_to_clubs that person's friends from person_to_friends
    belong to, excluding the clubs that person belongs to.  Each club
    appears in the returned list once per each of the person's friends
    who belong to it.

    >>> get_clubs_of_friends(P2F, P2C, 'Danny R Tanner')
    ['Comics R Us', 'Rock N Rollers']
    
    >>> person_to_friends = {}
    >>> person_to_clubs = {
    ...  'Vincent Zhu': ['Swim club'],
    ...  'Jack Chen': ['Kendo club', 'Swim club'],
    ...  'Linh Lang': ['Kendo club', 'Swim club'],
    ...  'Linh Zhu': ['Kendo club']}
    >>> get_clubs_of_friends(person_to_friends, person_to_clubs, 'Vincent Zhu')
    []
    """
    clubs = []
    club_to_persons = invert_and_sort(person_to_clubs)
    if person not in person_to_friends:
        return clubs
    for friend in person_to_friends[person]:
        for club in club_to_persons:
            if person not in club_to_persons[club] and friend in \
               club_to_persons[club]:
                clubs.append(club)
    clubs.sort()
    return clubs


def recommend_clubs(
        person_to_friends: Dict[str, List[str]],
        person_to_clubs: Dict[str, List[str]],
        person: str,) -> List[Tuple[str, int]]:
    """Return a list of club recommendations for person based on the
    "person to friends" dictionary person_to_friends and the "person
    to clubs" dictionary person_to_clubs using the specified
    recommendation system.

    >>> recommend_clubs(P2F, P2C, 'Stephanie J Tanner',)
    [('Comet Club', 1), ('Rock N Rollers', 1), ('Smash Club', 1)]
    
    >>> recommend_clubs(P2F, P2C, 'Jesse Katsopolis',)
    [('Comics R Us', 2), ('Smash Club', 1)]
    """
    club_members = make_unique_list(person_to_clubs, 1)
    club_to_persons = invert_and_sort(person_to_clubs)
    potential_clubs = get_clubs_of_friends(person_to_friends, 
                                           person_to_clubs, person)
    for member in club_members:
        members_clubs = person_to_clubs[member]
        for club in members_clubs:
            if person not in club_to_people[club]:
                potential_clubs.append(club)
    return freq_to_list(club_points)


if __name__ == '__main__':
    pass

    # If you add any function calls for testing, put them here.
    # Make sure they are indented, so they are within the if statement body.
    # That includes all calls on print, open, and doctest.

    #import doctest
    #doctest.testmod()
