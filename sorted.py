def sort_dictionary(d):

    sorted_by_name = sorted(d.items(), key=lambda x: x[0],reverse=True)

    result = [(name, info[0]) for name, info in sorted_by_name]

    return result

