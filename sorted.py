def sort_dictionary(d):
    sorted_dict = sorted(d.items(), key=lambda x: x[1][1], reverse=True)
    sorted_list = [(k, v[0]) for k, v in sorted_dict]
    return sorted_list

