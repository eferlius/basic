import numpy as np

def is_list(inp):
    return(isinstance(inp,list))

def is_npArray(inp):
    return(isinstance(inp,np.ndarray))

def is_listOfList(inp):
    if inp == []:
        return False
    return is_list(inp) and all(isinstance(el, list) for el in inp)

def is_listOfNpArray(inp):
    if inp == []:
        return False
    return is_list(inp) and all(isinstance(el, np.ndarray) for el in inp)

def is_list_containing_lists_or_npArray(inp):
    if inp == []:
        return False
    return is_list(inp) and all(isinstance(el, list) or isinstance(el, np.ndarray) 
                                  for el in inp)

def is_npArray_containing_npArray(inp):
    return is_npArray(inp) and all(isinstance(el, np.ndarray) for el in inp)

def is_emptyList_or_emptyNpArray(inp):
    if is_list(inp) and inp != []:
        return False
    elif is_npArray(inp) and np.any(inp):
        return False
    else:
        return True

def get_length(arrayOrScalar):
    if np.isscalar(arrayOrScalar):
        return 0
    else:
        return len(arrayOrScalar)
    