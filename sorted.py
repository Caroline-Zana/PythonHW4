def sort_dictionary(d):
    sorted_by_value = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return sorted_by_value

