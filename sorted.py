def sort_dictionary(d): 
	if not isinstance (d, dict):
		raise ValueError ("not valid dictionary.")

	sorted_d = sorted(d. items, key=lambda x: x[0],reverse=True)
	result_list = [(name, data[0]) for name, data in sorted _d]

	return result_list 

