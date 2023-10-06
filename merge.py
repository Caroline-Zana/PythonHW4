def merge_list(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("be of type list")

    merged_list = list1 + list2

    for item in merged_list:
        if not isinstance(item, int):
            raise TypeError("contain only integers")

    for i in range(len(merged_list) - 1):
        for j in range(len(merged_list) - i - 1):
            if merged_list[j] > merged_list[j+1]:
                merged_list[j], merged_list[j+1] = merged_list[j+1], 
merged_list[j]

    return merged_list
