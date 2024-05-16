my_list = ["черешня", "вишня", "груша", "манго", "банан", "апельсин"]
print(my_list)
my_berries, my_fruits = my_list[0], my_list[-1]
print('First element: ', my_berries)
print('Last element:  ',my_fruits)
print('Sublist:       ',my_list[2:5])
my_list[2] = "персик"
print('Modified list: ',my_list, end='\n\n')
##################################################################################################
my_dict = {"cherry": "черешня",  "pear": "персик", "mango": "манго", "banana": "банан", "orange": "апельсин"}
print('Dictionary:          ',my_dict)
print('Translation:         ',my_dict["pear"])
my_dict["cherry"] = "вишня"
print('Modified dictionary: ',my_dict)



