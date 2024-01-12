from . import check

def make_list(inp):
    if not isinstance(inp, list):
        return [inp]
    else:
        return inp

def make_listOfList(inp):
    if not (check.is_listOfList(inp)):
        return [inp]
    else:
        return inp

def make_listOfNpArray(inp):
    if not (check.is_listOfNpArray(inp)):
        return [inp]
    else:
        return inp

def make_listOfList_or_listOfNpArray(inp):
    if not (check.is_listOfList(inp) or check.is_listOfNpArray(inp) or 
            check.is_list_containing_lists_or_npArray(inp)):
        return [inp]
    else:
        return inp
    
def count_exceding_char(ofThisString, wrtToThisString, char):
    return ofThisString.count(char) -  wrtToThisString.count(char)

def remove_duplicates_from_list(myList):
    return list(dict.fromkeys(myList))

def remove_duplicates_from_list_of_list(myListOfList):
    newListOfList = []
    for l in myListOfList:
        if l not in newListOfList:
            newListOfList.append(l)
    return newListOfList

def remove_elements_already_in_list2(list1, list2):
    newList1 = []
    for l in list1:
        if l not in list2:
            newList1.append(l)
    return newList1
    
def merge_lists_OR(listOfLists):
    '''
    Returns a list with all the elements contained in at least one of the lists 
    without repetition
    '''
    listOfLists = make_listOfList(listOfLists)
    list_all = []
    for l in listOfLists:
        for e in l:
            list_all.append(e)
    return remove_duplicates_from_list(list_all)

def merge_lists_AND(listOfLists):
    '''
    Returns a list with only the elements contained in each one of the lists
    '''
    listOfLists = make_listOfList(listOfLists)
    first_list = listOfLists[0].copy()
    for l in listOfLists[1:]:
        for el in first_list.copy():
            if not el in l:
                first_list.remove(el)
    return first_list

def merge_lists_logic(logic, listOfLists):
    if logic == 'AND':
        return merge_lists_AND(listOfLists)
    elif logic == 'OR':
        return merge_lists_OR(listOfLists)
    else:
        raise Exception('logic in merge_lists_condition should be AND or OR, got {}'.format(logic))