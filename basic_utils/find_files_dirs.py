import os
from . import list_operations
import numpy as np

def list_files_in_this_dir(directory):
    '''
    Returns a list containing the complete path to all the files contained in 
    the given directory
    '''
    tmp = os.listdir(directory)
    if tmp is None:
        return []
    tmp = list_operations.make_list(tmp)
    tmp = [os.path.join(directory, item) for item in tmp]
    files = [item for item in tmp if os.path.isfile(item)]
    return files

def count_files_in_this_dir(directory):
    return len(list_files_in_this_dir(directory))

def count_files_in_dirs_inside_this_dir(directory):
    ans = []
    for d in list_dirs_in_this_dir(directory):
        dirName = os.path.split(d)[1]
        n = count_files_in_this_dir(d)
        ans.append([dirName, n])
    return ans

def list_files_in_these_dirs(listDirectories):
    '''
    Returns a list containing the complete path to all the files contained in 
    the given directories
    '''
    files = []
    listDirectories = list_operations.make_list(listDirectories)
    for directory in listDirectories:
        files.extend(list_files_in_this_dir(directory))
    return files

def list_dirs_in_this_dir(directory):
    '''
    Returns a list containing the complete path to all the directories contained 
    in the given directory
    '''
    tmp = os.listdir(directory)
    if tmp is None:
        return []
    tmp = list_operations.make_list(tmp)
    tmp = [os.path.join(directory, item) for item in tmp]
    dirs = [item for item in tmp if os.path.isdir(item)]
    return dirs

def list_dirs_deep_this_dir(directory, maxDepth):
    '''
    Iterates inside the directories of directory until maxDepth is reached and 
    returns a list containing the complete path to all the found directories
    '''
    search_dirs = list_operations.make_list(directory)
    found_dirs = []

    incr = 1
    if maxDepth == -1:
        incr = -1
    counter = -1
    while counter <= maxDepth:
        counter += incr
        new_dirs = []
        for search_dir in search_dirs:
            tmp = list_dirs_in_this_dir(search_dir)
            new_dirs.extend(tmp)
        if new_dirs == []:
            return found_dirs
        found_dirs.extend(new_dirs)
        search_dirs = new_dirs
    return found_dirs

def is_correct_depth(ofThisPath, wrtToThisPath, depth):
    return list_operations.count_exceding_char(ofThisPath, wrtToThisPath, '\\') == depth+1

def is_partial_name_inside(partialName, thisString):
    return partialName in thisString

def get_extension(thisString):
    return os.path.splitext(thisString)[-1]

def is_correct_extension(ext, thisString):
    return thisString.endswith(ext)

def filter_list_partialName(listOfPaths, listPartialName, logic = 'AND'):
    '''
    Given a list of strings, returns a list with all the strings whose name is contains
    - at least one of the string in listPartialName (if filterPartNameLogic == 'OR')
    - all the strings in listPartialName (if filterPartNameLogic == 'AND')
    '''
    assert logic in ['AND', 'OR'], f"logic should be AND or OR, got: {logic}"
    listOfPaths = list_operations.make_list(listOfPaths)
    listPartialName = list_operations.make_list(listPartialName)
    # AND: if at least one condition is NOT satisfied, remove from valid list
    if logic == 'AND': 
        validPaths = listOfPaths.copy()
        for partialName in listPartialName:
            for path in validPaths.copy():
                if partialName not in path:
                    validPaths.remove(path)
    # OR: if at least one condition is satisfied, add to valid list
    elif logic == 'OR': 
        validPaths = []
        for partialName in listPartialName:
            for path in listOfPaths:
                if partialName in path:
                    validPaths.append(path)
    return validPaths

def filter_list_extension(listOfPaths, listExtension):
    ''' 
    Returns a list with all the files whose extension is one of the value in listExtension
    '''    
    listOfPaths = list_operations.make_list(listOfPaths)
    listExtension = list_operations.make_list(listExtension)
    
    # only works in OR condition: impossible for one file to have two extensions at the same time    
    validPaths = []
    for extension in listExtension:
        for path in listOfPaths:
            if path.endswith(extension):
                validPaths.append(path)
    return validPaths

