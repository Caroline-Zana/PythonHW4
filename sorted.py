def sort_dictionary(d):

    sorted_d = sorted(d.items(), key=lambda x: x[1])

    result = [(name, phone) for name, (phone, age) in sorted_by_name]

    return result
