def find_characters_around_substring(s, substring, n, skip = 0):
    '''
    returns the "n" characters in "s" after or before "substring", skipping "skip" characters

    Parameters
    ----------
    s : string
        complete string
    substring : string
        substring to be used for searching
    n : int (positive or negative)
        how many characters after or before (respectively) the occurrence of substring
        if n positive, after
        if n negative, before
    skip: int (positive) or -1
        how many character are skipped after or before (respectively) writing the substring

    Returns
    -------
    substring
    '''
    skip = abs(skip)
    if n>0:
        direction = 'after'
    if n<0:
        direction = 'before'
        n=-n
        skip = - skip
    index = s.find(substring) + skip

    if index == -1:
        return None

    if direction == 'before':
        start_index = max(0, index - n)
        result = s[start_index:index]
    elif direction == 'after':
        end_index = min(len(s), index + len(substring) + n)
        result = s[index + len(substring):end_index]
    else:
        return None

    return result