def filter_list_depth(listOfPaths, mainPath, listDepth):
    '''
    Returns a list with all the paths whose depth wrt to mainPath is equal to 
    one of the value in listDepth 
    If 0, searches only in the specified folder
    If 1, searches only in the folders inside the folder
    If [0,1], searches only in the specified folder and its subfolders
    '''
    listOfPaths = list_operations.make_list(listOfPaths)
    listDepth = list_operations.make_list(listDepth)

    # only works in OR condition: impossible for one file to have two depths at the same time
    validPaths = []
    for depth in listDepth:
        for path in listOfPaths:
            if is_correct_depth(path, mainPath, depth):
                validPaths.append(path)
    return validPaths

def filter_dirs_in_list(dirList, mainDir, listDepth, listPartialName, filterPartNameLogic='AND'):
    '''
    Given a list of directories, returns a list of directories that meet the requirements:
    - their depth wrt to mainDir is equal to one of the values in listDepth
    - their complete path contains: 
        - one of the string in listPartialName (if filterPartNameLogic == 'OR')
        - all the strings in listPartialName (if filterPartNameLogic == 'AND')

    _extended_summary_

    Parameters
    ----------
    dirList : _type_
        _description_
    mainDir : _type_
        _description_
    listDepth : _type_
        _description_
    listPartialName : _type_
        _description_

    Returns
    -------
    string
        contains the valid directories
    '''
    listDepth = list_operations.make_list(listDepth)
    listPartialName = list_operations.make_list(listPartialName)
    if listDepth == [-1]:
        valid_dirs_depth = dirList
    else:
        valid_dirs_depth = filter_list_depth(dirList, mainDir, listDepth)
    valid_dirs_partialName = filter_list_partialName(dirList, listPartialName, 
                                                     filterPartNameLogic)
    valid_dirs = list_operations.merge_lists_logic('AND', [valid_dirs_depth, valid_dirs_partialName])
    return valid_dirs

def filter_files_in_list(dirList, listExt, listPartialName, filterPartNameLogic='AND'):
    '''
     Given a list of directories, returns a list of the files that meet the requirements:
    - their extension is equal to one of the values in listExt
    - their complete path contains: 
        - one of the string in listPartialName (if filterPartNameLogic == 'OR')
        - all the strings in listPartialName (if filterPartNameLogic == 'AND')

    _extended_summary_

    Parameters
    ----------
    dirList : _type_
        _description_
    listExt : _type_
        _description_
    listPartialName : _type_
        _description_

    Returns
    -------
    string
        contains the valid files

    '''
    listExt = list_operations.make_list(listExt)
    listPartialName = list_operations.make_list(listPartialName)
    valid_files_ext = filter_list_extension(dirList, listExt)
    valid_files_partialName = filter_list_partialName(dirList, listPartialName, 
                                                      filterPartNameLogic)
    valid_files = list_operations.merge_lists_logic('AND', [valid_files_ext, valid_files_partialName])
    return valid_files

def print_files_and_dirs(listFilesFound, listDirsFound):
    print('Found files: ')
    for this_file in listFilesFound:
        print(this_file)
    print('-'*10)
    print('Found dirs: ')
    for this_dir in listDirsFound:
        print(this_dir)
    print('-'*10)

