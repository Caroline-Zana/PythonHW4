def merge_list(list1, list2):
    if not all(isinstance(x, int) for x in list1) or not all(isinstance(x, int) for x in list2):
        raise TypeError("Input lists should contain only integers.")
    
    merged = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    
    merged.extend(list1[i:])
    merged.extend(list2[j:])

    return merged

