def reverse_sort_dictionary(d):

    sorted_items = sorted(d.items(), key=lambda x: x[0], reverse=True)
    
    result = [(name, phone_age[0]) for name, phone_age in sorted_items]
    
    return result

