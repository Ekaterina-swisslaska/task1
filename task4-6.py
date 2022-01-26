my_dict = {	'foo': {'a':12, 'b': (1, 2, 3, 4, my_list)},
			   'bar': {'c':12, 'd': {5, 6, 7, 8}},
	'moo': {'e':12, 'f': {'Lol': ['L', 'o', 'l']}},}
value_b = my_dict["foo"]
print(value_b["b"])
unique_values = set(my_dict)
unique_values.add(9)