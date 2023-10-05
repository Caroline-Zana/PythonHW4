def sort_dictionary(input_dict):
    
    sorted_items = sorted(input_dict.items(), key=lambda x: x[1].lower())

    result = [(name, info[1]) for name, info in sorted_items]

    return result