def find_files_and_dirs_in_dir(directory, listDepth = [0], listExt = [''], 
    listPartialName = [''], filterPartNameLogic = 'AND', onlyDirs = False, 
    sortOutput = 1, printOutput = False):
    '''
    Given a directory, returns two lists containing the complete paths to every file and to every directory contained for all the depths specified in listDepth.
    If searching files, the extension can be specified in listExt (use "." as first character).
    If searching files or folders, part of the name can be specified in listPartialName. 
    If using filterPartNameLogic == 'AND', only the names containing each partial name specified in list will be considered
    If using filterPartNameLogic == 'OR', only the names containing at least one partial name specified in list will be considered

    onlyDirs can be set to True if searching only for folders to speed up the process

    sortOutput allows to sort the list in output

    printOutput allows to print the output

    Parameters
    ----------
    directory : string
        complete path of the main directory
    listDepth : list, optional
        list of depth (of subfolders) where the files and the dirs are searched, by default 1
        If 0, searches only in the specified folder
        If 1, searches only in the folders inside the folder
        If [0,1], searches only in the specified folder and its subfolders
        If -1, searches iteratively in all the possible subfolders
        by default [0] (only inside the directory specified)
    listExt : list, optional
        list of possible extensions when searching the files, 
        by default [''] (nothing excluded)
    listPartialName : str, optional
        the search excludes all the files and folders not containing it, 
        by default [''] (nothing excluded)
    filterPartNameLogic : str, optional
        If using filterPartNameLogic == 'AND', only the names containing each partial name specified in list will be considered
        If using filterPartNameLogic == 'OR', only the names containing at least one partial name specified in list will be considered
        by default 'AND' (all the partial names should be in the path)
    onlyDirs : bool, optional
        If True, both files and directories are searched
        by default False (both files and dirs are in output)
    sortOutput : bool, optional
        If 1, sorts all the two lists of found files and dirs
        If -1, sorts all the two lists of found files and dirs in reverse
        by default 1
    printOutput : bool, optional
        If True, prints all the found files and dirs, by default False

    Returns
    -------
    tuple 
        of 2 lists containing valid_files and valid_dirs
    '''

    listExt = list_operations.make_list(listExt)
    listDepth = list_operations.make_list(listDepth)
    listPartialName = list_operations.make_list(listPartialName)

    dirs = list_dirs_deep_this_dir(directory, max(listDepth))
    valid_dirs = filter_dirs_in_list(dirs, directory, listDepth, listPartialName, filterPartNameLogic)

    if onlyDirs:
        valid_files = []
    else:
        if listDepth == [-1]:
            # if all directoreis
            dirs_for_files = dirs
            dirs_for_files.append(directory)
        elif listDepth == [0]:
            dirs_for_files = [directory]
        else:
            dirs.append(directory)
            # dirs for files are one level shallower
            dirs_for_files = filter_dirs_in_list(dirs, directory, list(np.array(listDepth)-1), '', filterPartNameLogic)
        files = list_files_in_these_dirs(dirs_for_files)
        valid_files = filter_files_in_list(files, listExt, listPartialName, filterPartNameLogic)
    
    if sortOutput == 1:
        valid_dirs.sort()
        valid_files.sort()
    elif sortOutput == -1:
        valid_dirs.sort(reverse = True)
        valid_files.sort(reverse = True)

    if printOutput:
        print_files_and_dirs(valid_files, valid_dirs)
    
    return (list_operations.make_list(valid_files), list_operations.make_list(valid_dirs))

def get_directory_substring(directory, dir_char, target_substring, steps):
    """
    Get a substring of the directory path based on the given parameters.

    Parameters:
    - directory: String representing the directory path.
    - dir_char: String representing the directory separator character.
    - target_substring: Substring to look for in the directory path.
    - steps: Number of steps before or after the target substring (negative if before, positive if after).

    Returns:
    - Substring of the directory path based on the given parameters.
    """
    parts = directory.split(dir_char)
    try:
        index = parts.index(target_substring)
        new_index = index + steps
        if 0 <= new_index < len(parts):
            return parts[new_index]
        else:
            return "Invalid steps"
    except ValueError:
        return "Target substring not found in the directory path"
    

def get_directory_part(directory, substring, include_substring=True, get_before=True):
    """
    Get the part of the directory path before or after the given substring.

    Parameters:
    - directory: String representing the directory path.
    - substring: Substring to look for in the directory path.
    - include_substring: Boolean flag. If True, include the substring in the result.
    - get_before: Boolean flag. If True, get the part before the substring. If False, get the part after.

    Returns:
    - Part of the directory path based on the given parameters.
    """
    index = directory.find(substring)

    if index != -1:
        if include_substring:
            if get_before:
                return directory[:index + len(substring)]
            else:
                return directory[index:]
        else:
            if get_before:
                return directory[:index]
            else:
                return directory[index + len(substring):]
    else:
        return "Substring not found in the directory path"